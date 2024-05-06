import unittest
from um import count


def test_single_um(self):
    assertEqual(count("Um"), 1)

def test_multiple_um(self):
    assertEqual(count("Um um um"), 3)

def test_no_um(self):
    assertEqual(count("No ums here"), 0)

def test_um_as_substring(self):
    assertEqual(count("This is an umbrella"), 0)

def test_um_as_part_of_word(self):
    assertEqual(count("Crumb"), 0)

def test_case_insensitivity(self):
    assertEqual(count("uM uM uM"), 3)
