#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class Test(unittest.TestCase):
 def test_c(self):
  testcase = "Lovelace, Ada"
  expected = "Ada Lovelace"
  self.assertEqual(rearrange_name(testcase), expected)
unittest.main()
