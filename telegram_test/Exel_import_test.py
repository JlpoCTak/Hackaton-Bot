from openpyxl import load_workbook

book = load_workbook(filename="C:/Users/Sokol/Documents/GitHub/Hackaton-Bot/data_read/Schedule.xlsx")

sheet = book['Sheet1']

for i in range(1,20):
    print(sheet['A' + str(i)].value, sheet['B' + str(i)].value, sheet['C' + str(i)].value)
