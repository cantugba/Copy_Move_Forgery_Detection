from abc import ABCMeta, abstractmethod

class AbstractShape(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, image, key_points1, key_points2, color): pass