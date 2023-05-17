from login import login;
from webinit_ import initBrowser;
from url_fournisseurs.utopya import utopya_urls;
from single_links.utopya_single import utopya_single;
from last_line import retrieve_last_line, define_last_line, last_run_crash_check, define_last_run_crash;
import os;
import configparser;
import openpyxl;

driver = login(initBrowser(True))
all_items = []
csv_file = []

file_path = 'utopya/src/output.xlsx'
file_exists = os.path.isfile(file_path)

if file_exists:
    config = configparser.ConfigParser()
    config.read('config.cfg')

    if config.has_section('CRASH') :
        if last_run_crash_check() == False:
            workbook = openpyxl.load_workbook(file_path)
            worksheet = workbook.active
            worksheet.delete_rows(1, worksheet.max_row)
            workbook.save(file_path)    


try: 
    for i, link in enumerate(utopya_urls[retrieve_last_line():], start=retrieve_last_line()):
        print("URL : ", i, " / ", len(utopya_urls) )
        define_last_line(i)
        utopya_single(driver, link)
    define_last_line(0)
    define_last_run_crash(False)
except (KeyboardInterrupt, Exception) as e:

    if isinstance(e, KeyboardInterrupt):
        define_last_run_crash(True)

    if isinstance(e, Exception):
        define_last_run_crash(True)

    print('script terminated. An error has occured.')
    print(e)