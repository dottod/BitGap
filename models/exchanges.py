from abc import ABC, abstractmethod

class Exchanges(ABC):
    @abstractmethod
    def buyAPI(self, amount, symbol):
        pass

    @abstractmethod
    def getPriceAPI(self, symbol):
        pass

    @abstractmethod
    def sellAPI(self, amount, symbol):
        pass

    @abstractmethod
    def execute_exchange(self, exchange):
        pass

    @abstractmethod
    def set_authorization(self, api_key, secret_key):
        pass

