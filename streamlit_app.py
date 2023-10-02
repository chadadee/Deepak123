import streamlit
streamlit.title('My Parents new healthy dinner')
streamlit.header('Break fast Menu')
streamlit.text('🥑Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free Range Egg')
streamlit.text('🍞Upma or Dosa')
streamlit.text('🥣Oat Meal Upma with veggies')
streamlit.text('🥗Multigrain vegggies')
streamlit.text('🐔Boiled Eggs with banana')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
