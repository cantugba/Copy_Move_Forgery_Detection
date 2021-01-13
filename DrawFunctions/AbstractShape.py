from abc import ABCMeta, abstractmethod

class AbstractShape(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, image, keypoints1, keypoints2, color): pass
