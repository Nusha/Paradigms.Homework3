# Итератор (Iterator): Это интерфейс, который определяет методы для обхода коллекции: has_next()
# (есть ли следующий элемент) и next() (получить следующий элемент).
# Пример с CD changer
from abc import abstractmethod, ABC


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class CdChangerIterator(Iterator, ABC):

    def __init__(self, cd_changer):
        self.cd_changer = cd_changer
        self.index = 0

    def has_next(self):
        return self.index < len(self.cd_changer.cds)

    def next(self):
        cd = self.cd_changer.cds[self.index]
        self.index += 1
        return cd


class CdChanger:
    def __init__(self):
        self.cds = []

    def add_cd(self, cd):
        self.cds.append(cd)

    def iterator(self):
        return CdChangerIterator(self)


cd_changer = CdChanger()
for i in range(11):
    cd_changer.add_cd("Диск " + str(i))

iterator = cd_changer.iterator()
while iterator.has_next():
    print(iterator.next())
