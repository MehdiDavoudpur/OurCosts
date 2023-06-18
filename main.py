import streamlit as st
from functions import add_row
from datetime import date

myPath = 'ourCosts.xlsx'
header = ['Date', 'Commodity/Service', 'Group', 'Price']
options = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment & Welfare', 'Transportation']

if st.session_state.get('date', None) is None &\
        st.session_state.get('com/ser', None) is None & \
        st.session_state.get('price', None) is None :
    add_row(myPath, header)

title_bar = st.title('Our Costs'.title())
title_bar2 = st.header('Registration and management of expenses'.title())
selected_date = st.date_input("Date:", date.today(), key='date')
com_ser_text = st.text_input(label="Commodity/Service:", key='com/ser')
selected_group = st.selectbox("Group:", options, key='group')
price = st.text_input(label='Price:', key='price')
add = st.button(label='Add', key='Add')
create_dl_lnk = st.button(label='Create Download link', key='c_d_l')

mylist = [selected_date, com_ser_text, selected_group, price]

if add:
    add_row(myPath, mylist)

if create_dl_lnk:
    def download_excel():
        with open('ourCosts.xlsx', 'rb') as f:
            data = f.read()
        st.download_button(label='Download Excel file', data=data, file_name='ourCosts.xlsx',
                           mime='application/vnd.malformations-office document.spreadsheet.sheet')

    download_excel()
