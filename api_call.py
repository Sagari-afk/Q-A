import ast

import requests


class MakeApiCall:

    def __init__(self, params: dict):
        self.params = params

    def get_data(self, api):
        response = requests.get(api, params=self.params)
        if response.status_code == 200:
            res = ast.literal_eval(response.text)["results"]
            return res
        else:
            print(f"Hello person, there's a {response.status_code} error with your request\n")