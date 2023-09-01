import streamlit as st
import pandas as pd

st.markdown(
    """
<style>
thead tr th:nth-child(1),
tbody tr th:nth-child(1) { display:none; }
</style>
    """,
    unsafe_allow_html=True
)

st.title("The 12-Digit Calendar")

with open("calendar.epub", "rb") as epub:
    st.download_button(label="EPUB", data=epub, file_name="calendar.epub", mime="application/octet-stream")

st.write("""
The year is 2023. The 12-digit calendar for this year is **0 3 3 6 1 4 6 2 5 0 3 5**, with each digit corresponding to its respective month. You find the day of the week by adding the month's digit to the date.

December is the 12th month. As you can see, the 12th digit in the calendar is 5. To find the day of the week for December 25, 2023, add 25 to 5, for a sum of 30.

The weekly cycle is seven days, so we can ignore the first 28 of the 30, leaving 2. The second day of the week is Monday.

December 25, 2023 is a Monday.
""")

st.header("Basics")

st.write("""
When working with calendars, there are a few things that will make life ever so much simpler: The multiplication table, division and getting remainders, and identifying leap years.
        
*The Multiplication Table*. Especially the 7s and the 4s. Working with calendars involves a lot of 7s, since that's how many days there are in the week. If you know that 35 is divisible by 7, or that 51 divided by 7 leaves a remainder of 2, you're in good shape.
        
*Remainders / x modulo y*. Something you'll do all the time is get sums and then divide by 7 and take the remainder. For this, we'll use the term “modulo”: The sum of 9 and 32, modulo 7 is 6. The sum of 75, 18, 5, and 25, modulo 7 is 4. If you're add numbers and find that your sum is getting unwieldy, you can take modulo 7 at any time, just to get a more comfortable value to work with. Since the weekly cycle is 7 days, modulo 7 will usually make no difference to the final result.
        
*Leap Years*. We all know that, generally speaking, every fourth year is a leap year. So 2008 was a leap, as were 2012 and 2016. How about 1986? Or 1972? You'll want to be able to easily identify leap years.
        
And you will also want to be familiar with...
""")

st.subheader("The 12-digit Calendar")

st.write("""
The concept of the 12-digit calendar is simple. Each of the 12 months is represented by a “month offset,” which is a single-digit number in the range of 0 - 6.

If you open a calendar app and look at the calendar grid for the year, you'll see the standard set of four or five “week” rows in a given month.

You'll also notice that the top row for most months has fewer than seven “date” numbers. If the first day of the month is, say, Tuesday, the top row will have an empty spot for Sunday and Monday. If the first day of the month is Saturday, the top row will have six empty spots: Sunday through Friday. And so on. The number of empty spots for a month is the "month offset."
        
For the year 2023, the 12-digit calendar is:
""")

data = [
    {"month": "January", "offset": 0},
    {"month": "February", "offset": 3},
    {"month": "March", "offset": 3},
    {"month": "April", "offset": 6},
    {"month": "May", "offset": 1},
    {"month": "June", "offset": 4},
    {"month": "July", "offset": 6},
    {"month": "August", "offset": 2},
    {"month": "September", "offset": 5},
    {"month": "October", "offset": 0},
    {"month": "November", "offset": 3},
    {"month": "December", "offset": 5}
]

df = pd.DataFrame(
    data
)
st.table(df)

st.write("""
(Coincidentally, because January of 2023 has an offset of 0, the calendar for this year also serves as a generic 12-digit calendar, which will be used in calculations for any year. It would make sense to memorize this if you have continued interest in the calendar.)
""")

st.subheader("Practical Use: Finding the Day of the Week")

st.write("""
To find the day of the week, all you have to do is add the date to the month offset, and take modulo 7. If the result is 1 - 6, the day of the week is Sunday - Friday. If the result is 0, the day of the week is Saturday. This is because Saturday is day 7 in the weekly cycle, and 7 modulo 7 is 0.

Let's try an example: March 17, 2023. The month offset for March 2023 is 3. Add 3 to 17, giving a sum of 20.  20 modulo 7 is 6. The 6th day of the week is Friday. So March 17, 2023 was a Friday.

How about October 28? The month offset for October 2023 is 0. The sum of 0 and 28, modulo 7 is 0. That's a Saturday, since Saturday is the 7th day, and 7 modulo 7 is 0.

So that's the basics.

For any year, you can get the 12-digit calendar just by looking at the months for that year and getting the month offset, or the number of empty spaces before the first day of each month. Then, armed with a 12-digit calendar, you can find the day of the week for any date in that year.

Next, we're going to look at finding the 12-digit calendar for any year. We'll also look at directly calculating the day of the week for any date, without getting the calendar first.
""")

