from site_classes.site_classes import HeadHunter, SuperJob
from src.connector import Connector
from src.utils import *
from src.dictionary import user_questions, user_search, user_search_answers, user_search_vacancies,\
    user_search_answers_vacancies, user_search_sorted, user_search_sorted_answers


def main():

    connect_to_file = Connector('info.json')
    connect_to_config = Connector("config.json")

    while True:
        print(*user_questions[0])
        user_input = input()

        if user_input == user_questions[0]["5.Завершить обработку"]:
            break

        if user_input == user_questions[0][" 1.Запросить данные с сайта hh.ru\n"]:
            search_filter = (input("Введите слово поиска для вакансии\n")).lower()

            # Создаем экземпляр для работы с hh и делаем запрос
            head_hunter = HeadHunter()

            head_hunter.get_request(search_filter)
            respond = head_hunter.vacancies

            # Если данные получили, записываем в файл
            if respond:
                connect_to_config.insert(head_hunter.config)
                connect_to_file.insert(head_hunter.vacancies)

            else:
                print("Нет данных по запросу.\n")

        # Запросить данные с сайта sj
        elif user_input == user_questions[0]["2.Запросить данные с сайта superjob.ru\n"]:

            # Запрос на взаимодействие с токеном
            user_choice = check_user_input("Нужен токен подключения. Использовать свой - 1, использовать демо - 2", "",
                                            2)

            if user_choice == "1":
                sj_api_key = input("Введите токен\n")
            else:
                sj_api_key = "v3.r.137494512.c0bfbe9460bf69a9f1737c09e672ee1300ef0865.e3c764694" \
                             "d2428df6ccc1719788c0cc1f7cad2d8"

            search_filter = (input("Введите слово поиска для вакансии\n")).lower()

            # Создаем экземпляр для работы с sj и делаем запрос
            super_job = SuperJob(sj_api_key)
            super_job.get_request(search_filter)
            respond = super_job.vacancies

            # Если данные получили, записываем в файл
            if respond:
                connect_to_config.insert(super_job.config)
                connect_to_file.insert(super_job.vacancies)
            else:
                print("Нет данных по запросу.\n")

        # Работа с файлом
        elif user_input == user_questions[0]["3.Работа с файлом\n"]:

            # Валидация файла
            if connect_to_file.validate() is True:

                while True:

                    # Меню взаимодействия при работе с файлом
                    print(*user_questions[1])
                    user_input = input()

                    # Выйти в основное меню
                    if user_input == user_questions[1]["4.Выйти в команды верхнего меню\n"]:
                        break

                    # Выбор данных их файла
                    elif user_input == user_questions[1][" 1.Выбор данных их файла\n"]:

                        # Запрос на критерии выборки ключа поиска
                        user_key = check_user_input("Выберите поле для поиска.", user_search, 8)

                        # Ввод значение поля поиска
                        user_value = (input("Введите точное значение.\n")).lower()

                        search_filter = {user_search_answers[user_key]: user_value}
                        founded_vacancies = connect_to_file.select(search_filter)

                        if founded_vacancies:
                            input(
                                "Нажмите Enter. Будет выведена информация: Ссылка | Название | Город | Компания |"
                                " ЗП от | ЗП до|\n")
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
                    elif user_input == user_questions[1]["2.Удаление данных их файла\n"]:

                        # Запрос на критерии удаления данных
                        user_answer_key = check_user_input("Выберите поле для операции удаления вакансии.",
                                                            user_search, 8)

                        # Значение поля для удаления вакансии
                        user_value = (input("Введите значение для удаления.\n")).lower()
                        search_filter = {user_search_answers[user_answer_key]: user_value}
                        print(f"Было удалено:{connect_to_file.delete(search_filter)} вакансий.")
                        input("Операция проведена. Для продолжения нажмите Enter...")

                    # Полная сортировка данных файла
                    elif user_input == user_questions[1]["3.Полная сортировка данных файла\n"]:

                        # Запрос на критерии сортировки
                        user_key = check_user_input("Выберите поле для сортировки.", user_search_sorted, 5)

                        sorted_filter = user_search_sorted_answers[user_key]
                        connect_to_file.data_sort(sorted_filter)
                        input("Данные отсортированы. Для продолжения нажмите Enter...")

                    else:
                        print(*user_questions[3])

        # Работа с вакансиями
        elif user_input == user_questions[0]["4.Работа с вакансиями\n"]:

            # Валидация файла
            if connect_to_file.validate() is True:
                get_last_status_request = (connect_to_config.select({"*": "*"}))[0]["last request"]
                print(get_last_status_request)
                while True:

                    # Меню взаимодействия при работе с вакансиями
                    print(*user_questions[2])
                    user_input = input()

                    # Выйти в основное меню
                    if user_input == user_questions[2]["3.Выйти в команды верхнего меню\n"]:
                        break

                    # Вывести N самых высокооплачиваемые вакансии
                    elif user_input == user_questions[2][" 1.Вывести N самых высокооплачиваемые вакансии\n"]:
                        count_of_vacancies = int(check_user_input("Ввести искомое количество вакансий. От 1 до 100.",
                                                                  "", 100))

                        # Обработка для hh
                        if get_last_status_request == "Последний запрос был к hh.ru":
                            # Поиск высокооплачиваемые вакансии
                            all_vacancy = connect_to_file.select({"*": "*"})
                            best_vacancy = filter_hh_vacancies(all_vacancy, count_of_vacancies)
                            [print(vacancy) for vacancy in best_vacancy]

                        # Обработка для sj
                        if get_last_status_request == "Последний запрос был к superjob.ru":
                            # Поиск высокооплачиваемые вакансии
                            all_vacancy = connect_to_file.select({"*": "*"})
                            best_vacancy = filter_sj_vacancies(all_vacancy, count_of_vacancies)
                            [print(vacancy) for vacancy in best_vacancy]

                    # Гибкий поиск по вакансиям
                    elif user_input == user_questions[2]["2.Глубокий поиск по вакансиям\n"]:

                        # Запрос на критерии поиска и поиск по этим критериям
                        user_key = check_user_input("Выбрать поле для поиска.", user_search_vacancies, 5)

                        user_value = (input("Введите значение для поиска. Ищет совпадения.\n")).lower()
                        search_filter = {user_search_answers_vacancies[user_key]: user_value}

                        # Обработка для hh
                        if get_last_status_request == "Последний запрос был к hh.ru":
                            all_vacancy = connect_to_file.select({"*": "*"})
                            deep_search_hh_vacancies(all_vacancy, user_value, user_key)

                        # Обработка для sj
                        if get_last_status_request == "Последний запрос был к superjob.ru":
                            all_vacancy = connect_to_file.select({"*": "*"})
                            deep_search_sj_vacancies(all_vacancy, user_value, user_key)

                    else:
                        print(*user_questions[3])

        else:
            print(*user_questions[3])


main()
