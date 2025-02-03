from datetime import date, timedelta
from unittest import TestCase

from cal import PataphysicalDate


class TestCal(TestCase):
    def test_first_day(self):
        date_vulg = date(1873, 9, 8)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Sunday 1 Absolu 1")
        pd = PataphysicalDate(1, "Absolu", 1)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_jan_1(self):
        date_vulg = date(2000, 1, 1)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Wednesday 4 Décervelage 127")
        pd = PataphysicalDate(4, "Décervelage", 127)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_day_of_week(self):
        date_vulg = date(2012, 11, 10)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Sunday 8 As 140")
        pd = PataphysicalDate(8, "As", 140)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_leap_vulg(self):
        date_vulg = date(2020, 2, 29)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Friday 6 Pédale 147")
        pd = PataphysicalDate(6, "Pédale", 147)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_leap2(self):
        date_vulg = date(2020, 3, 23)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Sunday 1 Clinamen 147")
        pd = PataphysicalDate(1, "Clinamen", 147)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_leap3(self):
        date_vulg = date(2020, 2, 23)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Sunday 29 Gueules 147")
        pd = PataphysicalDate(29, "Gueules", 147)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_leap4(self):
        date_vulg = date(2020, 2, 24)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Sunday 1 Pédale 147")
        pd = PataphysicalDate(1, "Pédale", 147)
        self.assertEqual(pd.date_vulg, date_vulg)

    def test_gueules(self):
        date_vulg = date(2025, 1, 26)
        pd = PataphysicalDate.from_vulgate(date_vulg)
        self.assertEqual(str(pd), "Sunday 1 Gueules 152")
        pd = PataphysicalDate(1, "Gueules", 152)
        self.assertEqual(pd.date_vulg, date_vulg)

    # TODO: test negative dates? dates before 1873?

    def test_full_non_leap_year(self):
        d = date(1873, 9, 8)
        with open("fixtures/non_leap_year_dump.txt", "r") as f:
            correct_pata_dates = [l.strip() for l in f.readlines()]

        for correct_pata_date in correct_pata_dates:
            self.assertEqual(correct_pata_date, str(PataphysicalDate.from_vulgate(d)))
            pd = PataphysicalDate.from_str(correct_pata_date)
            self.assertEqual(d, pd.date_vulg)
            d += timedelta(days=1)

    def test_full_leap_year(self):
        d = date(2019, 9, 8)

        with open("fixtures/leap_year_dump.txt", "r") as f:
            correct_pata_dates = [l.strip() for l in f.readlines()]

        for correct_pata_date in correct_pata_dates:
            self.assertEqual(correct_pata_date, str(PataphysicalDate.from_vulgate(d)))
            pd = PataphysicalDate.from_str(correct_pata_date)
            self.assertEqual(d, pd.date_vulg)
            d += timedelta(days=1)
