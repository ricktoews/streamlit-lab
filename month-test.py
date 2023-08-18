import streamlit as st
import calendar

# Set the year and month
year = 2023
month = 8

# Create a calendar instance
cal = calendar.month(year, month)

# Title for the app
st.title("Calendar App")

# Display the calendar
st.text(cal)

