import streamlit
streamlit.title('My Mom''s New Healthy Dinner')
streamlit.header('Break fast Favorites')
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
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
