import base64

import pandas
import streamlit as st
from functions import add_row
from datetime import date
import pandas as pd

myPath = 'ourCosts.xlsx'
header = ['Date', 'Commodity/Service', 'Group', 'Price']
add_row(myPath, header)

options = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment', 'Transportation']
selected_date = st.date_input("Date:", date.today())
com_ser_text = st.text_input(label="Commodity/Service:")
selected_group = st.selectbox("Group:", options)
price = st.text_input(label='Price:')
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


    # Call the function to show the download button
    download_excel()
