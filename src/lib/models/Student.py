from src.lib.db.interface import TableReadable, TableWritable


class Student(TableReadable, TableWritable):
    id: int
    name: str
    age: int

    def __init__():
        pass # TODO

    # TODO: Implement interfaces here
