import streamlit as st
from datetime import date
import sqlite3

myPath = 'ourCosts.xlsx'
header = ['Date', 'Commodity/Service', 'Group', 'Price']
options = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment & Welfare', 'Transportation']

title_bar = st.title('Our Costs'.title())
title_bar2 = st.header('Registration and management of expenses'.title())
selected_date = st.date_input("Date:", date.today(), key='date')
com_ser_text = st.text_input(label="Commodity/Service:", key='com/ser')
selected_group = st.selectbox("Group:", options, key='group')
price = st.text_input(label='Price:', key='price')
add = st.button(label='Add', key='Add')
# create_dl_lnk = st.button(label='Create Download link', key='c_d_l')
show = st.button(label='Show', key='show')

mylist = [selected_date, com_ser_text, selected_group, price]
row = [(com_ser_text, selected_group, price, selected_date)]

connection = sqlite3.connect('costs.db')
cursor = connection.cursor()


def add_row_to_database(a_row):
    cursor.executemany("INSERT INTO our_costs VALUES(?, ?, ?, ?)", a_row)
    connection.commit()


if add:
    add_row_to_database(row)

if show:
    cursor.execute('SELECT * FROM our_costs')
    data = cursor.fetchall()
    connection.close()

    st.write("Data from the database:")
    st.table(data)
