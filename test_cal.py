from datetime import date, timedelta
from unittest import TestCase

from cal import PataphysicalDate


class TestCal(TestCase):
  maxDiff = None

  def test_first_day(self):
    pd = PataphysicalDate(1873, 9, 8)
    self.assertEqual(str(pd), "Sunday 1 Absolu 1")

  def test_jan_1(self):
    pd = PataphysicalDate(2000, 1, 1)
    self.assertEqual(str(pd), "Wednesday 4 Decervelage 127")

  def test_day_of_week(self):
    pd = PataphysicalDate(2012, 11, 10)
    self.assertEqual(str(pd), "Sunday 8 As 140")


  # TODO: more tests
  # test the 29th on the two months that have that
  # honestly could proably just print out an entire year and compare it
  # one for leap eyar and non-leap year

  # TODO: test negative dates? dates before 1873?

  def test_print_non_leap_year(self):
    d = date(1873, 9, 8)
    to_compare = ''
    for _ in range(365):
      to_compare += str(PataphysicalDate(d.year, d.month, d.day)) + '\n'
      d += timedelta(days=1)
    with open("fixtures/non_leap_year_dump.txt", "r") as f:
      text = f.read()
    self.assertEqual(text, to_compare)

  def test_print_leap_year(self):
    d = date(2019, 9, 8)
    to_compare = ''
    for _ in range(366):
      to_compare += str(PataphysicalDate(d.year, d.month, d.day)) + '\n'
      d += timedelta(days=1)
    with open("fixtures/leap_year_dump.txt", "r") as f:
      text = f.read()
    self.assertEqual(text, to_compare)


