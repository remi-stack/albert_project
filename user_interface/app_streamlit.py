import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
from scripts.datasourcing import fetch_quotes

# Header
st.header("Welcome to Our Cool Streamlit App 🎉")

# Introduction Text
st.markdown("""
This app demonstrates some of the cool features of Streamlit, including data fetching, interactive sliders, image display, and data visualization. Enjoy exploring!
""")

# Get_data button
def get_hello():
    r = requests.get('http://127.0.0.1:5000')
    return pd.read_json(r.json(), orient='split')

if st.button("Get training data!"):
    data = get_hello()
    st.write(data)
    st.success("Data loaded successfully!")

# Select_id_menu
option = st.selectbox(
    'How would you like to be contacted?',
    ('911157302', '926424', '92753'))

st.write('You selected:', option)

# Slider example
age = st.slider('Select an age', 0, 130, 25)
st.write("You've selected:", age, "years old")

# Display the image
st.image("https://storage.googleapis.com/pod_public/1300/150707.jpg", caption="Streamlit is awesome!", width=300)



# Generating a fake dataset
np.random.seed(42)  # For reproducible results
x = np.arange(10)  # X values
y = np.random.rand(10) * 100  # Y values, randomly generated

# Creating a plot
st.subheader("Fake Data Visualization")
fig, ax = plt.subplots()
ax.bar(x, y, color='b', label="Fake Data")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Simple Plot of Fake Data")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Display a dataframe in Streamlit
st.subheader("Quotes Data")

#url to paste : https://quotes.toscrape.com/
base_url = st.text_input("Enter the URL to scrape:")
if base_url:
    quotes_data = fetch_quotes(base_url)
    st.write(pd.DataFrame(quotes_data))
    st.success("Data loaded successfully!")
