import os
from os.path import abspath

USER_DATA_DIR = os.environ.get("REWARDS_USER_DATA_DIR", abspath("./data-dir"))
PROFILE_NAME = "Default"