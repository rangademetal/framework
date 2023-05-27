from Database.variable import Values
from datetime import datetime
import json
import re


class Attribution(Values):
    def __init__(self, database, schema, table, path):
        self.database = database.split(',')

        self.schema = schema
        self.table_name = table

        self.database_dict = {
            "CREATE_TIME": str(datetime.now()),
            "SCHEMA": self.schema,
            "TABLE": [{self.table_name: {}}],
            "PFK_LINK": [],
            "VALUE": []
        }

        self.STR = {"STR": []}
        self.BOOLEAN = {"BOOLEAN": []}
        self.INTEGER = {"INTEGER": []}
        self.DATE = {"DATE": []}
        self.DATETIME = {"DATETIME": []}
        self.FLOAT = {"FLOAT": []}

    def get_attribution(self, Schema):
        for attribute in self.database:
            attribute = attribute.strip()

            if Values.__PRIMARYKEY__ in attribute:
                PRIMARY_KEY = {
                    "PRIMARY_KEY": {
                        "column_name": attribute.split(' ')[0],
                        "type": "uuid",
                        "unique": True,
                    }
                }
                if Values.__AUTOINCREMENT__ in attribute:
                    PRIMARY_KEY["PRIMARY_KEY"].update({"auto_increment": True})
                self.database_dict["TABLE"][0][self.table_name].update(PRIMARY_KEY)

            if Values.__STR__ in attribute:
                STR_LIST = {
                    "column_name": attribute.split(' ')[0],
                    'length': re.subn(r'\D', '', attribute)[0],
                    'not_null': False,
                    'unique': False,
                    'type': 'str'
                }

                if Values.__NOTNULL__ in attribute:
                    STR_LIST.update({'not_null': True})

                if Values.__UNIQUE__ in attribute:
                    STR_LIST.update({'unique': True})

                self.STR['STR'].append(STR_LIST)
                self.database_dict['TABLE'][0][self.table_name].update(self.STR)

            if Values.__BOOLEAN__ in attribute:
                BOOLEAN_LIST = {
                    "column_name": attribute.split(' ')[0],
                    "type": 'boolean'
                }

                if 'default=true' in attribute:
                    BOOLEAN_LIST.update({'default': True})
                elif 'default=false' in attribute:
                    BOOLEAN_LIST.update({'default': False})

                self.BOOLEAN['BOOLEAN'].append(BOOLEAN_LIST)
                self.database_dict['TABLE'][0][self.table_name].update(self.BOOLEAN)

            if Values.__INTEGER__ in attribute:
                INTEGER_LIST = {
                    "column_name": attribute.split(' ')[0],
                    'length': re.subn(r'\D', '', attribute)[0],
                    'not_null': False,
                    'type': 'integer'
                }

                if Values.__NOTNULL__ in attribute:
                    INTEGER_LIST.update({'not_null': True})

                self.INTEGER['INTEGER'].append(INTEGER_LIST)
                self.database_dict['TABLE'][0][self.table_name].update(self.INTEGER)

            if Values.__DATE__ in attribute:
                if "DATE" == attribute.split(' ')[1]:
                    DATE_LIST = {
                        "column_name": attribute.split(' ')[0],
                        'not_null': False,
                        'type': 'date'
                    }

                    if Values.__NOTNULL__ in attribute:
                        DATE_LIST.update({'not_null': True})

                    self.DATE['DATE'].append(DATE_LIST)
                    self.database_dict['TABLE'][0][self.table_name].update(self.DATE)

            if Values.__DATETIME__ in attribute:
                DATETIME_LIST = {
                    "column_name": attribute.split(' ')[0],
                    'not_null': False,
                    'type': 'datetime'
                }

                if Values.__NOTNULL__ in attribute:
                    DATETIME_LIST.update({"not_null": True})

                self.DATETIME['DATETIME'].append(DATETIME_LIST)
                self.database_dict['TABLE'][0][self.table_name].update(self.DATETIME)

            if Values.__FLOAT__ in attribute:
                FLOAT_LIST = {
                    "colunm_name": attribute.split(' ')[0],
                    'not_null': False,
                    'type': 'float'
                }

                if Values.__NOTNULL__ in attribute:
                    FLOAT_LIST.update({"not_null": True})

                self.FLOAT['FLOAT'].append(FLOAT_LIST)
                self.database_dict['TABLE'][0][self.table_name].update(self.FLOAT)

        with open(f'{Schema}.json', 'w') as filejson:
            json.dump(self.database_dict, filejson, indent=4)

    def get_values(self, insert):
        insert = insert.split(' ')[2]


