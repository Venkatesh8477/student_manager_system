class studdentsmanager:
    def __init__(self):
        self.students = {}
    def add_students(self,student_id,name,marks):
        if student_id in self.students:
            raise ValueError("student is already exits")
        if not 0 <=marks<= 100:
            raise ValueError("enter correct marks")
        self.students[student_id] = {
            "name":name,
            "marks":marks
        }
    def get_student(self,student_id):
        if student_id not in self.students:
            raise ValueError("user doesnot exist")
        return self.students[student_id]
    def calulate(self):
        if not self.students:
            return 0
        total=sum(
            student["marks"]
            for student in self.students.values()
        )
        return total/len(self.students)
manager = studdentsmanager()
try:
    manager.add_students(101,"venky",45)
    manager.add_students(102,"sai",98)
    manager.get_student(102)
    print("avg marks",manager.calulate())
except (ValueError,KeyError) as e:
    print("Error:",e)

    