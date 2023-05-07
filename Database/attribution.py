from variable import Values
import json

class Attribution(Values):
    def __init__(self, database, schema, table):
        self.database = database.split(',')
        self.schema = schema
        self.table_name = table

        self.database_dict = {
            "SCHEMA": self.schema,
            "TABLE": [{self.table_name: {}}]}

        self.STR = {"STR":[]}


    # def
    def get_attribution(self):

        for attribute in self.database:
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
                print(self.database_dict["TABLE"][0][self.table_name].update(PRIMARY_KEY))

            if Values.__STR__ in attribute:
                attribute = attribute.strip()
                self.STR['STR'].append({
                            "column_name": attribute.split(' ')[0],
                            'length': '30',
                            'not_null': True,
                            'unique': True,
                            'type': 'str'
                        })

                self.database_dict['TABLE'][0][self.table_name].update(self.STR)

                # if Values.__NOTNULL__ in attribute:
        with open('test.json', 'w') as filejson:
            json.dump(self.database_dict, filejson, indent=4)

