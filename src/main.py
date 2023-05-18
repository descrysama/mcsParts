from login import login;
from webinit_ import initBrowser;
from url_fournisseurs.utopya import utopya_urls;
from single_links.utopya_single import utopya_single;
from last_line import retrieve_last_line, define_last_line, last_run_crash_check, define_last_run_crash, create_config_file;
import os;
import json;
import configparser;
import openpyxl;
from config_db import getUtopyaLinks
from dotenv import load_dotenv
load_dotenv()

result = getUtopyaLinks()

driver = login(initBrowser(True))
all_items = []
csv_file = []
file_path = os.getenv("OUTPUT_PATH")
file_config = os.getenv("CONFIG_PATH")
file_exists = os.path.isfile(file_path)

if os.path.isfile(file_config) :
    create_config_file()

    if file_exists:
        config = configparser.ConfigParser()
        config.read(file_config)

        if config.has_section('CRASH'):
            if not last_run_crash_check():
                workbook = openpyxl.load_workbook(file_path)
                worksheet = workbook.active
                worksheet.delete_rows(1, worksheet.max_row)
                workbook.save(file_path) 
    

try: 
    for i, link in enumerate(result[retrieve_last_line():], start=retrieve_last_line()):
        print(json.dumps({'UTOPYA': (str(i+1) + " / " + str(len(result)))}))
        define_last_line(i)
        utopya_single(driver, result[0][0])
    define_last_line(0)
    define_last_run_crash(False)
except (KeyboardInterrupt, Exception) as e:

    if isinstance(e, KeyboardInterrupt):
        define_last_run_crash(True)

    if isinstance(e, Exception):
        define_last_run_crash(True)

    print('script terminated. An error has occured.')
    print(e)