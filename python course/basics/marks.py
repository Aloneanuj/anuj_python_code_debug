maths = int(input("input enter the math marks = "))
physics = int(input("input enter the physics marks ="))
hindi = int(input("input enter the hindi marks = "))
chemistry = int(input("input enter the chemistry marks= "))
biology = int(input("input enter the biology marks = "))

percent = ((maths + physics + chemistry + hindi + biology) / 500) * 100
print(f"your percentage = {percent:4f}")
