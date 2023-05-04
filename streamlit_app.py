import streamlit

streamlit.title('My Parents New Health Diner')

streamlit.header('Breakfast Favourite')

streamlit.text('🥣 Omega 3 & Blueberry OatMeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast ')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
