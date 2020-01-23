import base_client
from datetime import datetime

debug = True


class ClientGetID(base_client.BaseClient):
    method = "users"
    http_method = "get"
    json_data = None

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return {
            "user_ids": self.username
        }

    def response_handler(self, response):
        self.json_data = response.json()
        return self.json_data["response"][0]["uid"]


def calculate_age(born):
    today = datetime.utcnow()
    return today.year - born.year


class ClientGetFriendsAges(base_client.BaseClient):
    method = "friends"
    http_method = "get"
    json_data = None

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
            "user_id": self.user_id,
            "fields": "bdate"
        }

    def response_handler(self, response):
        self.json_data = response.json()
        ages = list()

        for friend in self.json_data["response"]:
            date_tmp = friend.get("bdate")
            # print (type(date_tmp),date_tmp)

            if date_tmp is None:
                ages.append(1)
                continue
                # print (date_tmp)
                # continue
            try:
                ages.append(calculate_age(datetime.strptime(date_tmp, "%d.%m.%Y")))
            except ValueError:
                ages.append(0)
            ages = sorted(ages)
        return ages
