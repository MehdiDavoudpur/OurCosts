import openpyxl

mylist = []
j = 0
workbook = openpyxl.load_workbook('/costs.xlsx')
worksheet = workbook['Sheet1']
print(mylist)
while True:
    myCost = input("enter your price: ")

    if myCost == 'finish':
        j = j + 1
        worksheet.insert_cols(j)

        for index, value in enumerate(mylist):
            worksheet.cell(row=index + 1, column=j, value=value)
        workbook.save('example.xlsx')
        mylist = []

    else:
        mylist.append(myCost)
        print(mylist)
