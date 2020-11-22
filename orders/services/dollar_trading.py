import requests


class DollarTradingService(object):

    def __init__(self):
        URL_BASE = "https://www.dolarsi.com"
        self.url = f"{URL_BASE}/api/api.php?type=valoresprincipales"

    def get(self):
        response = requests.get(self.url)
        if response.ok:
            response = response.json()
            return self._parse_dollar_trading(response)
        return 0

    @staticmethod
    def _parse_dollar_trading(data):
        return sum([
            float(info.get("casa").get("venta").replace(',', '.'))
            for info in data if info.get("casa").get("nombre") == "Dolar Blue"
        ])
