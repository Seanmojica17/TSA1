import pickle

class StudentRecord:
    def __init__(self, student_id, name, class_standing, exam_grade):
        self.student_id = student_id
        self.name = name  # Tuple (first_name, last_name)
        self.class_standing = class_standing
        self.exam_grade = exam_grade

    def grade(self):
        # 60% of class standing + 40% of exam grade
        return self.class_standing * 0.6 + self.exam_grade * 0.4

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name[0]} {self.name[1]}, Standing: {self.class_standing}, Exam Grade: {self.exam_grade}, Final Grade: {self.grade():.2f}"

class StudentManagement:
    def __init__(self):
        self.students = []
        self.file_name = ""

    def open_file(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                self.students = pickle.load(file)
                self.file_name = file_name
                print("File loaded successfully.")
        except Exception as e:
            print(f"Error opening file: {e}")

    def save_file(self):
        if self.file_name:
            try:
                with open(self.file_name, 'wb') as file:
                    pickle.dump(self.students, file)
                print("File saved successfully.")
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print("No file loaded. Use 'Save As' to choose a file location.")

    def save_as_file(self, file_name):
        try:
            with open(file_name, 'wb') as file:
                pickle.dump(self.students, file)
            self.file_name = file_name
            print("File saved successfully as", file_name)
        except Exception as e:
            print(f"Error saving file: {e}")

    def show_all_students(self):
        if not self.students:
            print("No records available.")
            return
        for student in self.students:
            print(student)

    def order_by_last_name(self):
        sorted_students = sorted(self.students, key=lambda x: x.name[1])
        for student in sorted_students:
            print(student)

    def order_by_grade(self):
        sorted_students = sorted(self.students, key=lambda x: x.grade(), reverse=True)
        for student in sorted_students:
            print(student)

    def show_student_record(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            print(student)
        else:
            print(f"Student with ID {student_id} not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, exam_grade):
        new_student = StudentRecord(student_id, (first_name, last_name), class_standing, exam_grade)
        self.students.append(new_student)
        print("Record added successfully.")

    def edit_record(self, student_id, first_name=None, last_name=None, class_standing=None, exam_grade=None):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            if first_name: student.name = (first_name, student.name[1])
            if last_name: student.name = (student.name[0], last_name)
            if class_standing is not None: student.class_standing = class_standing
            if exam_grade is not None: student.exam_grade = exam_grade
            print("Record updated successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_record(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            self.students.remove(student)
            print("Record deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

def print_menu():
    print("\n--- Student Record Management ---")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("0. Exit")
    
def main():
    management = StudentManagement()

    while True:
        print_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            file_name = input("Enter file name to open: ")
            management.open_file(file_name)
        elif choice == '2':
            management.save_file()
        elif choice == '3':
            file_name = input("Enter new file name: ")
            management.save_as_file(file_name)
        elif choice == '4':
            management.show_all_students()
        elif choice == '5':
            management.order_by_last_name()
        elif choice == '6':
            management.order_by_grade()
        elif choice == '7':
            student_id = int(input("Enter student ID to view: "))
            management.show_student_record(student_id)
        elif choice == '8':
            student_id = int(input("Enter student ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing grade: "))
            exam_grade = float(input("Enter exam grade: "))
            management.add_record(student_id, first_name, last_name, class_standing, exam_grade)
        elif choice == '9':
            student_id = int(input("Enter student ID to edit: "))
            first_name = input("Enter first name (leave blank to keep current): ")
            last_name = input("Enter last name (leave blank to keep current): ")
            class_standing = input("Enter class standing grade (leave blank to keep current): ")
            exam_grade = input("Enter exam grade (leave blank to keep current): ")
            management.edit_record(
                student_id,
                first_name if first_name else None,
                last_name if last_name else None,
                float(class_standing) if class_standing else None,
                float(exam_grade) if exam_grade else None
            )
        elif choice == '10':
            student_id = int(input("Enter student ID to delete: "))
            management.delete_record(student_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
