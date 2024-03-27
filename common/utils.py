import sys
from pathlib import Path

import yaml
from dynaconf import Dynaconf
BASE_DIR = Path(__file__).resolve().parent.parent



















def load_config(file_path: str) -> dict:
    config = Dynaconf(settings_files=[file_path])
    print(config["telegram"])
    # with open(f"{str(BASE_DIR)}/{config_path}") as stream:
    #     try:
    #         config = yaml.safe_load(stream)
    #     except yaml.YAMLError as exc:
    #         sys.exit(0)

    return config
