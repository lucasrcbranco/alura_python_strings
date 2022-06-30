import re
import requests


class URLExtractor:
    def __init__(self, url: str):
        self.url: str = url
        self._base_url: str = None
        self._params: str = None
        self._url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/exchange")
        self._url: str = self._prepare_url(url)
        self._validate_url()
        self._extract_query_params_from_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

    @property
    def params(self):
        return self._params

    @property
    def base_url(self):
        return self._base_url

    @staticmethod
    def _prepare_url(url: str):
        if type(url) == str:
            return url.strip().lower()
        else:
            return ""

    def _validate_url(self):
        if not self._url_pattern.match(self._url):
            raise ValueError("URL Inválida!")

    def _extract_query_params_from_url(self):
        url_separator_index: int = self._url.find("?")
        url_params: str = self._url[url_separator_index + 1:]
        self._params = url_params
        self._base_url = self._url[:url_separator_index]

    def get_value_from_keyword(self, keyword: str):
        search_param_index: int = self._params.find(keyword.strip().lower())
        value_index: int = search_param_index + len(keyword.strip().lower()) + 1
        ampersand_index: int = self._params.find('&', value_index)

        if ampersand_index == -1:
            extracted_value: str = self._params[value_index:]
        else:
            extracted_value: str = self._params[value_index:ampersand_index]
        return extracted_value

    def exchange(self):
        if re.search(re.compile("(amount)"), self.url):
            request_value = requests.get(f"https://economia.awesomeapi.com.br/json/{self.get_value_from_keyword('from')}")
            if int(request_value.status_code) == 200:
                from_value = "{:.2f}".format(float(request_value.json()[0]['high']))
                to_value = self.get_value_from_keyword("amount")
                return f"Convertendo de {self.get_value_from_keyword('from')} para {self.get_value_from_keyword('to')} e o resultado é: " + "{:.2f}".format(float(to_value) / float(from_value))
            else:
                return "Ocorreu um erro ao realizar a sua conversão. Tente novamente mais tarde!"

url: str = "https://bytebank.com/exchange?from=usd&to=brl&amount=100"
url_extractor = URLExtractor(url)

print(url_extractor.exchange())
