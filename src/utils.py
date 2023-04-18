from job_classes.vacancies import HHVacancy, SJVacancy
api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"


def print_info(*args) -> None:
    """
    Распечатка данных при выборке данных из файла
    :param args: Атрибуты экземпляра вакансий
    :return: Строковое значение нужных атрибутов
    """
    for description in args:
        print(description)
    print("--------------------------------------")


def check_user_answer(print_1: str, print_2: dict or str, counts_cases: int) -> str or None:
    """
    Обработка вариантов ответов пользователя
    :param print_1: Сообщение пользователю
    :param print_2: Меню вариантов ответов
    :param counts_cases: Возможные варианты, которые может выбрать пользователь
    :return: Выбор пользователя
    """
    print(print_1)
    print(*print_2)
    while True:
        answer = input().lower()

        cases = [case for case in range(1, counts_cases + 1)]
        if answer in "00000":
            print("! Некорректная команда ввода !\n")
        elif answer in "":
            print("! Данные не переданы !\n")
        elif answer in str(cases):
            return answer
        else:
            print("! Некорректная команда ввода !\n")


def get_best_hh_vacancies(all_vacancy: list, count_of_vacancies: int) -> list:
    """
    Поиск лучших вакансий по ЗП для HEAD HUNTER.
    :param all_vacancy: В списке экземпляры класса, которые сортируются между собой
    :param count_of_vacancies: Количество отсортированных вакансий для вывода
    :return:Отсортированный список экземпляров
    """
    sort_dict = []
    for vacancy in all_vacancy:
        vacancy_instance = HHVacancy(vacancy)
        sort_dict.append(vacancy_instance)

    sort_dict.sort(reverse=True)
    return sort_dict[:count_of_vacancies]


def get_best_sj_vacancies(all_vacancy: list, count_of_vacancies: int) -> list:
    """
    Поиск лучших вакансий по ЗП для SUPER JOB.
    :param all_vacancy: В списке экземпляры класса, которые сортируются между собой
    :param count_of_vacancies: Количество отсортированных вакансий для вывода
    :return:Отсортированный список экземпляров
    """
    sort_dict = []
    for vacancy in all_vacancy:
        vacancy_instance = SJVacancy(vacancy)
        sort_dict.append(vacancy_instance)

    sort_dict.sort(reverse=True)
    return sort_dict[:count_of_vacancies]


def get_deep_query_hh_vacancies(all_vacancy: list, user_answer_value: str, user_answer_key: str) -> None:
    """
    Глубокий поиск по экземплярам вакансий HEAD HUNTER. Печать по условию.
    :param all_vacancy: Список всех вакансий из файла
    :param user_answer_value: Слово которое ищем
    :param user_answer_key: Номер поля по которому ищем
    :return:
    """
    if user_answer_value == "":
        print("Для поиска введено пустое поле.\n")

    else:
        if user_answer_key == "1":
            for vacancy in all_vacancy:
                vacancy_instance = HHVacancy(vacancy)
                if user_answer_value in vacancy_instance.name:
                    print(vacancy_instance)

        elif user_answer_key == "2":
            for vacancy in all_vacancy:
                vacancy_instance = HHVacancy(vacancy)
                if user_answer_value in vacancy_instance.responsibility:
                    print(vacancy_instance)

        elif user_answer_key == "3":
            for vacancy in all_vacancy:
                vacancy_instance = HHVacancy(vacancy)
                if user_answer_value in vacancy_instance.town:
                    print(vacancy_instance)

        elif user_answer_key == "4":
            for vacancy in all_vacancy:
                vacancy_instance = HHVacancy(vacancy)
                if user_answer_value in vacancy_instance.employer:
                    print(vacancy_instance)

        elif user_answer_key == "5":
            for vacancy in all_vacancy:
                vacancy_instance = HHVacancy(vacancy)
                if user_answer_value in str(vacancy_instance.requirement):
                    print(vacancy_instance)


def get_deep_query_sj_vacancies(all_vacancy: list, user_answer_value: str, user_answer_key: str) -> None:
    """
    Глубокий поиск по экземплярам вакансий SUPER JOB. Печать по условию.
    :param all_vacancy: Список всех вакансий из файла
    :param user_answer_value: Слово которое изем
    :param user_answer_key: Номер поля по которому ищем
    :return:
    """
    if user_answer_value == "":
        print("Для поиска введено пустое поле.\n")
    else:
        if user_answer_key == "1":
            for vacancy in all_vacancy:
                vacancy_instance = SJVacancy(vacancy)
                if user_answer_value in vacancy_instance.name:
                    print(vacancy_instance)

        elif user_answer_key == "2":
            for vacancy in all_vacancy:
                vacancy_instance = SJVacancy(vacancy)
                if user_answer_value in vacancy_instance.responsibility:
                    print(vacancy_instance)

        elif user_answer_key == "3":
            for vacancy in all_vacancy:
                vacancy_instance = SJVacancy(vacancy)
                if user_answer_value in vacancy_instance.town:
                    print(vacancy_instance)

        elif user_answer_key == "4":
            for vacancy in all_vacancy:
                vacancy_instance = SJVacancy(vacancy)
                if user_answer_value in vacancy_instance.employer:
                    print(vacancy_instance)

        elif user_answer_key == "5":
            for vacancy in all_vacancy:
                vacancy_instance = SJVacancy(vacancy)
                if user_answer_value in str(vacancy_instance.requirement):
                    print(vacancy_instance)
