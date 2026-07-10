import os
os.system("cls")

location = input("Enter starting location (A/B):").upper()
clean = ['n','n']
while True:
    if location == "A":
        ans = input("Is location A clean? (y/n): ").lower()

        if ans == "n":
            print("Vacuuming A...")
            clean[0] ='y'
        else:
            print("A is already clean.")

        location = "B"
        

    else:
        ans = input("Is location B clean? (y/n): ").lower()

        if ans == "n":
            print("Vacuuming B...")
            clean[1] ='y'
        else:
            print("B is already clean.")

        location = "A"

    a = input("Is A clean now? (y/n): ").lower()
    b = input("Is B clean now? (y/n): ").lower()

    if a == "y" and b == "y":
        print("Both locations are clean. Exiting...")
        break