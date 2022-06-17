class User:
    def __init__(self, id, height, name, deleted, created):
        self.__id = id
        self.__name = name
        self.__height = height
        self.__deleted = deleted
        self.__created = created

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            """проверка """
            assert name[0].isdigit() == False
            assert name.isspace() == False
            self.__name = name
        except:
            print('Некорректно введенное имя')

    @name.deleter
    def name(self):
        print('Удаление имени')
        self.__name = None
