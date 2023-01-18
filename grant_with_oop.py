class Student:
    def __init__(self, full_name, group_number, average_rating):
        self.full_name = full_name
        self.group_number = group_number
        self.average_rating = average_rating
    def scholarship_amount(self):
        if self.average_rating == 5:
            return 3000
        if 4 <= self.average_rating < 5:
            return 2000
        if 3 <= self.average_rating < 4:
            return 1500
        else:
            raise NotImplementedError

class GraduateStudent(Student):
    def scholarship_amount(self):
        if self.average_rating == 5:
            return 5000
        if 4 <= self.average_rating < 5:
            return 4500
        if 3 <= self.average_rating < 4:
            return 3500
        else:
            raise NotImplementedError
