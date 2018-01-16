"""
base contains base classes for Dataset which provide standardized interface
by which we can run different recommendation algorithms on variety of
different algorithms
"""

import os
import zipfile
from hashlib import md5
from abc import ABCMeta, abstractmethod

import requests
from config import settings

class Dataset(metaclass=ABCMeta):
    """
    Dataset is an abstract class that we use for creation and management of
    all our datasets.
    """
    _name = ""
    _download_url = ""
    dataset = None

    def _parent_dir(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(current_directory, settings.BASE_DOWNLOAD_DIR_NAME)

    def file_name(self):
        """
        file_name method is used to get path of where dataset can be accessed from
        once it is downloaded

        also ensure that the directory exists before returning the filename
        """
        file_name = md5(self._name.encode("utf-8")).hexdigest()

        if not os.path.exists(self._parent_dir()):
            os.mkdir(self._parent_dir())

        return os.path.join(self._parent_dir(), file_name)

    def download(self):
        """
        download function is used to fetch the data
        """
        file_path = self.file_name()
        print("Downloading file at", file_path)

        # Don't download file if we've done that already
        if not os.path.exists(file_path):
            file_to_save = open(file_path, "wb")
            with requests.get(self._download_url, verify=False, stream=True) as response:
                for chunk in response.iter_content(chunk_size=1024):
                    file_to_save.write(chunk)
            print("Completed downloading dataset")
        else:
            print("We already have this file cached locally")

    def download_and_unzip(self):
        """
        download_and_unzip takes care of both downloading and uncompressing
        """
        self.download()
        compressed_file_name = self.file_name()
        with zipfile.ZipFile(compressed_file_name, "r") as compressed_file:
            compressed_file.extractall(self._parent_dir())
        print("Completed uncompressing")

    @abstractmethod
    def download_post_process(self):
        """
        download_post_process is a method that need to be written
        specifically for each dataset, this is also responsible for
        parsing dataset and put it into this standard form
        """
        pass

    @abstractmethod
    def total_instances(self):
        """
        total_instances method is used to get total instances of that given dataset
        """
        pass

    def get_instances(self):
        """
        get_instances returns all instances of dataset
        """
        return self.dataset