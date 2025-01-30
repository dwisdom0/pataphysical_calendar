from datetime import date


class PataphysicalDate:
    def __init__(
        self, year: int, month: str, day: int, day_of_week: str, date_vulg: date
    ):
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week
        self.date_vulg = date_vulg

    @classmethod
    def from_vulgate(cls, date_vulg: date):
        year = date_vulg.year - 1873
        if date_vulg >= date(date_vulg.year, 9, 8):
            year += 1

        months = [
            "Absolu",
            "Haha",
            "As",
            "Sable",
            "Decervelage",  # technically there's supposed to be an acute accent on the first e
            "Gueules",
            "Pedale",  # acute on first e
            "Clinamen",
            "Palotin",
            "Merde",
            "Gidouille",
            "Tatane",
            "Phalle",
        ]

        month_starts = [
            date(date_vulg.year, 9, 8),
            date(date_vulg.year, 10, 6),
            date(date_vulg.year, 11, 3),
            date(date_vulg.year, 12, 1),
            date(date_vulg.year, 12, 29),
            date(date_vulg.year, 1, 26),
            date(date_vulg.year, 2, 24)
            if cls.is_leap(year)
            else date(date_vulg.year, 2, 23),
            date(date_vulg.year, 3, 23),
            date(date_vulg.year, 4, 20),
            date(date_vulg.year, 5, 18),
            date(date_vulg.year, 6, 15),
            date(date_vulg.year, 7, 14),
            date(date_vulg.year, 8, 11),
        ]

        # search through the months to find the one our date is in
        month = None
        month_idx = None
        for i in range(len(month_starts)):
            if (
                month_starts[i] <= date_vulg
                and date_vulg < month_starts[(i + 1) % len(month_starts)]
            ):
                month = months[i]
                month_idx = i

        # special casses for dates in the month that wraps around
        # dates from december 29 through the end ofthe year
        # and Januarary 1 through to the start of the next month
        if (
            month is None
            and date(date_vulg.year, 12, 29) <= date_vulg
            and date_vulg <= date(date_vulg.year, 12, 31)
        ):
            month = "Decervelage"
            month_idx = 4

        elif (
            month is None
            and date(date_vulg.year, 1, 1) <= date_vulg
            and date_vulg <= date(date_vulg.year, 1, 25)
        ):
            month = "Decervelage"
            month_idx = 4

        assert month is not None
        assert month_idx is not None

        # have to do another special case for the days between the end of the vulgate year
        # and the month that starts on jan 26
        day = None
        if date(date_vulg.year, 1, 1) <= date_vulg and date_vulg <= date(
            date_vulg.year, 1, 25
        ):
            day = (date_vulg - date(date_vulg.year - 1, 12, 29)).days
        else:
            day = (date_vulg - month_starts[month_idx]).days
        assert day is not None
        day += 1

        days_of_week = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        # depends on index -1 being the last item in the list
        day_of_week = days_of_week[(day % len(days_of_week)) - 1]

        return cls(year, month, day, day_of_week, date_vulg)

    @staticmethod
    def is_leap(year):
        """
        determines whether a Pataphysical year is a leap year
        """
        return (year + 1) % 4 == 0

    def __repr__(self):
        return f"{self.day_of_week} {self.day} {self.month} {self.year}"


if __name__ == "__main__":
    pd_easy = PataphysicalDate.from_vulgate(date(2024, 5, 16))
    pd_endpoint = PataphysicalDate.from_vulgate(date(2024, 8, 15))
    pd_year_incr = PataphysicalDate.from_vulgate(date(2024, 11, 6))

    # wikipedia examples
    # I guess these should be test cases

    # should be 1 Absolu 1
    pd_start = PataphysicalDate.from_vulgate(date(1873, 9, 8))

    # should be 4 Decervelage 127
    pd_jan_2000 = PataphysicalDate.from_vulgate(date(2000, 1, 1))

    # should be 8 As 140 (Sunday)
    pd_dow = PataphysicalDate.from_vulgate(date(2012, 11, 10))
