import os
from os.path import abspath

USER_DATA_DIR = os.environ.get("REWARDS_USER_DATA_DIR", abspath("./data-dir"))
PROFILE_NAME = "Default"
NOUNS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "nouns.txt")