from variable import Values
import json
import re
class Attribution(Values):
    def __init__(self, database, schema, table):
        self.database = database.split(',')
        self.schema = schema
        self.table_name = table

        self.database_dict = {
            "SCHEMA": self.schema,
            "TABLE": [{self.table_name: {}}]}

        self.STR = {"STR": []}
        self.BOOLEAN = {"BOOLEAN": []}

    def get_attribution(self):
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

        with open('test.json', 'w') as filejson:
            json.dump(self.database_dict, filejson, indent=4)
