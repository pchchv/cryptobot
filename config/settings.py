import os
import sys
import logging
import logging.config
from config.base_logging import BASE_LOGGING


__CMC_PRO_API_KEY = os.environ.get("CMC_PRO_API_KEY")
__TOKEN = os.environ.get("TOKEN")
APP_NAME = os.environ.get("APP_NAME")

logging.config.dictConfig(BASE_LOGGING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


HEADERS = {
    "accept": "*/*",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/88.0.4324.182 Safari/537.36"
    ),
    "Content-Type": "application/json;charset=UTF-8",
    "X-CMC_PRO_API_KEY": __CMC_PRO_API_KEY,
}

COINMARKETCAP_KWARGS = {
    "url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/",
    "headers": HEADERS,
    "timeout": 10,
}

BOT_KWARGS = {
    "APP_NAME": APP_NAME,
    "IS_LOCALHOST": "misc" in sys.modules,
    "URL": f"https://api.telegram.org/bot{__TOKEN}/",
}

CONFIG_KWARGS = {
    "bot": BOT_KWARGS,
    "coinmarketcap": COINMARKETCAP_KWARGS,
}
