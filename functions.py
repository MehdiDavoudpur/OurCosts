import openpyxl
myWorkbook = openpyxl.Workbook()
worksheet = myWorkbook.active


def add_row(path, list_as_new_row):
    worksheet.append(list_as_new_row)
    myWorkbook.save(path)
