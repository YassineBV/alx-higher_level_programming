#!/usr/bin/python3
for numb1 in range(0, 10):
    for numb2 in range (0, 10):
        if numb1 != numb2 and numb1 < numb2:
            if numb1 == 8 and numb2 == 9:
                print(f"{numb1}{numb2}")
            else:
                print(f"{numb1}", end="")
                print(f"{numb2}", end=", ")