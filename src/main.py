from login import login;
from webinit_ import initBrowser;
from url_fournisseurs.utopya import utopya_urls;
from single_links.utopya_single import utopya_single;
import os

driver = login(initBrowser(True))
all_items = []
csv_file = []

file_path = '/var/www/html/output.xlsx'
file_exists = os.path.isfile(file_path)
if file_exists:
    os.remove(file_exists)

try: 
    for i, link in enumerate(utopya_urls) :
        print("URL : ", i, " / ", len(utopya_urls) )
        utopya_single(driver, link)
except:
    print('script terminated. An error has occured.')