import yaml
import re
import os

from config.base import Config

PATTERN = r"\${(.*)}"
env = os.getenv('ENV', "local")
current_path = os.path.dirname(os.path.realpath(__file__))
config_by_path = {}


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
        config = yaml.load(ymlfile)
        env_update(config)
    return Config(config)


def of(config_path="{}/config_{}.yaml".format(current_path, env)):
    config_ins = config_by_path.get(config_path, None)
    if config_ins:
        return config_ins
    config_by_path[config_path] = get_config(config_path)
    return config_by_path[config_path]
