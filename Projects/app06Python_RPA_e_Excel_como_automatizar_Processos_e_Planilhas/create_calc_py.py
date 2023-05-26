import xlsxwriter as writer
import os
from os import open


workbook = writer.Workbook('./doc1.xlsx')



sheet_padrao =  workbook.add_worksheet()


sheet_padrao.write("A1", 'Name')
sheet_padrao.write("B1", 'Age')
sheet_padrao.write("A2", 'Amanda')
sheet_padrao.write("B2", 21)
sheet_padrao.write("A3", 'Allan')
sheet_padrao.write("B3", 28)
workbook.close()    













