import re


class urlValidator:
    def __init__(self, url: str):
        self._url = url
        self._url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")


