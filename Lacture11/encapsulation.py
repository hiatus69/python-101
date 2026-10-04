class employee():
    def __init__(self):
        self.__maxearn = 30000

    def earn(self):
        print("earning is:{}".format(self.__maxearn))

    #setter method used for accesing private class
    def setMaxearn(self, earn):
        self.__maxearn = earn

emp1 = employee()
emp1.earn()

emp1.__maxearn = 10000
emp1.earn()

emp1.setMaxearn(10000)
emp1.earn()