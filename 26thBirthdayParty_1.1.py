""" 26thBirthdayParty_1.1.py
    This program creates a list of invitees to a birthday party
    by pulling data from 26thBirthdayParty_AttendanceList.
    Each indexed invitee is a dictionary with information about their name and attendance status.
"""

# import pertinent modules
import json
import time
# variable for delay time
t = 1

# print title of the program
print(" ")
print("*******ALAN'S 26TH BIRTHDAY PARTY LIST*******")
print(" ")
time.sleep(t)
print("WELCOME!")
print("")
time.sleep(t)
print("")
print("")


# import data from 26thBirthdayParty_AttendanceList_1.2.txt
# create inviteList
inviteList = []
# store attendance list data line by line
with open("26thBirthdayParty_AttendanceList_1.3a.txt") as f:
    data = f.readline()
    while data:
        # strip trailing newline
        newData = data.strip('\n')
        inviteeRaw = newData.split(maxsplit=1)
        for i in inviteeRaw:
            invitee = {"name": str(
                inviteeRaw[0]), "status": str(inviteeRaw[1])}
        inviteList.append(invitee)
        data = f.readline()
# print(inviteList)
# print("")


# function that prints the attendance status of each invitee
def statusReport(n):
    print("STATUS REPORT:")
    print(" ")
    for item in n:
        print("%s: %s" % (item["name"], item["status"]))
    return ""

# function that prints the attendance list
def attendanceList(n):
    print("ATTENDANCE LIST:")
    print(" ")
    for item in n:
        if item["status"] == "attending":
            print("%s: %s" % (item["name"], item["status"]))
    return ""

# count the number of invitees in attendance


def attendanceCount(n):
    totalAttending = 0
    for item in n:
        if item["status"] == "attending":
            totalAttending += 1
    return totalAttending


# intitialize variable for while loop to run program
finished = False
while finished == False:

    # give the user their options
    print("To view the attendance list, type \'Attendance List\' then hit Enter.")
    print("To view a status report on the invite list, type \'Status Report\' then hit Enter.")
    print("To add an invitee, type \'add\' then hit Enter.")
    print("To edit an invitee, type \'edit\' then hit Enter.")
    print("To exit the program, type \'exit\' then hit Enter.")
    print("")
    response = input("What would you like to do? ")
    print("")

    # code for printing the Attendance List
    if response == "Attendance List":
        print("")
        print(attendanceList(inviteList))

    # code for printing a Status Report
    elif response == "Status Report":
        print("")
        print(statusReport(inviteList))

    # code for adding someone to the invite list
    elif response == "add":
        print("")
        newInvitee = {"name": "a", "status": "b"}
        nameInput = input("Type the new invitee's name, then hit Enter: ")
        newInvitee["name"] = nameInput
        stillImporting = True
        while stillImporting:
            statusInput = input(
                "Type the new invitee's attendance status, then hit Enter (pending, attending, or can't go): ")

            # code for catching an invalid attendance status
            if statusInput == "pending" or statusInput == "attending" or statusInput == "can't go":
                newInvitee["status"] = statusInput
                inviteList.append(newInvitee)
                newInvitee = newInvitee["name"]  # might not be valid syntax
                print("")
                print("Your new invitee has been successfully added!")
                time.sleep(t)
                print("")
                print("")
                stillImporting = False
            else:
                print("")
                print("Please input a valid attendance status.")

    #code for editing the Invite List
    elif response == "edit":
        editing = True
        while editing == True:
            editInput = input("Please enter the name of the invitee you'd like to edit, then hit 'Enter' or enter 'cancel': ")
            print("")
            print("You've selected '%s'." % (editInput))
            found = False
            for dictionary in inviteList:
                if dictionary["name"] == editInput:
                    found = True
            
            #if invitee has been found somewhere in the list
            if found == True:
                print("")
                updating = True
                while updating == True:
                    target = input("What would you like to edit? Type 'name' or 'status', then hit 'Enter' or enter 'cancel': ")
                    print("")

                    #edit invitee name
                    if target == "name":
                        newName = input("Enter the new name to replace %s, or enter 'cancel': " % (editInput))
                        print("")
                        if newName == 'cancel':
                            print("Editing cancelled.")
                        else:
                            for dictionary in inviteList:
                                if dictionary["name"] == editInput:
                                    dictionary["name"] = newName
                            print("Your invitee's name has been successfully updated!")
                        updating = False
                    #edit invitee status
                    elif target == "status":
                        for dictionary in inviteList:
                            if dictionary["name"] == editInput:
                                oldStatus = dictionary["status"]
                                stillImporting = True
                                while stillImporting == True:
                                    newStatus = input("Enter the new status to replace '%s', or enter 'cancel': " % (oldStatus))
                                    print("")
                                    # code for catching an invalid attendance status
                                    if newStatus == "pending" or newStatus == "attending" or newStatus == "can't go":
                                        dictionary["status"] = newStatus
                                        stillImporting = False
                                    elif newStatus == "cancel":
                                        print("Editing cancelled.")
                                        stillImporting = False
                                    else:
                                        print("")
                                        print("Please input a valid attendance status.")
                        print("Your invitee's status has been successfully updated!")
                        updating = False
                    #cancel updating
                    elif target == 'cancel':
                        print("Editing cancelled.")
                        updating = False
                    else:
                        print("")
                        print("Please input a valid response.")
                editing = False

            #cancel editing
            elif editInput == 'cancel':
                print("Editing cancelled.")
                editing = False
            #invitee not found
            else:
                print("")
                print("Invitee not found.")
        print("")
        print("")

    # code for exiting the program
    elif response == "exit":
        print("")
        wrappedUp = False
        while wrappedUp == False:
            saveInput = input(
                "Save changes? type 'yes' or 'no' then hit Enter. ")
            # code for saving changes
            if saveInput == 'yes':
                with open("26thBirthdayParty_AttendanceList_1.3a.txt", "w") as f:
                    # code to properly format inviteList in string format
                    for invitee in inviteList:
                        savedData = ("%s %s" % (invitee["name"], invitee["status"]))
                        f.write(savedData + "\n")

                print("")
                print("Your changes have been successfully saved!")
                print("")
                wrappedUp = True
            elif saveInput == 'no':
                print("")
                wrappedUp = True
            else:
                print("Please input a valid response.")

        print ("Exiting program. Goodbye!")
        print ("")
        finished = True
    else:
        print("")
        print ("Please input a valid response.")
        time.sleep(1)
        print("")



# report who's coming
"""print (statusReport(inviteList))
print ("")

# report the attendance count
print ("ATTENDANCE COUNT:")
print ("")
print ("Total attending: %s" % (attendanceCount(inviteList)))
print ("")"""
