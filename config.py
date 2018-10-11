import json


class Config:
    __state = {}

    def __init__(self, env=None):
        self.__dict__ = Config.__state
        if self.__dict__ == {}:
            if env is None:
                # New instance. Still not initialized
                return
            else:
                self.__set_config(env)

    def __set_config(self, env):
        with open(env, 'r') as f:
            self.env = json.load(f)

    def get_var(self, key):
        return self.env[key]
