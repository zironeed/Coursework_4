from abc import ABC, abstractmethod


class Engine(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass
