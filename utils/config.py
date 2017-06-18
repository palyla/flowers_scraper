import configparser


class Singletone:
    def __singletone__(self, *args, **kwargs):
        return self

    def __raised_call__(self, *args, **kwargs):
        raise RuntimeError


class Configuration(configparser.ConfigParser, Singletone):
    def __init__(self, path='conf/config.ini', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read(path)
        self.__call__ = self.__singletone__
        self.__init__ = self.__raised_call__
