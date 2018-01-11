import os
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

    def file_name(self):
        """
        file_name method is used to get path of where dataset can be accessed from
        once it is downloaded

        also ensure that the directory exists before returning the filename
        """
        file_name = md5(self._name.encode("utf-8")).hexdigest()
        current_directory = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.join(current_directory, settings.BASE_DOWNLOAD_DIR_NAME)

        if not os.path.exists(parent_dir):
            os.mkdir(parent_dir)

        return os.path.join(parent_dir, file_name)

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
