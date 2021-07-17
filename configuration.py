import json

CONFIG_PATH = './config.json'
# can add more keys
# but do not change order of prev keys as index is used in Configuration class
KEYS = ("settings", "actions")
SETTINGS_KEYS = ("payment method", "browser name", "driver path")


class Configuration:
    def __init__(self):
        self._config = parse_json_file(CONFIG_PATH)
        self._settings = self._config[KEYS[0]]
        self._actions = self._config[KEYS[1]]

    @property
    def payment_method(self):
        return self._settings[SETTINGS_KEYS[0]]

    @property
    def browser_name(self):
        return self._settings[SETTINGS_KEYS[1]]

    @property
    def driver_path(self):
        return self._settings[SETTINGS_KEYS[2]]

    @property
    def actions(self):
        return self._actions


def parse_json_file(path):
    try:
        with open(path) as file:
            config = json.load(file)
            if all(key in config[KEYS[0]] for key in SETTINGS_KEYS) and all(key in config for key in KEYS):
                return config
            else:
                raise Exception("invalid keys in config.json")
    except json.JSONDecodeError:
        raise Exception("failed to decode config.json")
    except FileNotFoundError:
        raise Exception("invalid CONFIG_PATH")
    except Exception as e:
        raise e