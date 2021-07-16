import json

CONFIG_PATH = './config.json'
# do not change order of CONFIG_KEYS as index is used in Configuration class
CONFIG_KEYS = ("payment method", "search url", "browser name", "driver path")


class Configuration:
    def __init__(self):
        self._config = parse_json_file(CONFIG_PATH)

    @property
    def payment_method(self):
        return self._config[CONFIG_KEYS[0]]

    @property
    def search_url(self):
        return self._config[CONFIG_KEYS[1]]

    @property
    def browser_name(self):
        return self._config[CONFIG_KEYS[2]]

    @property
    def driver_path(self):
        return self._config[CONFIG_KEYS[3]]


def parse_json_file(path):
    try:
        with open(path) as file:
            config = json.load(file)
            if all(key in config for key in CONFIG_KEYS):
                return config
            else:
                raise Exception("invalid config keys in config.json")
    except json.JSONDecodeError:
        raise Exception("failed to decode config.json")
    except FileNotFoundError:
        raise Exception("invalid CONFIG_PATH")
    except Exception as e:
        raise e
