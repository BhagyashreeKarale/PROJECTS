import json
import os.path
from pickle import TRUE
import re
from datetime import datetime
from time import strftime
# now = datetime.now()
largeSpots=0
compactSpots=0
motorcycleSpots=0
from simplejson import load
login="unsuccessful"
adminfile = "adminData.json"
username=""

##################################################################################################################
def lotDetails():
    levels=int(input("Enter number of levels:\n"))
    parkingLot=[]
    for i in range(levels):
        element={}
        print("Details for LEVEL",i+1)
        element["level"]=str(i+1)
        global largeSpots ,compactSpots,motorCycleSpots
        largeSpots=int(input("Enter number of large spots:\n"))
        compactSpots=int(input("Enter number of compact spots:\n"))
        motorCycleSpots=int(input("Enter number of motorcycle spots:\n"))
        element["largeSpots"]=[{}for i in range(largeSpots)]
        element["largeSpots"].insert(0,largeSpots)
        element["compactSpots"]=[{}for i in range(compactSpots)]
        element["compactSpots"].insert(0,compactSpots)
        element["motorcycleSpots"]=[{}for i in range(motorCycleSpots)]
        element["motorcycleSpots"].insert(0,motorCycleSpots)
        parkingLot.append(element)
    return parkingLot

##################################################################################################################

def loads(filename):
    with open(filename,"r") as targetfile:
        jsonData=targetfile.read()
        pythonData=json.loads(jsonData)
        return pythonData

##################################################################################################################

def checkexisting_id(username):
    with open(adminfile,"r") as jsonFile:
        jsonData=jsonFile.read()
        pythonData=json.loads(jsonData)
        for i in pythonData:
            if i["username"] == username:
                return True
        return False

##################################################################################################################

def isStrongPassword(pw):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"
    match_re = re.compile(reg)
    res = re.search(match_re, pw)
    if res:
        return True
    else:
        return False

##################################################################################################################

def dumping(data):
    with open (adminfile,"w" ) as file:
        json.dump(data,file,indent=2)

##################################################################################################################

def checkexisting_pwd(pwdinput):
    with open(adminfile,"r") as file:
        data=file.read()
        data1=json.loads(data)
        for i in data1:
            if i["password"] == pwdinput:
                return True
        return False

##################################################################################################################

def adminLogin(idinput):
    if checkexisting_id(idinput)==False:
            data=createAccount()
            if data!= None:
                with open(adminfile,"r")as jsonFile:
                    jsonData=jsonFile.read()
                    pythonData=json.loads(jsonData)
                    pythonData.append(data)
                    dumping(pythonData)
                loginRedirect()
    else:
        pwdinput=input("Enter password :\n")
        if checkexisting_pwd(pwdinput) == True:
                print("Login successfull.")
                global login
                login="successfull"

        else:
            print("Incorrect password.")

##################################################################################################################

def createAccount():
    account={}
    accountCreateRedirect=input("Account doesn't exist.Do you want to create a new account?(y/n)")
    if accountCreateRedirect=="y" or accountCreateRedirect=="Y":
        global username
        username = input("Enter username with which you want to create an account:\n")
        password = input("Enter a strong password:\n(It should contain least one capital letter, one number and one special character. Also make sure the length of the password is between 8 and 18.")
        if isStrongPassword(password)==True:
                account["username"]=username
                account["password"]=password
                print("Account created successfully.\nPlease provide following lot details to manage parking system at your location.\n")
                main_data=lotDetails()
                account["lotDetails"]=main_data
                print("Details registered successfully.")
                return account
        else:
            flag=False
            while flag==False:
                print("Not strong enough.Please create a new password")
                password = input("Enter a strong password:\n(It should contain least one capital letter, one number and one special character. Also make sure the length of the password is between 8 and 18.")
                if isStrongPassword(password)==True:
                    flag=True
                    account["username"]=username
                    account["password"]=password
             
                    print("Account created successfully.\nPlease provide following lot details to manage parking system at your location.\n")
                    main_data=lotDetails()
                    account["lotDetails"]=main_data
                    print("Details registered successfully.")
                    return account

    else:
        print("Thank you for visiting Parking Management System!")

##################################################################################################################

def loginRedirect():
    loginRedirect = input("Do you want to return to the loginpage(y/n)?\n")
    if loginRedirect=="Y" or loginRedirect=="y":
            id = input("Welcome to BK Parking Management System!Please login to authenticate your access\nEnter your username:\n")
            adminLogin(id)
    else:
        print("Thank you for visiting BK Parking Management System!\nHave a good time :)")

##################################################################################################################

