from config import Config

config = Config()


def my_log():
    print("In mode: " + str(config.env))
