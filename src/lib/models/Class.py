from src.lib.db.interface import TableReadable, TableWritable


class Class(TableReadable, TableWritable):
    id: int
    name: str
    time: int #[0,24)
    days_of_week: int #8 bit flag

    def __init__():
        pass # TODO

    # TODO: Implement interfaces here
