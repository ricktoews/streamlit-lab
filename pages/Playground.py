import streamlit as st
import calendar
import random

calendar.setfirstweekday(calendar.SUNDAY)

MONTH_OFFSETS = [-1, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

DOW = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def leap_admustment(year, month):
    if month >= 3:
        return 0
    
    if year % 400 == 0:
        return 1
    
    if year % 100 == 0 and year < 1600:
        return 1
    
    if year % 4 == 0 and year % 100 > 0:
        return 1
    
    return 0


def calc_century_offset(year):
    century_year = year // 100
    offset = 0

    if century_year >= 16:
        offset = 7 - (century_year % 4 * 2)

    else:
        offset = 19 - century_year

    return offset % 7

def random_year_range(century_range):
    min_year = (century_range[0] - 1) * 100 + 1
    max_year = century_range[1] * 100
    # Define the range of years
    year_range = range(min_year, max_year)
    
    # Define the weights for each year range
    weights = [1] * 1699  # Years 1 to 1699 with weight 1
    weights += [10] * 501  # Years 1700 to 2200 with weight 10
    
    # Randomly select a year based on the weights
    selected_year = random.choices(year_range)[0]
    
    return selected_year

@st.cache_data
def get_random_date(century_range):
    # Generate a random year using the function
    random_year = random_year_range(century_range)
    random_month = random.randint(1, 12)
    max_date = calendar.monthrange(random_year, random_month)[1]
    random_date = random.randint(1, max_date)
    random_month_name = calendar.month_name[random_month]
    two_digit_year = random_year % 100
    leap_days = two_digit_year // 4
    month_offset = MONTH_OFFSETS[random_month]
    century_offset = calc_century_offset(random_year)

    return [random_year, two_digit_year, random_month, random_month_name, random_date, leap_days, month_offset, century_offset]


def calc_dow(year, leap_days, month_offset, date, century_offset):
    result = year + leap_days + month_offset + date + century_offset
    return result % 7


st.title("Calendar Playground")

century_range = st.slider("Century Rante", min_value=1, max_value=23, value=[20, 21])

play_date = get_random_date(century_range)

[year, two_digit_year, month_num, month, date, leap_days, month_offset, century_offset] = play_date

st.write(f"What day of the week is {month} {date}, {year}?")
st.write("If the date is in January or February of a leap year, adjust the Month offset.")

cols = st.columns(5)

with cols[0]:
    entered_year = st.number_input("Two-digit Year", min_value=0, max_value=99)

with cols[1]:
    entered_leap_days =  st.number_input("Leap days", min_value=0, max_value=25)

with cols[2]:
    entered_month_offset = st.number_input("Month offset", min_value=0, max_value=6)

with cols[3]:
    entered_date = st.number_input("Date", min_value=1, max_value=31)

with cols[4]:
    entered_century_offset = st.number_input("Century offset", min_value=0, max_value=6)

st.write(entered_year, entered_leap_days, entered_month_offset, entered_date, entered_century_offset)

if entered_year is not None and entered_leap_days is not None and entered_month_offset is not None and entered_date is not None and entered_century_offset is not None:
    dow = calc_dow(entered_year, entered_leap_days, entered_month_offset, entered_date, entered_century_offset)
    check_dow = calc_dow(two_digit_year, leap_days, month_offset, date, century_offset)

    st.write(DOW[dow])
    st.write(DOW[check_dow])

    if dow == check_dow:
        if st.button("Another?"):
            # Invalidate the cache by changing a session variable
            st.cache_data.clear()
