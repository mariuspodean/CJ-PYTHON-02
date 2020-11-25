import openpyxl, pprint

#Opening workbook

wb = openpyxl.load_workbook('october_database.xlsx')
sheet = wb.get_sheet_by_name('october_database')
october_database_data = {}

for row in range (2,sheet.get_highest_row() +1 ):

# bla ahah
