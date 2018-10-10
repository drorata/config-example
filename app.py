from config import Config
config = Config('./test.json')
import mod


print("In app: " + str(config.env))

mod.my_log()
