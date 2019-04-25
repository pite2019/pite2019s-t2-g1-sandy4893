'''
Student Registry
'''
import sys

true = 1
false = 0
classList = []

class Student:
    _name = []
    _attendance = []
    _score = []

    def __init__(self):
        self._name = []
        self._attendance = []
        self._score = []

    def getStudentName(self, index):
        return self._name[index]

    def setStudentName(self, name):
        self._name.append(name)

    def getStudentAttendance(self, index):
        return self._attendance[index]

    def setStudentAttendance(self, attendance):
        self._attendance.append(attendance)

    def getStudentScore(self, index):
        return self._score[index]

    def setStudentScore(self, score):
        self._score.append(score)

    def getNumberOfStudents(self):
        return len(self._name)

class Class(Student):
    _avgScore = 0
    _totalStudents = 0
    _classNumber = 0

    def __init__(self, classNumber = 0):
        self._avgScore = 0
        self._totalStudents = 0
        #print(classNumber)
        self._classNumber = classNumber
        super(Class, self).__init__()

    def getTotalStudents(self):
        self._totalStudents = super().getNumberOfStudents()
        #print(super().getNumberOfStudents())
        return self._totalStudents

    def getAverageScore(self):
        sum = 0
        #print("total:",self.getTotalStudents())
        for index in range(self.getTotalStudents()):
            sum += super().getStudentScore(index)
        return sum/self._totalStudents

    def getClassNumber(self):
        return self._classNumber

    def setClassNumber(self, classNumber):
        self._classNumber = classNumber

class School(Class):
    _classInstances = []

    def __init__(self):
        pass

    def createInstances(self, *vargs):
        newClass = Class(vargs[0])
        #super(School, self).__init__(vargs[0], vargs[1])
        #print("new class: ",newClass)
        self._classInstances.append(newClass)


    def printInstances(self):
        print(self._classInstances)

    def enterStudentDetails(self, classNum, name, attendance, score):
        #print("enterstu:",self._classInstances[classNum - 1])
        self._classInstances[classNum - 1].setStudentName(name)
        self._classInstances[classNum - 1].setStudentAttendance(attendance)
        self._classInstances[classNum - 1].setStudentScore(score)

    def setClassNumber(self, classNumber):
        self.printInstances()
        self._classInstances[_classNumber - 1].setClassNumber(classNumber)

    def getStudentName(self, classNum, index):
        #print("getstu:",self._classInstances[classNum - 1])
        return self._classInstances[classNum - 1].getStudentName(index)

    def getStudentAttendance(self, classNum, index):
        return self._classInstances[classNum - 1].getStudentAttendance(index)

    def getStudentScore(self, classNum, index):
        return self._classInstances[classNum - 1].getStudentScore(index)

    def getTotalStudents(self, classNum):
        return self._classInstances[classNum - 1].getTotalStudents()

    def getAverageScore(self, classNum):
        return self._classInstances[classNum - 1].getAverageScore()

    def getAvgScoresAllClasses(self):
        sum = 0
        for classIndex in range(len(self._classInstances)):
            sum += self._classInstances[classIndex].getAverageScore()
        return sum/len(self._classInstances)

    def displayStudentsDetails(self, classNumber):
        totalStudent = self.getTotalStudents(classNumber)
        #print("tot:", totalStudent)
        for studentIndex in range(totalStudent):
            print("Student's name is %s, has attendance of %d and score of %d" % ( \
                self.getStudentName(classNumber, studentIndex), self.getStudentAttendance(classNumber, studentIndex), self.getStudentScore(classNumber, studentIndex)))


def operation(operationIndex):
        if operationIndex == 1:
            classNumber = int(input("Enter Class number: "))
            if classNumber not in classList:
                s.createInstances(classNumber)
                classList.append(classNumber)
            studentName = str(input("Enter student name: "))
            studentAttendance = int(input("Enter attendance detail: "))
            studentScore = int(input("Enter score: "))
            s.enterStudentDetails(classNumber, studentName, studentAttendance, studentScore)
        elif operationIndex == 2:
            classNumber = int(input("Enter Class number: "))
            if classNumber in classList:
                s.displayStudentsDetails(classNumber)
            else:
                print("Information not available")
        elif operationIndex == 3:
            classNumber = int(input("Enter Class number: "))
            if classNumber in classList:
                print("Total no. of students in class %d are %d" %(classNumber, s.getTotalStudents(classNumber)))
            else:
                print("Information not available")
        elif operationIndex == 4:
            classNumber = int(input("Enter Class number: "))
            if classNumber in classList:
                print("Average score in the class: %.4f" %(s.getAverageScore(classNumber)))
            else:
                print("Information not available")
        elif operationIndex == 5:
            if len(classList) != 0:
                print("Average score across all the classes: %.4f" % (s.getAvgScoresAllClasses()))
            else:
                print("Information not available")
        elif operationIndex == 6:
                sys.exit(0);


print("Welcome to the School Registry Wizard")
#numOfClasses = int(input("Enter number of classes in the school: "))
global s
s = School()
#print(s)

#s.setClassNumber(classNumber)
while true:
    print("List of operations available: ")
    print("1: Enter student details")
    print("2: Get all Students details")
    print("3: Get total number of students in the class")
    print("4: Average score in the class")
    print("5: Average score across all the classes")
    print("6: Exit")
    inputValue = int(input("Enter Input: "))
    operation(inputValue)
