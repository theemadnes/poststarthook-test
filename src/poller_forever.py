import time
import requests
import logging

# set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

while True:
#for _ in range(0, 5):

    # check google.com
    url = 'https://www.google.com'
    r = requests.get(url)
    if r.ok:
        logging.info(url + ' is OK')
    else:
        logging.warning(url + ' is inaccessible')

    # wait 5 seconds
    time.sleep(5)