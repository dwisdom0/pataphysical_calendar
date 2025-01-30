from calendar import isleap
from datetime import date




# TODO: this is probably the wrong way
# I think I should be passing pataphysical dates to this class
# and then it can convert to vulgate internally
# instead of passing vulgate and then having it convert to pataphysical
#
# What I really want is an extension of the datetime class
# that adds a method like to_pataphysical()
# that just prints the pataphysical date
# or retuns 
# but I'll keep goin with this for now

# TODO: refactor to make it like
# PataphysicalDate.from_vulgate(datetime)


class PataphysicalDate:
  def __init__(self, year_vulg, month_vulg, day_vulg):
    self.year_vulg = year_vulg
    self.month_vulg = month_vulg
    self.day_vulg = day_vulg
    self.date_vulg = date(year_vulg, month_vulg, day_vulg)

    # first figure out if it's a leap year
    # leap years are every 4 years since 1872
    # (i.e., every 4 years since 1 before
    # the start of pataphysical time)
    # If Google Translate is to be believed
    # and 1872 was a leap year in vulgate

    # started on 1873-09-08
    self.year = self.year_vulg - 1873
    if self.date_vulg >= date(self.year_vulg, 9, 8):
      self.year += 1
    assert self.year is not None

    is_leap = (self.year + 1) % 4 == 0



    months = [
      'Absolu',
      'Haha',
      'As',
      'Sable',
      'Decervelage',  # technically there's supposed to be an acute accent on the first e
      'Gueules',
      'Pedale',  # acute on first e
      'Clinamen',
      'Palotin',
      'Merde',
      'Gidouille',
      'Tatane',
      'Phalle'
    ]

    month_starts = [
      date(self.year_vulg, 9, 8),
      date(self.year_vulg, 10, 6),
      date(self.year_vulg, 11, 3),
      date(self.year_vulg, 12, 1),
      date(self.year_vulg, 12, 29),
      date(self.year_vulg, 1, 26),
      date(self.year_vulg, 2, 24) if is_leap else date(self.year_vulg, 2, 23),
      date(self.year_vulg, 3, 23),
      date(self.year_vulg, 4, 20),
      date(self.year_vulg, 5, 18),
      date(self.year_vulg, 6, 15),
      date(self.year_vulg, 7, 14),
      date(self.year_vulg, 8, 11),
    ]

    self.month = None
    month_idx = None
    for i in range(len(month_starts)):
      if month_starts[i] <= self.date_vulg and\
         self.date_vulg < month_starts[(i+1)%len(month_starts)]:
        self.month = months[i]
        month_idx = i

    if self.month is None and \
       date(self.year_vulg, 12, 29) <= self.date_vulg and \
       self.date_vulg <= date(self.year_vulg, 12, 31):
       self.month = 'Decervelage'
       month_idx = 4

    elif self.month is None and \
       date(self.year_vulg, 1, 1) <= self.date_vulg and \
       self.date_vulg <= date(self.year_vulg, 1, 25):
       self.month = 'Decervelage'
       month_idx = 4

    assert self.month is not None
    assert month_idx is not None


    # have to do another special case for the days between the end of the vulgate year
    # and the month that starts on jan 26
    self.day = None
    if date(year_vulg, 1, 1) <= self.date_vulg and self.date_vulg <= date(year_vulg, 1, 25):
      self.day = (self.date_vulg - date(self.year_vulg - 1, 12, 29)).days
    else:
      self.day = (self.date_vulg - month_starts[month_idx]).days
    assert self.day is not None
    self.day += 1



    # day of week is probably going to be harder
    # or actually manybe it's easier?
    # I think every month is aligned to start on a sunday
    # since they have 28 days
    # and then the one (or two) month(s) with 29 days will end on a Sunday
    # and the next month will start with another Sunday
    days_of_week = [
      'Sunday',
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday'
    ]

    # depends on index -1 being the last item in the list
    self.day_of_week = days_of_week[(self.day % len(days_of_week)) - 1]



  def __repr__(self):
    return f'{self.day_of_week} {self.day} {self.month} {self.year}'

if __name__ == '__main__':
  pd_easy = PataphysicalDate(2024, 5, 16)
  pd_endpoint = PataphysicalDate(2024, 8, 15)
  pd_year_incr = PataphysicalDate(2024, 11, 6)

  # wikipedia examples
  # I guess these should be test cases

  # should be 1 Absolu 1
  pd_start = PataphysicalDate(1873, 9, 8)

  # should be 4 Decervelage 127
  pd_jan_2000 = PataphysicalDate(2000, 1, 1)

  # should be 8 As 140 (Sunday)
  pd_dow = PataphysicalDate(2012, 11, 10)


