



class Student:
    def __init__(self,id,name,gender,major,average,classified):
        self._id = id
        self._name = name
        self._gender = gender
        self._major = major
        self._average = average
        self._classifed = classified

class ClassA1 :
    studentList  = []
    def studentQuantity(self):
        return len(self.studentList)

    def generateId(self):
        maxId = 1
        if self.studentQuantity() > 0:
            maxId = self.studentList[0]._id
            for sv in self.studentList:
                if maxId < sv._id:
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def addStudent(self):
        student_id = self.generateId()
        name = input("Enter student's name: ")
        gender = input("Enter student's gender: ")
        major = input("Enter student's major: ")
        average = float(input("Enter student's average grade: "))
        classified = input("Enter student's classification: ")

        new_student = Student(student_id, name, gender, major, average, classified)
        self.xeploaihocluc(new_student)
        self.studentList.append(new_student)

    def updateStudent(self,id):
        sv:Student = self.findByID(id)
        if(sv != None):

    def xeploaihocluc(self, new_student):