def park(vtype,vehicleDetails):
    spotList=["largeSpots","compactSpots","motorcycleSpots"]
    data=loads(adminfile)
    main = [elem for elem in data if elem["username"]==username]
    for i in main[0]["lotDetails"]:
        if i[spotList[int(vtype)-1]][0]>0:
            for j in i[spotList[int(vtype)-1]][1:]:
                if len(j)==0:
                    slotNumber=i[spotList[int(vtype)-1]].index(j)
                    levelNumber=i["level"]
                    print("Level",levelNumber,"Slot number",slotNumber)
                    vehicleDetails["slotNumber"]=slotNumber
                    vehicleDetails["levelNumber"]=levelNumber
                    i[spotList[int(vtype)-1]][slotNumber]=vehicleDetails
                    i[spotList[int(vtype)-1]][0]-=1
                    dumping(data)
                    print("Here is your receipt:")
                    for i in vehicleDetails:
                        print("----------------------------------------------------")
                        print(i,":",vehicleDetails[i])
                        print("____________________________________________________")
                    return "Slot found."
    return "No slots found"

##################################################################################################################

def unPark(vtype,slotNumber,levelNumber):
    spotList=["largeSpots","compactSpots","motorcycleSpots"]
    data=loads(adminfile)
    if levelNumber not in range(1,len(data[0]["lotDetails"])+1):
        return ("Wrong level number entered")
    if slotNumber not in range(1,len(data[0]["lotDetails"][levelNumber-1][spotList[vtype-1]])):
        return ("Wrong slot number entered")
    if (len(data[0]["lotDetails"][levelNumber-1][spotList[vtype-1]][slotNumber])) == 0 :
        return("Please check your slot number and level number\nNo car found at the location you mentioned")
    else:
        checkinTime=data[0]["lotDetails"][levelNumber-1][spotList[vtype-1]][slotNumber]["checkinTime"]
        checkinDate=data[0]["lotDetails"][levelNumber-1][spotList[vtype-1]][slotNumber]["checkinDate"]
        data[0]["lotDetails"][levelNumber-1][spotList[vtype-1]][slotNumber]={}
        data[0]["lotDetails"][levelNumber-1][spotList[vtype-1]][0]+=1
        now = datetime.now()
        checkoutTime=now.strftime("%H:%M:%S")
        checkoutDate=now.strftime("%d/%m/%Y")
        diff=datetime.strptime(checkoutDate+" "+checkoutTime,"%d/%m/%Y %H:%M:%S")-datetime.strptime(checkinDate+" "+checkinTime,"%d/%m/%Y %H:%M:%S")
        seconds=int(diff.total_seconds())
        minutes=int(diff.total_seconds()/60)
        hours=int(minutes/60)
        print("Your parking time:",hours,"hour/s",minutes,"minutes",seconds,"seconds")
        print("       Please pay:",minutes*2,"RS at the exit")
        dumping(data)
        return ("You can now unpark your car and proceed to the payment at the exit.\nTHANK YOU")

##################################################################################################################

def main():
    global username
    username = input("Welcome to BK Parking Management System!Please login to authenticate your access\nEnter your username:\n")
    if os.path.exists(adminfile)==True:
        adminLogin(username)
    else:
        x=createAccount()
        if x != None:
            dumping([x])
            loginRedirect()
    if login=="successfull":
        userFlag=True
        while userFlag==True:
            signout=input("You are currently logged in as "+username+"\nPress Q to signout\nPress F to move forward\n")
            if signout=="Q" or signout=="q":
                print("Thank you for visiting BK Parking Management System!\nHave a good time :)")
                break
            vehicles=["Bus","Car","Motorcycle"]
            if login=="successfull":
                vehicleDetails={}
                action=input("Press 1 to park a vehicle\nPress 2 to unpark a vehicle\n")
                vehicleType=int(input("Enter vehicle type\n1.Bus\n2.Car\n3.Motorcycle\n"))
                if vehicleType not in range(1,4):
                    print("Invalid input")
                    break
                if action=="1":
                    vehicleNumber=input("Enter vehicle number:\n")
                    vehicleDetails["vehicleType"]=vehicles[int(vehicleType)-1]
                    vehicleDetails["vehicleNumber"]=vehicleNumber
                    now = datetime.now()
                    vehicleDetails["checkinTime"]=now.strftime("%H:%M:%S")
                    now = datetime.now()
                    vehicleDetails["checkinDate"]=now.strftime("%d/%m/%Y")
                    print("Checking for slot availability.Please be patient.")
                    print(park(vehicleType,vehicleDetails))
                elif action=="2":
                    levelNumber=int(input("Enter your level number please:\n"))
                    slotNumber=int(input("Enter your slot number please:\n"))
                    result=unPark(vehicleType,slotNumber,levelNumber)
                    print(result)

##################################################################################################################

main()
