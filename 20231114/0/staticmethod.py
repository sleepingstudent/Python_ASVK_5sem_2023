class Sender:
    st = "Greeting!"
    @classmethod
    def report(cls, arg):
        print(cls.st)
        cls.st = "Get away"
        
class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            Sender.report(i)

Asker().askall([Sender() for i in range(3)])