#!/usr/bin/env python

"""Tests for `textstego` package."""


import unittest

from textstego import Stego1 as stego1
from textstego import Stego2 as stego2


class TestTextstego(unittest.TestCase):
    """Tests for `textstego` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.cover = "This is a secret message."
        self.bits = "10101"
        self.stego1 = stego1()
        self.stego2 = stego2()


    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test extraction of hidden bits"""
        stego = self.stego1.encode(self.cover, self.bits)
        print(f"Encoded bits {self.bits} into message: {stego}.")
        extract = self.stego1.decode(stego)
        print(f"Extracted bits: {extract}")
        self.assertEqual(extract, self.bits)

    def test_001(self):
        """ Test stego 2 """
        cover = "Hello"
        bits = "10101"
        stego = self.stego2.encode(cover, bits)
        extract = self.stego2.decode(stego)
        self.assertEqual(extract, self.bits)

if __name__ == "__main__":
    unittest.main()
