from variable import Values


class Attribution(Values):
    def __init__(self, database, schema, table):
        self.database = database.split(',')
        self.schema = schema
        self.table_name = table

        self.database_dict = {
            "SCHEMA": "test",
            "TABLE": {
                self.table_name: {

                }
            }
        }

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
                self.database_dict['TABLE'][self.table_name].update(PRIMARY_KEY)

            if Values.__STR__ in attribute:
                attribute = attribute.strip()
                print(attribute)
        print(self.database_dict)

