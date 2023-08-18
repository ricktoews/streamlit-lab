import streamlit as st

# Title for the app
st.title("Simple Streamlit App")

# Text input
user_input = st.text_input("Enter something:")

# Displaying user input
st.write("You entered:", user_input)

# Slider widget
slider_value = st.slider("Select a value", 0, 100, 50)

# Displaying the slider value
st.write("Slider value:", slider_value)

# Checkbox widget
checkbox_result = st.checkbox("Check me!")

# Displaying checkbox result
st.write("Checkbox result:", checkbox_result)

# Button widget
button_result = st.button("Click me!")

# Displaying button result
st.write("Button clicked:", button_result)

