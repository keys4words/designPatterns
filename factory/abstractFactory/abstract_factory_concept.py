from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB


class IAbstractFactory(metaclass=ABCMeta):
    "The Static Abstract factory interface method"


class AbstractFactory(IAbstractFactory):
    "The Abstract factory Concrete Class"

    @staticmethod
    def create_object(factory):
        "Static get_factory method"
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA().create_object(factory[1])
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB().create_object(factory[1])
            raise Exception('No Factory Found')
        except Exception as e:
            print(e)
        return None


pr1 = AbstractFactory.create_object('ab')
print(f"{pr1.__class__}")
pr2 = AbstractFactory.create_object('bc')
print(f"{pr2.__class__}")