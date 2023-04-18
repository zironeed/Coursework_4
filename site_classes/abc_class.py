from abc import ABC, abstractmethod


class Engine(ABC):
    """Абстрактный метод для взаимодействия через API"""
    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass