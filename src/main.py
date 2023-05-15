from login import login;
import csv;
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

with open('src/output/utopya.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['SKU', 'PRICE'])
    for row in csv_file:
        writer.writerow(row)
file.close()