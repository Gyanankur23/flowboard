class SemanticModel:
    def __init__(self):
        self.tables = {}  # table_name: {'dimensions': list, 'measures': dict}
        self.relationships = []  # list of tuples (table1, col1, table2, col2)

    def add_table(self, table_name, dimensions, measures):
        self.tables[table_name] = {
            'dimensions': dimensions,
            'measures': measures
        }

    def add_relationship(self, table1, col1, table2, col2):
        self.relationships.append((table1, col1, table2, col2))