import os
import json
from datetime import datetime


class OsOperation:
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r') as SETTING_FILE:
            settings = json.load(SETTING_FILE)
            self.path = settings['PATH_DB']['PATH']
            self.schema_path = settings['PATH_DB']['SCHEMA_PATH']

    def get_file(self):
        return os.getcwd()

    def write_schema(self, Schema):
        Schema = f'{Schema}.json'
        os.chdir(self.path)
        if Schema in os.listdir():
            return
        else:
            create = {
                "CREATE_TIME": str(datetime.now()),
                "SCHEMA": Schema.split('.')[0],
                "TABLE": [],
                "PFK_LINK": [],
                "VALUE": []
            }

            with open(Schema, 'w') as file_write:
                json.dump(create, file_write, indent=4)

    def check_schema_path(self, schema):
        print(schema)

