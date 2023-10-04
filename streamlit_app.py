import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError
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
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.write('The user entered',fruit_choice)
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      #output it the screen as table 
      streamlit.dataframe(fruityvice_normalized)
except URLError as e:
streamlit.error()
streamlit.stop()
#import snowfalke.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding',add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.FRUIT_LOAD_LIST VALUES ('from streamlit')")
