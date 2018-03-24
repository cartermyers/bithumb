from abc import ABCMeta, abstractmethod

class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    def set_image(self, src):
        pass
