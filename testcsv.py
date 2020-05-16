
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("student info.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  # First Sheet
  
def getVal(row, col):
	return str(sheet.cell_value(row, col))

def totalRows():
	return sheet.nrows
