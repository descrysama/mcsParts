from login import login;
from webinit_ import initBrowser;
from url_fournisseurs.utopya import utopya_urls;
from single_links.utopya_single import utopya_single;


driver = login(initBrowser(True))
all_items = []
csv_file = []

try: 
    for i, link in enumerate(utopya_urls) :
        print("URL : ", i, " / ", len(utopya_urls) )
        utopya_single(driver, link)
except:
    print('script terminated. An error has occured.')