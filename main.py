import streamlit as st
from datetime import date
import sqlite3

myPath = 'ourCosts.xlsx'
header = ['Date', 'Commodity/Service', 'Group', 'Price']
options = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment & Welfare', 'Transportation']

title_bar = st.title('Our Costs'.title())
title_bar2 = st.header('Registration and management of expenses'.title())

selected_date = st.date_input("Date:", date.today(), key='date')
com_ser = st.text_input(label="Commodity/Service:", key='com/ser')
selected_group = st.selectbox("Group:", options, key='group')
price = st.text_input(label='Price:', key='price')

add = st.button(label='Add', key='Add')
show = st.button(label='Show', key='show')

# selected_row = st.number_input("Enter the ID of the row you want to edit or delete:", min_value=1, value=1)
#
# edit = st.button(label='edit', key='edit')
#
# n_date = st.date_input("New Date:", date.today(), key='n_date')
# n_com_ser = st.text_input(label="Commodity/Service:", key='n_com/ser')
# n_group = st.selectbox("New Group:", options, key='n_group')
# n_price = st.text_input(label='New Price:', key='n_price')
#
# delete = st.button(label='delete', key='delete')
#
row = [(com_ser, selected_group, price, selected_date)]


def new_record(a_row):
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO our_costs VALUES(?, ?, ?, ?)", a_row)
    connection.commit()
    connection.close()


def view_data():
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM our_costs')
    data = cursor.fetchall()
    connection.close()

    return data


def edit_data(row_id, new_com_ser, new_group, new_price, new_date):
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE our_costs SET com/ser=?, group=?, price=? date=? WHERE id=?',
                   (new_com_ser, new_group, new_price, new_date, row_id))
    connection.commit()
    connection.close()


def delete_data(row_id):
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM our_costs WHERE id=?', row_id)
    connection.commit()

    connection.close()


if add:
    new_record(row)
    st.success("Cost Added successfully!")


if show:
    datas = view_data()
    st.write("Data from the database:")
    st.table(datas)

# if edit:
#     edit_data(selected_row, n_com_ser, n_group, n_price, n_date)
#     st.success("Row edited successfully!")
#
# if delete:
#     delete_data(selected_row)
#     st.success("Row deleted successfully!")
