import requests


class BaseClient:
    # URL vk api
    BASE_URL = "https://api.vk.com/method/"

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL + self.method + "." + self.http_method, params=self.get_params())

        return self.response_handler(response)

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )
