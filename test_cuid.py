import unittest
import timeit
import cuid

class TestHelpers(unittest.TestCase):
    """
    Test the helper functions for generating cuids
    """
    def test_base36(self):
        known_mappings = {
            96192: "2280",
            53248: "1534",
            84896: "1ti8",
            28355: "lvn",
            57908: "18ok",
            52478: "14hq",
            88436: "1w8k",
            93482: "204q",
            19069: "epp",
            97614: "23bi",
            0: "0",
        }

        for k, v in known_mappings.items():
            self.assertEqual(cuid._to_base36(k), v)

    def test_pad(self):
        self.assertEqual("001234", cuid._pad("1234", 6))
        self.assertEqual("234", cuid._pad("1234", 3))


    def test_random_block(self):
        """
        Test that a 'random' block is the right size and that
        successive blocks are not the same. Not the best test,
        but a start.
        """
        blocks = [cuid._random_block() for i in range(10)]
        for b in blocks:
            self.assertEqual(len(b), cuid.BLOCK_SIZE)

        self.assertEqual(len(set(blocks)), len(blocks))


class TestCuid(unittest.TestCase):

    def setUp(self):
        self.generator = cuid.CuidGenerator()

    def test_module_works(self):
        full_cuid = cuid.cuid()
        self.assertEqual(len(full_cuid), 25)
        slug = cuid.slug()
        self.assertEqual(len(slug), 7)

    def test_get_process_fingerprint(self):
        """
        Ensure that the system fingerprint generator returns
        a string of the right length, and does so consistently
        on the same system.
        """
        first = cuid.get_process_fingerprint()
        second = cuid.get_process_fingerprint()
        self.assertEqual(len(first), 4)
        self.assertEqual(first, second)

    def test_safe_counter(self):
        """
        Ensure that the generator's counter increments, and
        rolls over after the full range of cuid.DISCRETE_VALUES
        has been explored
        """
        val = self.generator.counter
        val2 = self.generator.counter
        self.assertGreater(val2, val)
        self.generator._counter = cuid.DISCRETE_VALUES - 1
        val3 = self.generator.counter
        self.assertEqual(val3, 0)

    def test_generates_string(self):
        self.assertIsInstance(self.generator.cuid(), str)

    def test_format_matches(self):
        ident = self.generator.cuid()
        self.assertEqual(len(ident), 25)
        self.assertEqual(ident[0], "c")

    def test_no_collisions(self):
        seen = set()
        for i in range(99999):
            seen.add(self.generator.cuid())
        self.assertEqual(len(seen), 99999)

    def test_few_collisions_with_slug(self):
        seen = set()
        for i in range(5000):
            seen.add(self.generator.slug())
        # Confirm that <10% collide
        self.assertLess(5000 - len(seen), 50)

    def test_sequential(self):
        previous = self.generator.cuid()
        for i in range(99999):
            current = self.generator.cuid()
            self.assertLess(previous, current)
            previous = current

    def test_is_fast(self):
        """Ensure that several cuids can be generated per millisecond"""
        setup_stmt = "import cuid; g = cuid.CuidGenerator()"
        timed_stmt = "g.cuid()"
        times = 9999
        time_to_run = timeit.timeit(timed_stmt, setup=setup_stmt, number=times)
        time_each = time_to_run / times
        self.assertLess(time_each, 0.0002)
        print("{:.6f}ms / cuid".format(time_each * 1000))


if __name__ == "__main__":
    unittest.main()
