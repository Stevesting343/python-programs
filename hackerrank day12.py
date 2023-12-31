# # inheritance

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self,firstName, lastName,idNumber,scores):

            super().__init__(firstName, lastName, idNumber) # we take here super function  to accsess person constructor value
            self.scores = scores

    def calculate(self):
        sum = 0
        for score in scores:

            sum += score

        average = sum/len(scores)
        if average < 40:
            return "T"
        elif average < 55:
            return "D"
        elif average < 70:
            return "P"
        elif average < 80:
            return "A"
        elif average < 90:
            return "E"
        else :
            return "O"





line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())