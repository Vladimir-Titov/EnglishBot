from environs import Env


class MyEnv:
    env_message = Env()
    env = Env()
    env.read_env('.env')
    env.read_env('message.env')
