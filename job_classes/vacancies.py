class Vacancy:
    """Класс для вакансий"""
    def __init__(self, info) -> None:
        self.__name = info["name"]
        self.__url = info["url"]
        self.__employer = info["employer"]
        self.__town = info["town"]
        self.__responsibility = info["responsibility"]
        self.__requirement = info["requirement"]
        self.__salary_from = info["salary_from"]
        self.__salary_to = info["salart_to"]

    @property
    def name(self) -> str:
        """Вывод значения __name"""
        return self.__name

    @property
    def url(self) -> str:
        """Вывод значения url"""
        return self.__url

    @property
    def employer(self) -> str:
        """Вывод значения employer"""
        return self.__employer

    @property
    def town(self) -> str:
        """Вывод значения town"""
        return self.__town

    @property
    def responsibility(self) -> str:
        """Вывод значения responsibility"""
        return self.__responsibility

    @property
    def requirement(self) -> str:
        """Вывод значения requirement"""
        return self.__requirement

    @property
    def salary_from(self) -> str:
        """Вывод значения salary_from"""
        return self.__salary_from

    @property
    def salary_toe(self) -> str:
        """Вывод значения salary_to"""
        return self.__salary_to

    def __str__(self) -> str:
        return f"""Название: {self.__name}\nСсылка: {self.__url}\nГород: {self.__town}\nКомпания: {self.__employer}\n
        Описание: {self.__responsibility}\nТребования: {self.__requirement}\n
        ЗП от: {self.__salary_from}\nЗП до: {self.__salary_to}"""

    def __lt__(self, other: any) -> int:
        return int(self.__salary_to) < int(other.__salary_to)

    def __le__(self, other: any) -> int:
        return int(self.__salary_to) <= int(other.__salary_to)


class HHVacancy(Vacancy):
    """Класс для вакансий с hh.ru"""
    def __str__(self):
        return f'Информация с сайта hh.ru:\n{super().__str__()}'


class SJVacancy(Vacancy):
    """Класс для вакансий с superjob.ru"""
    def __str__(self):
        return f'Информация с сайта superjob.ru:\n{super().__str__()}'
