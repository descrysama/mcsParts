from login import login;
import openpyxl
from webinit_ import initBrowser;
from url_fournisseurs.utopya import utopya_urls;
from single_links.utopya_single import utopya_single;
import os;

driver = login(initBrowser(True))
all_items = []
csv_file = []

for i, link in enumerate(utopya_urls) :
    print("URL : ", i, " / ", len(utopya_urls) )
    all_items.append(utopya_single(driver, link))

for single_phone in all_items :
    for single_item in single_phone :
        csv_file.append(single_item)



workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

# Write the header row to the worksheet
worksheet.cell(row=1, column=1, value='SKU')
worksheet.cell(row=1, column=2, value='PRICE')

# Iterate over the rows in the CSV file and write them to the worksheet
for row_number, row in enumerate(csv_file, start=2):
    worksheet.cell(row=row_number, column=1, value=row[0])
    worksheet.cell(row=row_number, column=2, value=row[1])

# Save the workbook to a file
workbook.save('../../utopya.xlsx')