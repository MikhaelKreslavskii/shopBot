import telebot


###создание синглтона телеграмм бота
class BotSingleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = telebot.TeleBot('6728698451:AAGKVYgAFRGo0EQSZRCh2-A_EnNY_BbjQg0')
        return cls.instance
