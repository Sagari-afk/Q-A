import ast

import requests


class MakeApiCall:
    """
    This is a class named MakeApiCall which is used to make API calls to get data from a web service
    """

    # Constructor for the class which receives a dictionary of parameters
    def __init__(self, params: dict):
        self.params = params

    # Method to make an API call and get data as response
    def get_data(self, api):
        # Sends a get request to the given API with the given parameters
        response = requests.get(api, params=self.params)

        # If the response code is 200, the response text is evaluated and
        # the "results" part is returned as a list of dictionaries
        if response.status_code == 200:
            res = ast.literal_eval(response.text)["results"]
            return res
        # If the response code is not 200, a message with the response code is printed to the console
        else:
            print(f"Hello person, there's a {response.status_code} error with your request\n")
