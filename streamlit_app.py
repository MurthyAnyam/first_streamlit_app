import streamlit
streamlit.title('My parents health new diner')
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥑🍞Egg')
streamlit.text('🥑🍞hasbrown')
streamlit.text('🥣 🥗 Bread')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
