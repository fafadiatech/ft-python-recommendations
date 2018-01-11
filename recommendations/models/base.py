from abc import ABCMeta, abstractmethod


class Dataset(metaclass=ABCMeta):
    """
    Dataset is an abstract class that we use for creation and management of
    all our datasets.
    """

    @abstractmethod
    def download(self):
        """
        download function is used to fetch the data
        """
        pass

    @abstractmethod
    def init(self):
        """
        init method is used for initialization of dataset
        """
        pass

    @abstractmethod
    def total_instances(self):
        """
        total_instances method is used to get total instances of that given dataset
        """
        pass


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
