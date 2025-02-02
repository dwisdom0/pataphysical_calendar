from datetime import date, timedelta


class PataphysicalDate:
    def __init__(self, day: int, month: str, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.day_of_week = self.get_dow(day)

        year_vulg = year + 1873 - 1

        # convert pataphysical to vulgate
        month_starts = {
            "Absolu": date(year_vulg, 9, 8),
            "Haha": date(year_vulg, 10, 6),
            "As": date(year_vulg, 11, 3),
            "Sable": date(year_vulg, 12, 1),
            "Décervelage": date(year_vulg, 12, 29),
            "Gueules": date(year_vulg, 1, 26),
            "Pédale": date(year_vulg, 2, 24) if self.is_leap(year) else date(year_vulg, 2, 23),
            "Clinamen": date(year_vulg, 3, 23),
            "Palotin": date(year_vulg, 4, 20),
            "Merde": date(year_vulg, 5, 18),
            "Gidouille": date(year_vulg, 6, 15),
            "Tatane": date(year_vulg, 7, 14),
            "Phalle": date(year_vulg, 8, 11),
        }

        date_vulg = month_starts[month] + timedelta(days=day - 1)

        if date_vulg < date(year_vulg, 9, 8):
            date_vulg = date_vulg + timedelta(days=365)

        # extra correction for leap years
        if self.is_leap(year) and month in (
            "Clinamen",
            "Palotin",
            "Merde",
            "Gidouille",
            "Tatane",
            "Phalle",
        ):
            date_vulg = date_vulg + timedelta(days=1)

        self.date_vulg = date_vulg

    @classmethod
    def from_str(cls, s: str):
        """
        Assume day month year order
        with no other puncuation
        """
        items = s.strip().split()
        # have to drop the day-of-week at the beginning
        if items[0].lower() in (
            "sunday",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
        ):
            items = items[1:]
        items[0] = int(items[0])
        items[2] = int(items[2])

        return cls(*items)

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
            "Décervelage",
            "Gueules",
            "Pédale",
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
            month = "Décervelage"
            month_idx = 4

        elif (
            month is None
            and date(date_vulg.year, 1, 1) <= date_vulg
            and date_vulg <= date(date_vulg.year, 1, 25)
        ):
            month = "Décervelage"
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

        return cls(day, month, year)

    @staticmethod
    def is_leap(year):
        """
        determines whether a Pataphysical year is a leap year
        """
        return (year + 1) % 4 == 0

    @staticmethod
    def get_dow(day):
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
        return days_of_week[(day % len(days_of_week)) - 1]

    def __repr__(self):
        return f"{self.day_of_week} {self.day} {self.month} {self.year}"


