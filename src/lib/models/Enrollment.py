from src.lib.db.interface import TableReadable, TableWritable
from src.lib.models import Class, Student


class Enrollment(TableReadable, TableWritable):
    id: int
    student: Student
    klass: Class

    def __init__():
        pass # TODO

    # TODO: Implement interfaces here
