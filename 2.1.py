class Logger:
    instance = None
    def __new__(cls):
     if cls.instance is None:
        cls.instance = super(Logger, cls).__new__(cls)
        cls.instance.logs = []
     return cls.instance

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs

logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")




print(logger1.get_logs())