import openpyxl

path = 'costs.xlsx'
print(path)


def add_row(costList):
    workbook = openpyxl.load_workbook(path)
    worksheet = workbook['Sheet1']

    worksheet.append(costList)
    workbook.save(path)
