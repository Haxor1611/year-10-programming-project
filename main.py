# tasks
import random
import time
import json

# example for the program

caseIds = [2243, 3432, 7645, 8768]
with open("keywords.json", "r") as f:
    keywordString = f.read()
    f.close()
with open("solutions.json", "r") as j:
    solutionString = j.read()
    j.close()

keywords = json.loads(keywordString)

solutions = json.loads(solutionString)


# generating the case id
def caseIdGenerate(IDS):
    # getting a random integer
    caseID = random.randint(1, 9999)
    # making sure its not in the ids
    if caseID not in IDS:
        # adding to the list
        IDS.append(caseID)
        return caseID
    else:
        # recursion
        caseIdGenerate(IDS)


def task1():
    print("Welcome to Mobile Trouble shooting guide.")
    time.sleep(1)
    choice = input("Is the phone overheating?")
    if choice == "yes":
        print(solutions["overheating"])
    else:
        choice1 = input("Has the phone been dropped in water?")
        if choice1 == "yes":
            print(solutions["wet"])
        else:
            choice2 = input("Have you dropped the phone?")
            if choice2 == "yes":
                print(solutions["dropped"])
            else:
                choice3 = input("Are your apps loading?")
                if choice3 == "yes":
                    print(solutions["apps"])
                else:
                    choice4 = input("Is your screen not responding?")
                    if choice3 == "yes":
                        print(solutions["screen"])
                    else:
                        choice5 = input("Is the phone not turning on?")
                        if choice3 == "yes":
                            print(solutions["power"])
                        else:
                            choice6 = input("Is your phone slow?")
                            if choice3 == "yes":
                                print(solutions["slow"])
                            else:
                                choice7 = input("Is the battery running out?")
                                if choice3 == "yes":
                                    print(solutions["battery"])
                                else:
                                    choice8 = input("Is the storage full?")
                                    if choice3 == "yes":
                                        print(solutions["storage"])
                                    else:
                                        choice9 = input("Is the phone freezing?")
                                        if choice3 == "yes":
                                            print(solutions["freezes"])


def task2(question):
    found = False
    arr = question.split()
    print(arr)

    # looping through the array of words from the question
    for i in range(0, len(arr)):
        # looping through the array of keywords
        for k in range(0, len(keywords)):
            # checking if our word is in the list of keywords
            if arr[i] == keywords[k]:
                # giving the solution
                print(solutions[keywords[k]])
                found = True
                return solutions[keywords[k]]
    if not found:
        # no solution found
        print("There is no current solution to this problem.")
        found = True
        return "No Solution"


def task3():
    rep = report()
    rep.Device = input("What device is it?")
    rep.Brand = input("What brand is the phone?")
    rep.Model = input("What model is the phone?")
    rep.Version = input("What version is this phone?")
    rep.Memory = input("How much memory does this phone have?")
    rep.Problem = input("What is your problem?")
    rep.Solution = task2(rep.Problem)
    rep.caseID = caseIdGenerate(caseIds)


class report:
    def __init__(self, Device, Brand, Model, Version, Memory, Problem, Solution, caseID):
        self.Device = Device
        self.Brand = Brand
        self.Model = Model
        self.Version = Version
        self.Memory = Memory
        self.Problem = Problem
        self.Solution = Solution
        self.caseID = caseID


task2()
