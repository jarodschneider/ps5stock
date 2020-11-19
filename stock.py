import requests
import logging
import coloredlogs
import os
import time
import sys, getopt


def main(argv):
    try:
        delay = float(argv[0])
    except (IndexError, ValueError):
        raise SystemExit(f"Usage: stock.py <time_between_gets>")
    
    initLog()

    while True:
        disk_raw = requests.get('https://api.direct.playstation.com/commercewebservices/ps-direct-us/users/anonymous/products/productList/?fields=BASIC&productCodes=3005816')

        disk_json = disk_raw.json()

        disk_status = 'nope' if disk_json['products'][0]['stock']['stockLevelStatus'] == 'outOfStock' else '!!STOCK!!'

        digital_raw = requests.get('https://api.direct.playstation.com/commercewebservices/ps-direct-us/users/anonymous/products/productList/?fields=BASIC&productCodes=3005817')

        digital_json = digital_raw.json()

        digital_status = 'nope' if digital_json['products'][0]['stock']['stockLevelStatus'] == 'outOfStock' else '!!STOCK!!'

        logging.info('\nDISK: {}\nDIGITAL: {}\n'.format(disk_status, digital_status))
        time.sleep(delay)


def initLog():
    logging.basicConfig(
        filename='stock.log',
        level=logging.INFO,
        format='%(levelname)s: "%(asctime)s - %(message)s')
    
    LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter('%(levelname)s: "%(asctime)s - %(message)s')
    )

    logging.getLogger().addHandler(stream_handler)
    coloredlogs.install(LOGLEVEL, logger=logging.getLogger())


if __name__ == "__main__":
    main(sys.argv[1:])