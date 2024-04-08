from datetime import date
from pony.orm import *


from itertools import count
from typing import Any
from datetime import datetime

from bookkeeper.repository.abstract_repository import AbstractRepository, T

##db = Database()
##
##
##class Doctor(db.Entity):
##    id = PrimaryKey(int, auto=True)
##    last_name = Required(str)
##    first_name = Required(str)
##    patronymic = Optional(str)
##    fee_per_visit = Required(float)
##    visits = Set('Visit')
##
##
##class Visit(db.Entity):
##    id = PrimaryKey(int, auto=True)
##    doctor = Required(Doctor)
##    patient = Required('Patient')
##    weight = Optional(float)
##    height = Optional(float)
##    conclusion = Required(str, default="Патологии не выявлено.")
##
##
##class Patient(db.Entity):
##    id = PrimaryKey(int, auto=True)
##    last_name = Required(str)
##    first_name = Required(str)
##    patronymic = Optional(str)
##    gender = Optional(str, 1)
##    date_of_birth = Required(date)
##    visits = Set(Visit)
##
##
##
##db.bind(provider='sqlite', filename='content/database.sqlite', create_db=True)
##db.generate_mapping(create_tables=True)
##
##patient_data = [
##    {"last_name":"Кулишенко","first_name":"Леонид","patronymic":"Александрович","gender":"M","date_of_birth":"1952-06-25"},
##    {"last_name":"Некрасов","first_name":"Рафаил","patronymic":"Александрович","gender":"M","date_of_birth":"1935-09-29"},
##    {"last_name":"Пономаренко","first_name":"Ян","patronymic":"Александрович","gender":"M","date_of_birth":"1942-02-12"},
##    {"last_name":"Шумейко","first_name":"Шамиль","patronymic":"Александрович","gender":"M","date_of_birth":"1946-04-11"},
##    {"last_name":"Колобова","first_name":"Клементина","patronymic":"Александровна","gender":"F","date_of_birth":"1944-05-03"},
##    {"last_name":"Рыбакова","first_name":"Устинья","patronymic":"Александровна","gender":"F","date_of_birth":"1929-08-17"},
##    {"last_name":"Чикольба","first_name":"Эльмира","patronymic":"Александровна","gender":"F","date_of_birth":"1938-07-07"},
##    {"last_name":"Тимошенко","first_name":"Тарас","patronymic":"Алексеевич","gender":"M","date_of_birth":"1970-03-17"},
##    {"last_name":"Зиновьева","first_name":"Флорентина","patronymic":"Алексеевна","gender":"F","date_of_birth":"1928-08-07"},
##    {"last_name":"Козлова","first_name":"Зинаида","patronymic":"Алексеевна","gender":"F","date_of_birth":"1983-08-31"},
##    {"last_name":"Пономаренко","first_name":"Зинаида","patronymic":"Алексеевна","gender":"F","date_of_birth":"1942-02-12"},
##    {"last_name":"Мельников","first_name":"Йозеф","patronymic":"Анатолиевич","gender":"M","date_of_birth":"1949-02-05"},
##    {"last_name":"Овчаренко","first_name":"Григорий","patronymic":"Анатолиевич","gender":"M","date_of_birth":"1953-11-10"},
##    {"last_name":"Терентьева","first_name":"Нина","patronymic":"Анатолиевна","gender":"F","date_of_birth":"1926-10-19"},
##    {"last_name":"Чикольба","first_name":"Янита","patronymic":"Анатолиевна","gender":"F","date_of_birth":"1938-07-07"},
##    {"last_name":"Коломоец","first_name":"Арсений","patronymic":"Андреевич","gender":"M","date_of_birth":"1944-05-03"},
##    {"last_name":"Рожков","first_name":"Йоханес","patronymic":"Андреевич","gender":"M","date_of_birth":"1936-09-08"},
##    {"last_name":"Шаров","first_name":"Александр","patronymic":"Андреевич","gender":"M","date_of_birth":"1957-02-08"},
##    {"last_name":"Зайцева","first_name":"Глафира","patronymic":"Андреевна","gender":"F","date_of_birth":"1937-11-28"},
##    {"last_name":"Ильина","first_name":"Алёна","patronymic":"Андреевна","gender":"F","date_of_birth":"1952-06-25"}
##];
##
##doctor_data = [
##    {"last_name":"Иванов","first_name":"Иван","patronymic":"Иванович","fee_per_visit":2500.0},
##    {"last_name":"Виноградова","first_name":"Инесса","patronymic":"Валерьевна","fee_per_visit":3500.0},
##    {"last_name":"Горобчук","first_name":"Гертруда","patronymic":"Артёмовна","fee_per_visit":2400.0},
##    {"last_name":"Борисова","first_name":"Ульяна","patronymic":"Львовна","fee_per_visit":2500.0},
##    {"last_name":"Ерёменко","first_name":"Чилита","patronymic":"Сергеевна","fee_per_visit":2700.0},
##    {"last_name":"Медведев","first_name":"Матвей","patronymic":"Григорьевич","fee_per_visit":8000.0},
##    {"last_name":"Соболев","first_name":"Жерар","patronymic":"Вадимович","fee_per_visit":8500.0},
##    {"last_name":"Чикольба","first_name":"Бронислава","patronymic":"Анатолиевна","fee_per_visit":9000.0},
##    {"last_name":"Фокина","first_name":"Устинья","patronymic":"Львовна","fee_per_visit":1500.0},
##    {"last_name":"Фомичёва","first_name":"Жанна","patronymic":"Борисовна","fee_per_visit":4500.0},
##    {"last_name":"Фролова","first_name":"Ольга","patronymic":"Евгеньевна","fee_per_visit":5000.0},
##    {"last_name":"Игнатьев","first_name":"Денис","patronymic":"Богданович","fee_per_visit":3000.0},
##    {"last_name":"Дементьев","first_name":"Цицерон","patronymic":"Романович","fee_per_visit":5000.0},
##    {"last_name":"Дзюба","first_name":"Доминика","patronymic":"Львовна","fee_per_visit":6000.0}
##];
##
##@db_session
##def populate_data(cls, data):
##    if select(p for p in cls).count() > 0:
##        return
##
##    for item in data:
##        cls(**item)
##
##
##populate_data(Patient, patient_data)
##populate_data(Doctor, doctor_data)
##
##@db_session
##def select_show(cls):
##    q = select(d for d in cls)
##    q.show()
##
##select_show(Doctor)

