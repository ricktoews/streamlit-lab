def parse_year(year):
    century = year // 100
    short_year = year % 100
    return [century, short_year]

def calc_julian_year(year):
    [century, short_year] = parse_year(year)
    
    leap_days = short_year // 4
    if short_year % 4 != 0:
        leap_days += 1

    offset_days = short_year + leap_days
    
    century_jan = 18 - century
    jan = century_jan + offset_days
    return jan % 7

gregorian_centuries = [6, 5, 3, 1]
def calc_gregorian_year(year):
    [century, short_year] = parse_year(year)
    century_jan = gregorian_centuries[century % 4]

    leap_days = short_year // 4
    if short_year > 0:
        if short_year % 4 == 0:
            leap_days -= 1
        if century % 4 == 0:
            leap_days += 1

    offset_days = short_year + leap_days

    jan = century_jan + offset_days
    return jan % 7

YEAR_TEMPLATE = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
def leap_day(year):
    if year % 400 == 0:
        return 1

    if year < 1600 and year % 4 == 0:
        return 1

    if year % 4 == 0 and year % 100 != 0:
        return 1

    return 0

def get_12_digit_calendar(year):
    jan = 0
    if year < 1582:
        jan = calc_julian_year(year)
    elif year > 1582:
        jan = calc_gregorian_year(year)

    leap_offset = leap_day(year)
    adjusted_template = [x + leap_offset if 3 <= i + 1 <= 12 else x for i, x in enumerate(YEAR_TEMPLATE)]
    calendar_12_digit = [(x + jan) % 7 for x in adjusted_template]

    return calendar_12_digit

