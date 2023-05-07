from random import shuffle


class Replacer:

    def __init__(self, raw_data) -> None:
        self.raw_data = raw_data

    def replace_special_symbols(self) -> list:
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
        for i in range(len(res_data)):
            res_data[i]["all_answers"] = res_data[i]["incorrect_answers"].copy()
            res_data[i]["all_answers"].append(res_data[i]["correct_answer"])
            shuffle(res_data[i]["all_answers"])
        return res_data
