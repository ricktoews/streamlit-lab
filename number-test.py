import streamlit as st
import pandas as pd

# Title for the app
st.title("Number Table Generator")

# Input for the number of rows
num_rows = st.number_input("Enter the number of rows:", min_value=1, step=1)

# Generate the data for the table
data = []
for i in range(1, num_rows + 1):
    data.append([i, i ** 2, i ** 3])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=["Number", "Square", "Cube"])

# Display the table
st.write("Generated Table:")
st.dataframe(df)

