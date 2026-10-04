class StudentTest:
    def __init__(self,name,score1,score2,score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def sumScore(self):
        return self.score1 + self.score2 + self.score3

    def __str__(self):
        return "Name: {} Score1: {} Score2: {} Score3: {}".format(self.name,self.score1,self.score2,self.score3)

std1 = StudentTest("John", 80, 90, 70)
print(std1)
print(std1.name, std1.sumScore())