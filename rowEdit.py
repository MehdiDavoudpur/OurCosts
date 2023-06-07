import openpyxl

path = 'myCosts.xlsx'


def add_row(costList):
    myWorkbook = openpyxl.Workbook()
    worksheet = myWorkbook.active

    worksheet.append(costList)
    myWorkbook.save(path)
