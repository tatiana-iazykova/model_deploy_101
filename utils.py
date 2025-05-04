from typing import Dict, Any

import yaml


def load_config(path: str) -> Dict[str, Any]:
    """
    Safely loads config file
    :param path: path to onfig
    :return:
    """
    with open(path, "r", encoding="utf-8") as yamlfile:
        data = yaml.safe_load(yamlfile)
        return data
