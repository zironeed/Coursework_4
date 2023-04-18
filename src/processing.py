from site_classes.site_classes import HH, SJ
from src.connector import Connector
from src.dictionary import user_questions, user_search, user_search_answers, user_search_vacancies,\
    user_search_answers_vacancies, user_search_sorted, user_search_sorted_answers
from src.utils import *


def main_processing() -> None:
    """ Основная обработка запросов пользователя """

    connector_to_file = Connector("information.json")
    connector_to_file_config = Connector("configuration.json")

    while True:
        # Основное меню взаимодействия
        print(*user_questions[0])
        user_answer = input()

        # Завершить обработку
        if user_answer == user_questions[0]["5.Завершить обработку"]:
            break

        # Запросить данные с сайта HEAD HUNTER
        if user_answer == user_questions[0][" 1.Запросить данные с сайта HEAD HUNTER\n"]:
            search_filter = (input("Введите слово поиска для вакансии\n")).lower()

            # Создаем экземпляр для работы с HEAD HUNTER и делаем запрос
            head_hunter = HH()

            head_hunter.get_request(search_filter)
            respond = head_hunter.vacancies

            # Если данные получили, записываем в файл
            if respond:
                connector_to_file_config.insert(head_hunter.config)
                connector_to_file.insert(head_hunter.vacancies)

            else:
                print("Нет данных по запросу.\n")

        # Запросить данные с сайта SUPER JOB
        elif user_answer == user_questions[0]["2.Запросить данные с сайта SUPER JOB\n"]:

            # Запрос на взаимодействие с токеном
            user_choice = check_user_answer("Нужен токен подключения. Использовать свой - 1, использовать демо - 2", "",
                                            2)

            if user_choice == "1":
                sj_api_key = input("Введите токен\n")
            else:
                sj_api_key = api_key

            search_filter = (input("Введите слово поиска для вакансии\n")).lower()

            # Создаем экземпляр для работы с SUPER JOB и делаем запрос
            super_job = SJ(sj_api_key)
            super_job.get_request(search_filter)
            respond = super_job.vacancies

            # Если данные получили, записываем в файл
            if respond:
                connector_to_file_config.insert(super_job.config)
                connector_to_file.insert(super_job.vacancies)
            else:
                print("Нет данных по запросу.\n")

        # Работа с файлом
        elif user_answer == user_questions[0]["3.Работа с файлом\n"]:

            # Валидация файла
            if connector_to_file.validate() is True:

                while True:

                    # Меню взаимодействия при работе с файлом
                    print(*user_questions[1])
                    user_answer = input()

                    # Выйти в основное меню
                    if user_answer == user_questions[1]["4.Выйти в команды верхнего меню\n"]:
                        break

                    # Выбор данных их файла
                    elif user_answer == user_questions[1][" 1.Выбор данных их файла\n"]:

                        # Запрос на критерии выборки ключа поиска
                        user_answer_key = check_user_answer("Выберите поле для поиска.", user_search, 8)

                        # Ввод значение поля поиска
                        user_answer_value = (input("Введите точное значение.\n")).lower()

                        search_filter = {user_search_answers[user_answer_key]: user_answer_value}
                        founded_vacancies = connector_to_file.select(search_filter)

                        if founded_vacancies:
                            input(
                                "Нажмите Enter. Будет выведена информация: Ссылка|Название|Город|Компания|ЗП от|ЗП до|\n")
                            for vacancy in founded_vacancies:
                                vacancy_instance = HHVacancy(vacancy)

                                print_info(vacancy_instance.url,
                                           vacancy_instance.name,
                                           vacancy_instance.town,
                                           vacancy_instance.employer,
                                           vacancy_instance.salary_from,
                                           vacancy_instance.salary_to)

                        input("Для продолжения нажмите Enter...")

                    # Удаление данных их файла
                    elif user_answer == user_questions[1]["2.Удаление данных их файла\n"]:

                        # Запрос на критерии удаления данных
                        user_answer_key = check_user_answer("Выберите поле для операции удаления вакансии.",
                                                            user_search, 8)

                        # Значение поля для удаления вакансии
                        user_answer_value = (input("Введите значение для удаления.\n")).lower()
                        search_filter = {user_search_answers[user_answer_key]: user_answer_value}
                        print(f"Было удалено:{connector_to_file.delete(search_filter)} вакансий.")
                        input("Операция проведена. Для продолжения нажмите Enter...")

                    # Полная сортировка данных файла
                    elif user_answer == user_questions[1]["3.Полная сортировка данных файла\n"]:

                        # Запрос на критерии сортировки
                        user_answer_key = check_user_answer("Выберите поле для сортировки.", user_search_sorted, 5)

                        sorted_filter = user_search_sorted_answers[user_answer_key]
                        connector_to_file.sort_all(sorted_filter)
                        input("Данные отсортированы. Для продолжения нажмите Enter...")

                    else:
                        print(*user_questions[3])

        # Работа с вакансиями
        elif user_answer == user_questions[0]["4.Работа с вакансиями\n"]:

            # Валидация файла
            if connector_to_file.validate() is True:
                get_last_status_request = (connector_to_file_config.select({"*": "*"}))[0]["last request"]
                print(get_last_status_request)
                while True:

                    # Меню взаимодействия при работе с вакансиями
                    print(*user_questions[2])
                    user_answer = input()

                    # Выйти в основное меню
                    if user_answer == user_questions[2]["3.Выйти в команды верхнего меню\n"]:
                        break

                    # Вывести N самых высокооплачиваемые вакансии
                    elif user_answer == user_questions[2][" 1.Вывести N самых высокооплачиваемые вакансии\n"]:
                        count_of_vacancies = int(check_user_answer("Ввести искомое количество вакансий. От 1 до 100.", "", 100))

                        # Обработка для HEAD HUNTER
                        if get_last_status_request == "Последний запрос был к HEAD HUNTER":
                            # Поиск высокооплачиваемые вакансии
                            all_vacancy = connector_to_file.select({"*": "*"})
                            best_vacancy = get_best_hh_vacancies(all_vacancy, count_of_vacancies)
                            [print(vacancy) for vacancy in best_vacancy]

                        # Обработка для SUPER JOB
                        if get_last_status_request == "Последний запрос был к SUPER JOB":
                            # Поиск высокооплачиваемые вакансии
                            all_vacancy = connector_to_file.select({"*": "*"})
                            best_vacancy = get_best_sj_vacancies(all_vacancy, count_of_vacancies)
                            [print(vacancy) for vacancy in best_vacancy]

                    # Гибкий поиск по вакансиям
                    elif user_answer == user_questions[2]["2.Глубокий поиск по вакансиям\n"]:

                        # Запрос на критерии поиска и поиск по этим критериям
                        user_answer_key = check_user_answer("Выбрать поле для поиска.", user_search_vacancies, 5)

                        user_answer_value = (input("Введите значение для поиска. Ищет совпадения.\n")).lower()
                        search_filter = {user_search_answers_vacancies[user_answer_key]: user_answer_value}

                        # Обработка для HEAD HUNTER
                        if get_last_status_request == "Последний запрос был к HEAD HUNTER":
                            all_vacancy = connector_to_file.select({"*": "*"})
                            get_deep_query_hh_vacancies(all_vacancy, user_answer_value, user_answer_key)

                        # Обработка для SUPER JOB
                        if get_last_status_request == "Последний запрос был к SUPER JOB":
                            all_vacancy = connector_to_file.select({"*": "*"})
                            get_deep_query_sj_vacancies(all_vacancy, user_answer_value, user_answer_key)

                    else:
                        print(*user_questions[3])

        else:
            print(*user_questions[3])