db = Database()



class Catg(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    #parent = Required(Catg)
    #spend = Set('Spend')

class Spend(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(str)
    summ = Required(float)
    catg = Required(str)#Required(Catg)
    comment = Required(str)


db.bind(provider='sqlite', filename='content/database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


class SQLRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий на sql. 
    """

    def __init__(self) -> None:
        pass
        

    @db_session
    def add(self, amount, name, comment) -> int:
        #if getattr(obj, 'pk', None) != 0:
        #    raise ValueError(f'trying to add object {obj} with filled `pk` attribute')
        #pk = next(self._counter)
        #self._container[pk] = obj
        #obj.pk = pk
        t=datetime.now()
        t=str(date.today())+" "+t.strftime("%H:%M:%S")
        sp1 = Spend(date=t, summ=amount,
                     catg=name, comment=comment)
        commit()
        return 0
    
    @db_session
    def add_catg(self,name):
        sp1 = Catg(name=name)
        commit()
        return 0

    @db_session
    def show_spend(self):
        q = select(d for d in Spend)
        q.show()

    @db_session
    def show_catg(self):
        q = select(d for d in Catg)
        q.show()

    @db_session
    def list_spend(self):
        temp=[]
        for i in range(1000):
            gy=get(sp for sp in Spend if sp.id == i)
            try:
                temp.append([gy.date,str(gy.summ), gy.catg, gy.comment])
            except:
                pass
        return temp

    @db_session
    def list_catg(self):
        temp=[]
        for i in range(1000):
            gy=get(sp for sp in Catg if sp.id == i)
            try:
                temp.append(gy.name)
            except:
                pass
        return temp

    @db_session
    def pk_spend(self):
        temp={}
        z=0
        for i in range(1000):
            gy=get(sp for sp in Spend if sp.id == i)
            try:
                temp[str(z)]=gy.id
                z+=1
            except:
                pass
        return temp

    @db_session
    def pk_catg(self):
        temp={}
        z=0
        for i in range(1000):
            gy=get(sp for sp in Catg if sp.id == i)
            try:
                temp[str(z)]=gy.id
                z+=1
            except:
                pass
        return temp

    def get(self, pk: int) -> T | None:
        return self._container.get(pk)

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        if where is None:
            return list(self._container.values())
        return [obj for obj in self._container.values()
                if all(getattr(obj, attr) == value for attr, value in where.items())]

    @db_session
    def update(self, pk, date,summ,catg,comment) -> None:
        Spend[pk].date=date
        Spend[pk].summ=summ
        Spend[pk].catg=catg
        Spend[pk].comment=comment

    @db_session
    def delete(self, pk: int) -> None:
        Spend[pk].delete()

    @db_session
    def delete_ctg(self, pk: int) -> None:
        Catg[pk].delete()
        
































