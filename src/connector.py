import json
import os


class Connector:
    """Класс-коннектор к файлу"""
    def __init__(self, file_name: str) -> None:
        self.__file_data = file_name
        self.__file_path = None

    @property
    def file_data(self):
        return self.__file_data

    @file_data.setter
    def file_data(self, value: str) -> None:
        self.__file_data = value
        print("Успешно")
        self.try_connect()

    def try_connect(self) -> None:
        """Проверка доступности файла"""
        self.__file_path = os.path.join(os.getcwd(), 'data', self.__file_data)

        if os.path.isfile(self.__file_path) is False:
            file = open(self.__file_path, 'w+', encoding='UTF-8')
            file.close()
            print('Файл для хранения данных создан')

    def insert(self, data: list) -> None:
        """Запись данных в файл"""
        json_file = json.dumps(data, indent=4, ensure_ascii=False)

        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            file.write(json_file)

    def select(self, request: dict) -> list or str:
        """Выбор данных из файла по запросу"""
        sort_data = []

        with open(self.__file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        if request == {'*': '*'}:
            for cell in data:
                sort_data.append(cell)

        else:
            for cell in data:
                search_key = cell.get(*request, None)
                if search_key is not None:
                    if search_key == list(request.values())[0]:
                        sort_data.append(data)

        return sort_data

    def delete(self, request: dict) -> int:
        """Удаление указанных данных из файла"""
        required_data = []
        deleted_data_count = 0

        with open(self.__file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        for cell in data:
            search_key = cell.get(*request, None)

            if search_key is not None:
                if search_key == list(request.values())[0]:
                    deleted_data_count += 1

                else:
                    required_data.append(cell)

        json_file = json.dumps(required_data, indent=4, ensure_ascii=False)
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            file.write(json_file)

        return deleted_data_count

    def validate(self):
        """Обработка файла для хранения"""
        try:
            with open(self.__file_path, encoding='UTF-8') as file:
                json.load(file)
        except ValueError:
            print("Неверный формат файла")
            return False
        else:
            return True

    def data_sort(self, sort_key: str) -> list or str:
        """Сортировка данных"""
        with open(self.__file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        sort_list = sorted(data, key=lambda sorting: sorting[sort_key])

        json_file = json.dumps(sort_list)
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            file.write(json_file)
