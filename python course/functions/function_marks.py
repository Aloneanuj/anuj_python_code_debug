def marks(math, english, science, Hindi, physics):
    total = math + english + science + Hindi + physics
    percent = (total / 500) * 100
    print(f"Total Marks = {total}")
    print(f"Percentage = {percent}")


math_marks = int(input("Enter Math marks"))
english_marks = int(input("Enter english marks"))
science_marks = int(input("Enter science marks"))
hindi_marks = int(input("Enter hindi marks"))
physics_marks = int(input("Enter physics marks"))

marks(math_marks, english_marks, science_marks, hindi_marks, physics_marks)
