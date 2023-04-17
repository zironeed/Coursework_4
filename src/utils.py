from job_classes.vacancies import HHVacancy, SJVacancy


def check_user_input(message: str, choice_menu: dict, choice_count: int) -> None or str:
    """
    Обработка ответов пользователя
    :param message: сообщение пользователю
    :param choice_menu: Меню вариантов ответа
    :param choice_count: Возможные варианты ответа
    :return: Конечный выбор пользователя
    """
    print(message)
    print(choice_menu)

    while True:
        user_input = input().lower()
        choices = [choice for choice in range(1, choice_count + 1)]

        if user_input in "00000":
            print("Некорректная команда ввода. Пожалуйста, введите что-нибудь другое\n")
        elif user_input in "":
            print("Данные не переданы. Пожалуйста, введите что-нибудь другое\n")
        elif user_input in str(choices):
            return user_input
        else:
            print("Некорректная команда ввода. Пожалуйста, введите что-нибудь другое\n")


def filter_hh_vacancies(vacancies: list, vacancy_count: int) -> list:
    """Сортировка по ЗП для hh.ru"""
    sort_list = []

    for vacancy in vacancies:
        vacancy_instance = HHVacancy(vacancy)
        sort_list.append(vacancy_instance)

    sort_list.sort(reverse=True)

    return sort_list[:vacancy_count]


def filter_sj_vacancies(vacancies: list, vacancy_count: int) -> list:
    """Сортировка по ЗП для superjob.ru"""
    sort_list = []

    for vacancy in vacancies:
        vacancy_instance = HHVacancy(vacancy)
        sort_list.append(vacancy_instance)

    sort_list.sort(reverse=True)

    return sort_list[:vacancy_count]


def deep_search_hh_vacancies(vacancies: list, user_value: str, user_key: str) -> None:
    """Глубокий поиск по экземплярам вакансий hh.ru"""
    if user_value == "":
        print("Введено пустое поле\n")

    else:
        if user_key == "1":
            for vacancy in vacancies:
                vacancy_instance = HHVacancy(vacancy)
                if user_value in vacancy_instance.name:
                    print(vacancy_instance)

        elif user_key == "2":
            for vacancy in vacancies:
                vacancy_instance = HHVacancy(vacancy)
                if user_value in vacancy_instance.responsibility:
                    print(vacancy_instance)

        elif user_key == "3":
            for vacancy in vacancies:
                vacancy_instance = HHVacancy(vacancy)
                if user_value in vacancy_instance.town:
                    print(vacancy_instance)

        elif user_key == "4":
            for vacancy in vacancies:
                vacancy_instance = HHVacancy(vacancy)
                if user_value in vacancy_instance.employer:
                    print(vacancy_instance)

        elif user_key == "5":
            for vacancy in vacancies:
                vacancy_instance = HHVacancy(vacancy)
                if user_value in str(vacancy_instance.requirement):
                    print(vacancy_instance)


def deep_search_sj_vacancies(vacancies: list, user_value: str, user_key: str) -> None:
    """Глубокий поиск по экземплярам вакансий superjob.ru"""
    if user_value == "":
        print("Введено пустое поле\n")

    else:
        if user_key == "1":
            for vacancy in vacancies:
                vacancy_instance = SJVacancy(vacancy)
                if user_value in vacancy_instance.name:
                    print(vacancy_instance)

        elif user_key == "2":
            for vacancy in vacancies:
                vacancy_instance = SJVacancy(vacancy)
                if user_value in vacancy_instance.responsibility:
                    print(vacancy_instance)

        elif user_key == "3":
            for vacancy in vacancies:
                vacancy_instance = SJVacancy(vacancy)
                if user_value in vacancy_instance.town:
                    print(vacancy_instance)

        elif user_key == "4":
            for vacancy in vacancies:
                vacancy_instance = SJVacancy(vacancy)
                if user_value in vacancy_instance.employer:
                    print(vacancy_instance)

        elif user_key == "5":
            for vacancy in vacancies:
                vacancy_instance = SJVacancy(vacancy)
                if user_value in str(vacancy_instance.requirement):
                    print(vacancy_instance)
