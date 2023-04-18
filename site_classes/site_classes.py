from src.text_changing import format_text
from site_classes.abc_class import Engine
import requests


class HH(Engine):
    """Класс для работы с HEAD HUNTER"""
    __slots__ = ["__vacancies", "__config"]

    def __init__(self) -> None:
        self.__vacancies = []
        self.__config = [{"last request": "Последний запрос был к HEAD HUNTER"}]

    @property
    def vacancies(self) -> list:
        return self.__vacancies

    @property
    def config(self) -> list:
        return self.__config

    def get_request(self, keywords: str) -> None or str:
        """
        Запрос к ресурсу
        :param keywords: название вакансии для поиска
        :return: список с данными или None
        """
        print("Делаем запрос с HEAD HUNTER")
        url_head_hunter = "https://api.hh.ru/vacancies"
        page_number = 0
        # количество страниц обработки
        all_pages = 5

        while page_number < all_pages:

            params = {
                "text": keywords,
                "per_page": 100,
                "page": page_number,
                        }

            response = requests.get(url_head_hunter, params=params)
            if response.status_code == 200:

                vacancies = response.json()["items"]
                for vacancy in vacancies:

                    # Обработка данных по заработной плате
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

                    # Обработка формата для поля responsibility/requirement
                    convert_responsibility = format_text(vacancy["snippet"]["responsibility"])
                    convert_requirement = format_text(vacancy["snippet"]["requirement"])

                    # получаем всю информацию по запросу
                    self.__vacancies.append({"name": (vacancy["name"]).lower(),
                                             "url": (vacancy["url"]).lower(),
                                             "responsibility": convert_responsibility.lower(),
                                             "town": (vacancy["area"]["name"]).lower(),
                                             "employer": (vacancy["employer"]["name"]).lower(),
                                             "requirement": convert_requirement.lower(),
                                             "salary_from": (str(salary_from)).lower(),
                                             "salary_to": (str(salary_to)).lower(),
                                             })
            else:
                return "Error:", response.status_code

            # для обработки информации на следующей странице (all_pages = response.json()["pages"])
            page_number += 1


class SJ(Engine):
    """Класс для работы с SUPER JOB"""
    def __init__(self, api_key: str) -> None:
        self.__vacancies = []
        self.__config = [{"last request": "Последний запрос был к SUPER JOB"}]
        self.__api_key = api_key

    @property
    def vacancies(self) -> list:
        return self.__vacancies

    @property
    def config(self) -> list:
        return self.__config

    def get_request(self, keywords: str) -> None or str:
        """
         Запрос к ресурсу
        :param keywords: название вакансии для поиска
        :return: список с данными или None
        """
        print("Делаем запрос с SUPER JOB")
        url_super_job = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': self.__api_key}
        page_number = 1
        response_page = True

        while response_page:

            params = {"keywords": keywords,
                      "count": 100,
                      "page": page_number,
                      }

            response = requests.get(url_super_job, headers=headers, params=params)
            if response.status_code == 200:
                vacancies = response.json()["objects"]

                for vacancy in vacancies:
                    # Обработка формата для поля responsibility/requirement
                    convert_responsibility = format_text(vacancy["candidat"])
                    convert_requirement = format_text(vacancy["work"])

                    self.__vacancies.append({"name": (vacancy["profession"]).lower(),
                                             "url": (vacancy["link"]).lower(),
                                             "responsibility": convert_responsibility.lower(),
                                             "town": (vacancy["town"]["title"]).lower(),
                                             "employer": (vacancy["firm_name"]).lower(),
                                             "requirement": convert_requirement.lower(),
                                             "salary_from": (str(vacancy["payment_from"])).lower(),
                                             "salary_to": (str(vacancy["payment_to"])).lower()
                                             })

            else:
                return "Error:", response.status_code

            response_page = response.json()["more"]
            page_number += 1
