
class Schema:
    def __init__(self, schema):
        self.table = None
        self.schema = schema

    def create_schema(self):
        return self.schema

    def create_table(self, table):
        self.table = table
        return self.table

