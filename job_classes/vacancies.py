class Vacancy:
    """ Основной класс для вакансий """
    __slots__ = ["__name", "__url", "__responsibility", "__town", "__employer",
                 "__requirement", "__salary_from", "__salary_to"]

    def __init__(self, args) -> None:
        self.__name = args["name"]
        self.__url = args["url"]
        self.__responsibility = args["responsibility"]
        self.__town = args["town"]
        self.__employer = args["employer"]
        self.__requirement = args["requirement"]
        self.__salary_from = args["salary_from"]
        self.__salary_to = args["salary_to"]

    @property
    def name(self) -> str:
        return self.__name

    @property
    def url(self) -> str:
        return self.__url

    @property
    def requirement(self) -> str:
        return self.__requirement

    @property
    def town(self) -> str:
        return self.__town

    @property
    def employer(self) -> str:
        return self.__employer

    @property
    def responsibility(self) -> str:
        return self.__responsibility

    @property
    def salary_to(self) -> str:
        return self.__salary_to

    @property
    def salary_from(self) -> str:
        return self.__salary_from

    def __str__(self) -> str:
        return f'Наименование: {self.__name}\nСсылка: {self.__url}\nОписание: {self.__responsibility}\n'\
               f'Город: {self.__town}\nКомпания: {self.__employer}\nТребования: {self.__requirement}\n'\
               f'ЗП от: {self.__salary_from}\nЗП до: {self.__salary_to}'

    def __lt__(self, other: any) -> int:
        return int(self.salary_to) < int(other.salary_to)

    def __le__(self, other: any) -> int:
        return int(self.salary_to) <= int(other.salary_to)


class HHVacancy(Vacancy):
    """ Класс для HEAD HUNTER """
    def __str__(self) -> str:
        return f"Данные с HeadHunter\n{super().__str__()}\n"


class SJVacancy(Vacancy):  # add counter mixin
    """ Класс для SUPER JOB """
    def __str__(self) -> str:
        return f"Данные с SuperJob\n{super().__str__()}\n"
