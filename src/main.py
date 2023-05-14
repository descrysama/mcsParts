from login import login;
from webinit_ import initBrowser;
from url_fournisseurs.utopya import utopya_urls;
import time;

driver = login(initBrowser(False));
driver.get(utopya_urls[0])
