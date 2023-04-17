import requests
from site_classes.abc_class import Engine
from src.text_changing import text_change


class HeadHunter(Engine):
    """Класс сайта hh.ru"""
    def __init__(self) -> None:
        self.__vacancies = []
        self.__api = 'https://api.hh.ru/'

    @property
    def vacancies(self):
        """Вывод вакансий"""
        return self.__vacancies

    def get_request(self, vacancy: str) -> None or str:
        """
        Запрос к hh.ru
        """
        print("hh.ru")

        page_number = 0
        last_page = 5

        while page_number < last_page:

            response = requests.get(self.__api, params={'text': vacancy,
                                                    'per_page': 100,
                                                    'page': page_number})

            if response != 200:
                return "Ошибка:", response.status_code

            else:
                vacancies = response.json()["items"]

                for vacancy in vacancies:

                    if vacancy["salary"] is not None:
                        salary_from = vacancy["salary"]["from"]
                        if salary_from is None:
                            salary_from = 0
                        salary_to = vacancy["salary"]["to"]
                        if salary_to is None:
                            salary_to = 0
                    else:
                        salary_from = 0
                        salary_to = 0

                    self.__vacancies.append({"name": text_change((vacancy["name"])),
                                             "url": text_change((vacancy["url"])),
                                             "responsibility": text_change(vacancy["snippet"]["responsibility"]),
                                             "town": text_change((vacancy["area"]["name"])),
                                             "employer": text_change((vacancy["employer"]["name"])),
                                             "requirement": text_change(vacancy["snippet"]["requirement"]),
                                             "salary_from": text_change((str(salary_from))),
                                             "salary_to": text_change((str(salary_to))),
                                             })

            page_number += 1


class SuperJob(Engine):
    """Класс сайта superjob.ru"""
    def __init__(self):
        self.__vacancies = []
        self.__api = "v3.r.137494512.c0bfbe9460bf69a9f1737c09e672ee1300ef0865.e3c764694d2428df6ccc1719788c0cc1f7cad2d8"

    @property
    def vacancies(self):
        return self.__vacancies

    def get_request(self, vacancy: str) -> None or str:
        """Запрос к superjob.ru
        """
        print('superjob.ru')

        superjob_url = "https://api.superjob.ru/:2.0/vacancies"
        page_number = 0
        last_page = 5

        while page_number < last_page:

            response = requests.get(superjob_url,headers={'X-Api-App-Id': self.__api}, params={'text': vacancy,
                                                        'per_page': 100,
                                                        'page': page_number})

            if response != 200:
                return "Ошибка:", response.status_code

            else:
                vacancies = response.json()["objects"]

                for vacancy in vacancies:

                    self.__vacancies.append({"name": text_change((vacancy["profession"])),
                                             "url": text_change((vacancy["link"])),
                                             "responsibility": text_change(vacancy["candidat"]),
                                             "town": text_change((vacancy["town"]["title"])),
                                             "employer": text_change((vacancy["firm_name"])),
                                             "requirement": text_change(vacancy["work"]),
                                             "salary_from": text_change(vacancy["payment_from"]),
                                             "salary_to": text_change(vacancy["payment_to"]),
                                             })

                    page_number += 1
