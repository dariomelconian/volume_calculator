#           DRAFT BEING TEMP. USED          #
# Dario Melconian
# 251044493
# this program computes the volumes for 3 shapes, and lists them in decreasing to increasing order

# first import functions from summarize and volume python files created as part of this assignment
from volume import cubeVolume, pyramidVolume, ellipsoidVolume
from summarize import summarize
volume = 0.0

# make capitalization combinations of lower and upper still be valid
def formatInput(choice):
    choice = choice.lower().strip()
    wordList = choice.split()
    choice = " ".join(wordList)
    return choice

# Lists for each shape
cubeList = []
pyramidList = []
ellipsoidList = []

# request choice of shape
# request test number so it will print according to the test case number

testNumber = input("Enter a test number: ")

choice = str(input("Enter shape of interest (q/quit to terminate): "))
choice = formatInput(choice)

# this is incase the user presses q or quit right away, so must be out of loop
if choice == "quit":
    print("You have reached end of your session.")
    print("You did not perform any volume calculations.")

if choice == "q":
    print("You have reached end of your session.")
    print("You did not perform any volume calculations.")

# while loop for all cases
while choice != "quit" and choice != "q":
    choice = formatInput(choice)

    if choice == "c" or choice == "cube":
        c = int(input("Enter dimension of cube: "))
        volume = cubeVolume(c)
        cubeList.append(volume)

    elif choice == "p" or choice == "pyramid":
        b = int(input("Enter dimension of base: "))
        h = int(input("Enter dimension of height: "))
        volume = pyramidVolume(b, h)
        pyramidList.append(volume)

    elif choice == "e" or choice == "ellipsoid":
        r1 = int(input("Enter radius 1 of ellipsoid: "))
        r2 = int(input("Enter radius 2 of ellipsoid: "))
        r3 = int(input("Enter radius 3 of ellipsoid: "))
        volume = ellipsoidVolume(r1, r2, r3)
        ellipsoidList.append(volume)

# needs validation
    else:
        print("Invalid input.")

    choice = str(input("Enter shape of interest (q/quit to terminate): "))

# sort the lists before using the function summarize
cubeList.sort()
pyramidList.sort()
ellipsoidList.sort()

print(cubeList)
print(pyramidList)
print(ellipsoidList)

summarize(cubeList, pyramidList, ellipsoidList, testNumber)
