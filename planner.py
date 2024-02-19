import os

def getLines():
    with open('planner.txt') as file:
        lines = [line.strip() for line in file]
    return lines

# Function to print incomplete tasks into their groups.
def displayList(lines):
    os.system("cls")
    finished = 0
    unfinished = 0
    groups = {}
    print("\nYour Tasks:")
    for num in range(len(lines)):
        line = lines[num]
        if len(line.split(";GROUP: ")) == 2:
            unfinished += 1
            lineList = line.split(";GROUP: ")
            try:
                groups[lineList[1]].append([num, lineList[0]])
            except:
                groups[lineList[1]] = [[num, lineList[0]]]
        else:
            unfinished += 1
            try:
                groups["Other"].append([num, line])
            except:
                groups["Other"] = [[num, line]]
    if groups:
        for group in groups:
            if group != "Other":
                print("\n" + group + ":")
                for task in groups[group]:
                    if task[1][0] != "#":
                        num = task[0]
                        desc = task[1]
                        print(" "*(3-len(str(num))) + str(num), desc)
        try:
            print("\nOther:")
            for task in groups["Other"]:
                if task[1][0] != "#":
                    num = task[0]
                    desc = task[1]
                    print(" "*(3-len(str(num))) + str(num), desc)
        except:
            pass
    if finished == len(lines):
        print("You have no tasks.")
    return groups

# This function takes all of the existing groups as a parameter.
# The function can be cancelled at any time by entering "x" or "cancel".
def add(groups):
    print()
    line = []
    # Fisrt, the program sees if the task that he user wants to be added is related to my A-Levels (this system primarily existed to store A-Level related tasks).
    # If so, the program will tailor the next input prompts for the subject. 
    subject = input("Subject? (f/mat/maths) OR (ch/chem) OR (cs/co/comp) OR (n/none) OR (x/cancel)\n")
    if subject in ["f","mat","maths"]:
        #FMat
        line.append("FMat")
        teacher = input("Teacher? (b/black) OR (c) OR (h/hutch) OR (n/none) OR (x/cancel)\n")
        if teacher in ["b","black"]:
            line.append("Ms B")
        elif teacher in ["c"]:
            line.append("Mr C")
        elif teacher in ["h","hutch"]:
            line.append("Mr H")
        elif teacher in ["","n","none"]:
            line.append("----")
        elif teacher in ["x","cancel"]:
            return
        else:
            line.append("????")
    
    elif subject in ["ch","chem"]:
        #Chem
        line.append("Chem")
        teacher = input("Teacher? (w/wim/wimbridge) OR (l/lowe) OR (n/none) OR (x/cancel)\n")
        if teacher in ["w","wim","wimbridge"]:
            line.append("Ms W")
        elif teacher in ["l","lowe"]:
            line.append("Mr L")
        elif teacher in ["","n","none"]:
            line.append("----")
        elif teacher in ["x","cancel"]:
            return
        else:
            line.append("?")

    elif subject in ["cs","co","comp"]:
        #Comp
        line.append("Comp")
        teacher = input("Teacher? (k/keen) OR (m/manning) OR (n/none) OR (x/cancel)\n")
        if teacher in ["k","keen"]:
            line.append("Mr K")
        elif teacher in ["m","manning"]:
            line.append("Mr M")
        elif teacher in ["","n","none"]:
            line.append("----")
        elif teacher in ["x","cancel"]:
            return
        else:
            line.append("?")
    
    elif subject in ["","n","none"]:
        task = input("Task? (x/cancel)\n")
        if task in ["","x","cancel"]:
            return
        else:
            line.append(task)
    elif subject in ["x","cancel"]:
        return
    else:
        # Invalid subject
        line.append("???? ????")

    # If the task is A-Level related ask for more specification to save time typing out that it is a revision task or other common tasks.
    if subject in ["f","mat","maths", "ch","chem", "cs","co","comp"]:
        taskType = input("Type of task? (r/revise) OR (hw/homework) OR (w/wu/write up) OR (n/none) OR (x/cancel)\n")
        if taskType in ["r","revise"]:
            line.append("Revise:")
        elif taskType in ["hw","homework"]:
            line.append("H/W:")
        elif taskType in ["w","wu","write up"]:
            line.append("Write up:")
        elif taskType in ["","n","none"]:
            pass
        elif taskType in ["x","cancel"]:
            return
        else:
            pass
        
        # Task description
        task = input("Task? (n/none) OR (x/cancel)\n")
        if task in ["","n","none"]:
            pass
        elif task in ["x","cancel"]:
            return
        else:
            line.append(task)

        dueDate = input("\nDue date? (n/none) OR (x/cancel)\n")
        if dueDate in ["","n","none"]:
            pass
        elif dueDate in ["x","cancel"]:
            return
        else:
            line.append(dueDate)

        groupNum = input("\nWhich school group would you like to add to?\n1: Long Term.\n2: Short Term.\n")
        if groupNum in ["1", "2"]:
            line.append(";GROUP: School" + groupNum)

        return " ".join(line)

    # If the task is not related to A-Levels see if it belongs to a group, process grouping, and return the new line.
    groupList = [group for group in groups]
    groupString = "Existing groups are: " + ", ".join(groupList)
    addToExistingGroup = input("\nWould you like to add to an existing group? (y/n) OR (x/cancel)\n" + groupString + "\n")
    if addToExistingGroup == "y":
        for num, group in enumerate(groups):
            print(" "*(2-len(str(num))) + str(num), group)
        groupEntered = False
        while groupEntered == False:
            groupNum = input("\nWhat group would you like to add to? (*index of group*)\n")
            try:
                line.append(";GROUP: " + list(groups)[int(groupNum)])
                groupEntered = True
            except:
                print("Error...")
    elif addToExistingGroup == "n":
        group = input("\nName the new group? (*enter anything*) OR (n/none) OR (x/cancel)\n")
        if group in ["","n","none"]:
            pass
        elif group in ["x","cancel"]:
            return
        else:
            line.append(";GROUP: " + group)
    elif addToExistingGroup in ["x","cancel"]:
        return

    return " ".join(line)

# Updates lines to not have the line with the inputted number
def finish(lines):
    print()
    try:
        num = int(input("What is the number of the task you have finished\n"))
        lines[num] = "# " + lines[num]
    except:
        pass
    return lines

# Saves the inputted lines
def save(lines):
    with open("planner.txt","w") as file:
        file.write("\n".join(lines))

def menu():
    lines = getLines()
    while True:
        groups = displayList(lines)
        choice = input("\n\nHow would you like to edit the list? (a/add) OR (f/finish) OR (x/exit)\n\n")
        lines = getLines()
        if choice in ["a","add"]:
            # This function composes a line from user inputs in the terminal and returns it
            line = add(groups)
            if line:
                lines.append(line)
        elif choice in ["f","finish"]:
            # This function takes all of the lines and returns them without the line number that the user requests to be removed in the terminal
            lines = finish(lines)
        elif choice in ["x","exit"]:
            # End the while loop so lines get saved
            break
        save(lines)

menu()