
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_data = [row for row in self.table if condition(row)]
        return Table(self.table_name + "_filtered", filtered_data)

    def aggregate(self, aggregation_function, aggregation_key):
        values = [row[aggregation_key] for row in self.table if aggregation_key in row]
        return aggregation_function(values)

    def __str__(self):
        return f"Table: {self.table_name}, Rows: {len(self.table)}"


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for table in self.table_database:
            if table.table_name == table_name:
                return table
        return None































































































