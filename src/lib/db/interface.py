import abc

class TableReadable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    @staticmethod
    def get_query(id: str) -> str:
        pass

class TableWritable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def insert_query(self) -> str:
        pass


class Database(object):
    @staticmethod
    def get(obj: TableReadable, id: str):
        # TODO: implement database connection
        return obj.get_query(id)

    @staticmethod
    def insert(obj: TableWritable):
        # TODO: implement database connection
        return obj.insert_query()
