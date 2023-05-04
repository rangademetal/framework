from Variable.variable_init import Variables


class Attribution(Variables):
    def __init__(self, database):
        self.database = database
        Variables.__init__()

    if Variables.BOOLEAN in [True, False]:
