# tasks
import random
import time
import json


# example for the program

def readJsonIntoDict(file):
    with open(file, "r") as f:
        fileString = f.read()
        f.close()
    return json.loads(fileString)


keywords = readJsonIntoDict("keywords.json")
solutions = readJsonIntoDict("solutions.json")
caseIds = readJsonIntoDict("IDS.json")


# generating the case id
def caseIdGenerate(IDS):
    # getting a random integer
    caseID = random.randint(1, 9999)
    # making sure it's not in the ids
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
    if choice.lower() == "yes":
        print(solutions["overheating"])
    else:
        choice1 = input("Has the phone been dropped in water?")
        if choice1.lower() == "yes":
            print(solutions["wet"])
        else:
            choice2 = input("Have you dropped the phone?")
            if choice2.lower() == "yes":
                print(solutions["dropped"])
            else:
                choice3 = input("Are your apps loading?")
                if choice3.lower() == "yes":
                    print(solutions["apps"])
                else:
                    choice4 = input("Is your screen not responding?")
                    if choice4.lower() == "yes":
                        print(solutions["screen"])
                    else:
                        choice5 = input("Is the phone not turning on?")
                        if choice5.lower() == "yes":
                            print(solutions["power"])
                        else:
                            choice6 = input("Is your phone slow?")
                            if choice6.lower() == "yes":
                                print(solutions["slow"])
                            else:
                                choice7 = input("Is the battery running out?")
                                if choice7.lower() == "yes":
                                    print(solutions["battery"])
                                else:
                                    choice8 = input("Is the storage full?")
                                    if choice8.lower() == "yes":
                                        print(solutions["storage"])
                                    else:
                                        choice9 = input("Is the phone freezing?")
                                        if choice9.lower() == "yes":
                                            print(solutions["freezes"])
                                        else:
                                            print("No solutions found.")


def task2(question):
    question = question.lower()
    arr = question.split()
    sols = []
    # looping through the array of words from the question
    for i in range(0, len(arr)):
        # looping through the array of keywords
        for k in range(0, len(keywords)):
            # checking if our word is the current keyword we are currently iterating over.
            if arr[i] == keywords[k]:
                # giving the solution

                sols.append(solutions[keywords[k]])
                continue

    if len(sols) == 0:
        # no solution found
        return "No Solution"
    else:
        print(len(sols), " solutions found! Printing the solution/s now. \n")
        # adds all the solutions found
        return "\n".join(sols)


def task3():
    # init our class
    rep = Report(input("What device is it?"), input("What brand is the phone?"), input("What model is the phone?"),
                 input("What version is this phone?"), input("How much memory does this phone have?"),
                 input("What is your problem?"), caseIdGenerate(caseIds))
    # print solution
    print(rep.getSolution())
    if writeJson("report.json", rep):
        writeCase()
        print("Sent to a technician!")


class Report:
    # function gets called as soon as we use the class, so we can assign it values
    def __init__(self, Device, Brand, Model, Version, Memory, Problem, caseID):
        self.Device = Device
        self.Brand = Brand
        self.Model = Model
        self.Version = Version
        self.Memory = Memory
        self.Problem = Problem

        self.caseID = caseID

    def getSolution(self):
        # gives us our solution
        return task2(self.Problem)


# putting our report object into serialized json data. to be sent 'to a technician'

def writeJson(fileToWrite, report):
    with open(fileToWrite, "a") as ftw:
        jsonDump = json.dumps(report.__dict__)

        ftw.writelines(jsonDump + "\n")
        ftw.close()
        return True


def writeCase():
    # writes our current case id to the case ids json file
    with open("ids.json", "w") as file:
        # empties the file first
        file.truncate()
        file.write(str(caseIds))
        file.close()


task3()
