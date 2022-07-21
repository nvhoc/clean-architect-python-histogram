import logging

import yaml
import re
import os

PATTERN = r"\${(.*)}"
env = os.getenv('ENV', "local")
current_path = os.path.dirname(os.path.realpath(__file__))


def env_update(cfg):
    for key in cfg:
        c = cfg[key]
        type_c = type(c)
        if type_c is dict:
            env_update(c)
            continue
        if type_c is not str:
            continue
        matches = re.search(PATTERN, c)
        if not bool(matches):
            continue
        new_c = re.sub(PATTERN, os.getenv(matches.group(1), ""), c)
        cfg[key] = new_c


def get_config(config_path):
    print("open config by yaml at {}".format(config_path))
    with open(config_path, 'r') as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        env_update(config)
    return config


config_ins = get_config("{}/config_{}.yaml".format(current_path, env))
logging.info("....")


def __get(key):
    keys = key.split('.')
    ptr = config_ins
    for k in keys:
        ptr = ptr.get(k, None)
        if not type(ptr) is dict:
            return ptr
    return ptr


def get(key, default_value=None):
    value = __get(key)
    if value is None:
        return default_value
    return value
