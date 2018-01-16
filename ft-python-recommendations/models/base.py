"""
base contains base classes for recommendation algorithms
"""
from abc import ABCMeta, abstractmethod


class RecommendationAlgorithm(metaclass=ABCMeta):
    """
    RecommendationAlgorithm is an abstract class that we can used to
    implement different recommendation algorithms
    """
    @abstractmethod
    def train(self):
        """
        train method is used to implement training logic
        """
        pass

    @abstractmethod
    def predict(self):
        """
        predict method is used to get/generate recommendations
        """
        pass