st.header("A Little More Ambitious")

st.write("""        
So now, having achieved mastery of the basic concept of the 12-digit calendar, let's move on to the more ambitious concept of calculating the 12 digits for a given year–without needing an actual month layout for reference.

We'll start with years in the 21st century, and we'll use 2025 as an example. Here's what you do: Take the two-digit year (25), and add the leap days (6). Then, to get the 12-digit calendar, add the sum (31) to the generic month offset (see above) for each month. (At any point in this process, you can take modulo 7 if you want a smaller number to work with. For 31, that's 3.)

NOTE: We get the leap days by dividing the two-digit year by 4. If there's a remainder, we ignore it. Since 25 divided by 4 is 6, we add 6 leap days.

For 2025, adding 3 to the generic offset for each month, we get:
""")

data = [
    {"Month": "January:", "Calculation": "0 + 3 = 3"},
    {"Month": "February:", "Calculation": "3 + 3 = 6"},
    {"Month": "March:", "Calculation": "3 + 3 = 6"},
    {"Month": "April:", "Calculation": "6 + 3 = 9, modulo 7 = 2"},
    {"Month": "May:", "Calculation": "1 + 3 = 4"},
    {"Month": "June:", "Calculation": "4 + 3 = 7, modulo 7 = 0"},
    {"Month": "July:", "Calculation": "6 + 3 = 9, modulo 7 = 2"},
    {"Month": "August:", "Calculation": "2 + 3 = 5"},
    {"Month": "September:", "Calculation": "5 + 3 = 8, modulo 7 = 1"},
    {"Month": "October:", "Calculation": "0 + 3 = 3"},
    {"Month": "November:", "Calculation": "3 + 3 = 6"},
    {"Month": "December:", "Calculation": "5 + 3 = 8, modulo 7 = 1"},
]

st.table(data)
        
st.write("""
So the 12-digit calendar for 2025 is **3 6 6 2 4 0 2 5 1 3 6 1**.

Let's put it to use by finding the day of the week for Halloween. October's offset is 1, plus 31 is 32, modulo 7 is 4. So Halloween 2025 is a Wednesday.
""")

st.subheader("What about leap years?")

st.write("""
If you're going for a leap year, follow the same steps as for a normal year, but then adjust the month offsets for January and February by subtracting 1 from each.

Let's try it with 2024. Take the two-digit year (24), and add the leap days (6). The sum is 30, modulo 7 is 2.

Add 2 to the generic offset for each month, and subtract 1 for January and February:
""")

data = [
    {"Month": "January:", "Calculation": "0 + 2 - 1 = 1"},
    {"Month": "February:", "Calculation": "3 + 2 - 1 = 4"},
    {"Month": "March:", "Calculation": "3 + 2 = 5"},
    {"Month": "April:", "Calculation": "6 + 2 = 8, modulo 7 = 1"},
    {"Month": "May:", "Calculation": "1 + 2 = 3"},
    {"Month": "June:", "Calculation": "4 + 2 = 6"},
    {"Month": "July:", "Calculation": "6 + 2 = 8, modulo 7 = 1"},
    {"Month": "August:", "Calculation": "2 + 2 = 4"},
    {"Month": "September:", "Calculation": "5 + 2 = 7, modulo 7 = 0"},
    {"Month": "October:", "Calculation": "0 + 2 = 2"},
    {"Month": "November:", "Calculation": "3 + 2 = 5"},
    {"Month": "December:", "Calculation": "5 + 2 = 7, modulo 7 = 0"},
]

st.table(data)

st.write("""
So the 12-digit calendar for 2024 is **1 4 5 1 3 6 1 4 0 2 5 0**.

So there it is. In a few simple steps, you can get a calendar for any year in the 21st century.
""")

st.subheader("Now, how about for earlier years?")

st.write("""
You can extend the above technique to any year, just by adding the century offset for that year.

**Century offset**

The century offsets for 1600 - 1900:
""")

