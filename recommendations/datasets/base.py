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
