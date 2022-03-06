class ExeptionPrintSendData(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        return f"Ошибка {self.msg}"


class PrintData:
    def print(self, data):
        self.send_data()
        print(f"печать: {str(data)}")

    def send_data(self):
        if not self.send_to_print():
            raise ExeptionPrintSendData("принтер не отвечает")

    @staticmethod
    def send_to_print():
        return False


p = PrintData()
p.print("123")
# try:
#     p.print("123")
# except ExeptionPrintSendData:
#     print("Ошибка печати")