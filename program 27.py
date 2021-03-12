class Classroom:
    classroom_list=[1,2,3,4,5,65,7,8]
    @staticmethod
    def serach_classroom(class_room):
        if class_room in [i for i in Classroom.classroom_list]:
            return "Found"
        else:
            return -1



c1 =Classroom()
print(c1.serach_classroom(8))
