import plotly.express as px
import streamlit as st
from datetime import date
import sqlite3

myPath = 'ourCosts.xlsx'
header = ['Date', 'Commodity/Service', 'Category', 'Price']
options = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment & Welfare', 'Transportation']

title_bar = st.title('Our Costs'.title())
title_bar2 = st.header('Registration and management of expenses'.title())

selected_date = st.date_input("Date:", date.today(), key='date')
com_ser = st.text_input(label="Commodity/Service:", key='com/ser')
selected_category = st.selectbox("Category:", options, key='category')
price = st.text_input(label='Price:', key='price')

add = st.button(label='Add', key='Add')
show_all = st.button(label='Show All', key='a_show')
show_prices = st.button(label='Show Prices', key='p_show')
show_dates = st.button(label='Show Dates', key='d_show')
show_com_ser = st.button(label='Show Com/Ser', key='cs_show')
show_category = st.button(label='Show categories', key='g_show')
show_chart = st.button(label='Show Chart', key='c_show')

# selected_row = st.number_input("Enter the ID of the row you want to edit or delete:", min_value=1, value=1)
#
# edit = st.button(label='edit', key='edit')
#
# n_date = st.date_input("New Date:", date.today(), key='n_date')
# n_com_ser = st.text_input(label="Commodity/Service:", key='n_com/ser')
# n_category = st.selectbox("New Category:", options, key='n_category')
# n_price = st.text_input(label='New Price:', key='n_price')
#
# delete = st.button(label='delete', key='delete')
#
row = [(com_ser, selected_category, price, selected_date)]


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


def collect_price_s():
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()
    cursor.execute('SELECT price FROM our_costs')
    price_s = cursor.fetchall()
    connection.close()

    return price_s


def collect_date_s():
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()
    cursor.execute('SELECT date FROM our_costs')
    date_s = cursor.fetchall()
    connection.close()

    return date_s


def collect_com_ser_s():
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()
    cursor.execute('SELECT com_ser FROM our_costs')
    com_ser_s = cursor.fetchall()
    connection.close()

    return com_ser_s


def collect_category_s():
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()
    cursor.execute('SELECT category FROM our_costs')
    category_s = cursor.fetchall()
    connection.close()

    return category_s


def edit_data(row_id, new_com_ser, new_category, new_price, new_date):
    connection = sqlite3.connect('costs.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE our_costs SET com/ser=?, category=?, price=? date=? WHERE id=?',
                   (new_com_ser, new_category, new_price, new_date, row_id))
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

if show_all:
    all_data = view_data()
    st.write("Data from the database:")
    st.table(all_data)

if show_prices:
    prices = collect_price_s()
    price_list = []
    for i in range(len(prices)):
        price_list.append(prices[i][0])
    st.table(price_list)

if show_dates:
    dates = collect_date_s()
    dates_list = []
    for i in range(len(dates)):
        dates_list.append(dates[i][0])

    st.table(dates_list)


if show_com_ser:
    com_sers = collect_com_ser_s()
    com_sers_list = []
    for i in range(len(com_sers)):
        com_sers_list.append(com_sers[i][0])

    st.table(com_sers_list)


if show_category:
    categories = collect_category_s()
    categories_list = []
    for i in range(len(categories)):
        categories_list.append(categories[i][0])
        print(categories[i][0])

    print(categories_list)
    st.table(categories_list)


if show_chart:

    prices = collect_price_s()
    price_list = []
    for i in range(len(prices)):
        price_list.append(prices[i][0])

    dates = collect_date_s()
    dates_list = []
    for i in range(len(dates)):
        dates_list.append(dates[i][0])

    x = dates_list
    y = price_list

    figure = px.scatter(x=x, y=y, labels={'x': 'date', 'y': 'price'})
    st.plotly_chart(figure)

# if edit:
#     edit_data(selected_row, n_com_ser, n_category, n_price, n_date)
#     st.success("Row edited successfully!")
#
# if delete:
#     delete_data(selected_row)
#     st.success("Row deleted successfully!")
