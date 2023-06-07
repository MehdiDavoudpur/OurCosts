import streamlit as st
import pandas as pd

from rowEdit import add_row

from datetime import date
options = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment', 'Transportation']
selected_date = st.date_input("Date:", date.today())
com_ser_text = st.text_input(label="Commodity/Service:")
selected_group = st.selectbox("Group:", options)
price = st.text_input(label='Price:')
add = st.button(label='Add', key='Add')

mylist = [selected_date, com_ser_text, selected_group, price]


# Create a dataframe with some data
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Write the dataframe to an Excel file
df.to_excel('newCosts.xlsx', index=False)


if add:
    add_row(mylist)
