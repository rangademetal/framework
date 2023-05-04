from variable import Values


class Attribution(Values):
    def __init__(self, database, schema):
        self.database = database.split(',')
        self.schema = schema


    def get_attribution(self):
        print(self.database)
        for attribute in self.database:
            print(attribute)
            if Values.__PRIMARYKEY__ in attribute:
                PRIMARY_KEY = {
                    "PRIMARY_KEY": {
                        "column_name": "id",
                        "type": "uuid",
                        "unique": True,
                    }
                }
                print('found primary key')
                if Values.__AUTOINCREMENT__ in attribute:

                    PRIMARY_KEY["PRIMARY_KEY"].update({"auto_increment": True})

                print(PRIMARY_KEY)








