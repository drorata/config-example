from config import Config
import mod
config = Config('./test.json')


print("In app: " + str(config.env))

mod.my_log()