data = [
    {"Century Year": "1900:", "Offset": "1"},
    {"Century Year": "1800:", "Offset": "3"},
    {"Century Year": "1700:", "Offset": "5"},
    {"Century Year": "1600:", "Offset": "0"},
    {"Century Year": "Earlier century years:", "Offset": "19 minus century year / 100:"},
    {"Century Year": "1500:", "Offset": "19 - 15 = 4"},
    {"Century Year": "1400:", "Offset": "19 - 14 = 5"},
     {"Century Year": "1300:", "Offset": "19 - 13 = 6"},
     {"Century Year": "1200:", "Offset": "19 - 12 = 7, mod 7 = 0"},
     {"Century Year": "1100:", "Offset": "19 - 11 = 8, mod 7 = 1 "},
     {"Century Year": "and so on", "Offset": ""}
]

st.table(data)
        
st.write("""
So let's see how the century offset is used.

Example: 1975. That's in the 1900s, so the century offset is 1. Take the two-digit year (75), and add the leap days (18). Now, add the century offset (1). Take modulo 7, giving a result of 3. Construct the calendar for 1975 by adding 3 to each generic offset: 3 6 6 2 4 0 2 5 1 3 6 1.  [Note, 75 modulo 7 is 5, and 18 modulo 7 is 4. 5 + 4 + 1 is 10, modulo 7 is 3.]

How about for a leap year? 900. This time, the century offset is 19 - 9 = 10, modulo 7 = 3. So take the two-digit year (00), add the leap days (0). Then add the century offset of 3. The result is 3. The 12-digit calendar, with January and February adjusted for the leap year, is 2 5 6 2 4 0 2 5 1 3 6 1. New Year's Day was a Tuesday, and Christmas Day was a Thursday.
""")

st.subheader("Calculate Just Day of Week")
        
st.write("""
OK, that's great, but what if you don't care about getting the 12-digit calendar, per se, and you just want to get the day of the week for a particular date?

This is very similar to the above. All you have to do is add the two-digit year, the leap days, the generic month offset for the target month, and the date. Then, if the year is a leap year and the target month is January or February, subtract 1. Take modulo 7, and the result is the day of the week.

Example: Christmas Day, 2037. Two-digit year (37), leap days (9), generic month offset for December (5), date (25). The sum of those, modulo 7 is 6. So December 25, 2037 is a Friday.
        
Another: January 1, 2044. Two-digit year: 44, leap days: 11, month offset for January: 0, date: 1. The sum of those is 56. Since this is a leap year, and the month is January, subtract 1. Then take 55 modulo 7, which is 6. January 1, 2044 is a Friday.

Other examples:

January 1, 1933. Sunday: Two-digit year (33), leap days (8), month offset (0), date (1), century offset (1); sum modulo 7 is 1.

July 4, 1776. Thursday: Two-digit year (76), leap days (19), month offset (6), date (4), century offset (5); modulo 7 = 5.

December 25, 1621. Saturday. Two-digit year (21), leap days (5), month offset (5), date (25), century offset (0); modulo 7 = 0.

August 16, 1117. Thursday. Two-digit year (17), leap days (4), month offset (2), date (16), century offset (8); modulo 7 = 5.

February 4, 1872. Sunday. Two-digit year (72), leap days (18), month offset (3), date (4), century offset (3), leap year adjustment for February (-1); modulo 7 = 1.

That's pretty much it. Become comfortable with the generic month offsets and the century offsets, and you can get a calendar for any year, or directly find the day of the week for any date.

Except...
""")

st.header("The Calendar Change. October 1582.")

st.write("""        
The official word is that 10 days were dropped from the calendar in October 1582, so that Thursday, October 4 was followed by Friday, October 15.

So, while what we've covered will allow you to calculate most dates in the 1500s, it will fail spectacularly for anything after October 4 in the 16th century.

So here's what you do. Instead of getting the century offset by subtracting 15 from 19, treat the last nearly two decades of the 1500s as if they were from the 1900s, and use 1 as the century offset. This should give you a Friday for October 15, 1582:

Two-digit year (82), leap days (20), month offset (0), date (15), century offset (1); modulo 7 = 6. Friday.

Huzzah!

The calendar for 1582 is weird: **1 4 4 0 2 5 0 3 6 1 … October gets mangled … 5 1 3**
""")
