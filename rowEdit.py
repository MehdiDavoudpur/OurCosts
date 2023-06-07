import openpyxl

path = 'myCosts.xlsx'


def add_row(costList):
    myWorkbook = openpyxl.Workbook()
    worksheet = myWorkbook['Sheet1']

    worksheet.append(costList)
    myWorkbook.save(path)
