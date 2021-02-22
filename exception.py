class MyClassExcept(Exception):

    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def check_number(number):
        try:
            int(number)
            return True
        except ValueError:
            return False
