import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
BASE_DOWNLOAD_DIR_NAME = ".downloads"
STOPLIST_FILE_PATH = os.path.join(PROJECT_ROOT, "transforms", "stoplist.txt")
