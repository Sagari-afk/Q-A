from random import shuffle


class Replacer:

    def __init__(self, raw_data) -> None:
        self.raw_data = raw_data

    def replace_special_symbols(self) -> list:
        # iterates over each dictionary in raw_data, and for each key-value pair,
        # it checks if the value is a string. If it is, it replaces certain special
        # symbols with apostrophes. If the value is not a string, it assumes it is
        # a list of strings and replaces the special symbols in each string in the list.
        # The modified dictionary is then added to a list called data.
        data = []
        for dict_obj in self.raw_data:
            for key, value in dict_obj.items():
                if type(value) is str:
                    dict_obj[key] = value.replace("&quot;", "'").replace("&#039;", "'")
                    continue
                dict_obj[key] = [string.replace("&quot;", "'").replace("&#039;", "'") for string in value]
            data.append(dict_obj)
        return self.create_all_answers_list(data)

    @staticmethod
    def create_all_answers_list(res_data):
        # takes in a list of dictionaries called res_data and modifies each dictionary
        # in the list to include a new key called "all_answers". The value of this key
        # is a list that contains all the incorrect answers from the original dictionary,
        # plus the correct answer. The list is then shuffled randomly using the shuffle
        # function from the random module.
        for i in range(len(res_data)):
            res_data[i]["all_answers"] = res_data[i]["incorrect_answers"].copy()
            res_data[i]["all_answers"].append(res_data[i]["correct_answer"])
            shuffle(res_data[i]["all_answers"])
        return res_data
