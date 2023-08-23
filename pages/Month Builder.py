import streamlit as st
import calendar
from calc_month import calc_gregorian_year, get_12_digit_calendar
from build_calendar import build_calendar

calendar.setfirstweekday(calendar.SUNDAY)

# Title for the app
st.title("Month Builder")

# List of month names for autocompletion
month_names = [
    "--- Month ---", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox("Select a month:", month_names)

# Create a datalist element with month names
with col2:
    year_str = st.text_input("Year:")

month_index = month_names.index(selected_month)

#month_str = st.text_input("Month:")

# HTML and CSS for styling
style = """
<style>
table {
    border-collapse: collapse;
    width: 100%;
    border: 2px solid #f90;
}

th, td {
    border: 1px solid #ddd;
    text-align: center;
    padding: 8px;
}

th {
    background-color: #09f;
    text-align: center;
    color: white;
}

tr:nth-child(1) td {
    background-color: #f2f2f2;
}
</style>
"""

# Display the CSS style
st.markdown(style, unsafe_allow_html=True)

if month_index > 0 and year_str > "":
    year = int(year_str)
    month = month_index
    
    calendar_12_digit = get_12_digit_calendar(year)
    month_offset = calendar_12_digit[month_index - 1]
    discard, days_in_month = calendar.monthrange(year, month)

    # Get the name of the month
    month_name = calendar.month_name[month]

    # Display the month name
    st.markdown(f"## {month_name}")

    # Create a calendar instance
    #cal = calendar.monthcalendar(year, month)
    cal = build_calendar(month_offset, days_in_month)

    # Create a table with the month dates
    table = "<table>"
    # Add the day names row
    table += "<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>"
    # Add the calendar rows
    for week in cal:
        table += "<tr>"
        for day in week:
            if day == 0:
                table += "<td></td>"
            else:
                table += f"<td>{day}</td>"
        table += "</tr>"
    table += "</table>"

    # Display the calendar table
    st.markdown(table, unsafe_allow_html=True)

