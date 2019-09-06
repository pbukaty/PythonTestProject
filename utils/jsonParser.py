import json


class JsonParser:

    def parse(self, file_name):
        with open(file_name, 'r') as f:
            params = json.load(f)
        return params
