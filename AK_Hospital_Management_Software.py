AId="AK"
APass="Tiger"

#-------------------------------------------SAJAVAT-----------------------------------------------
print('                                          :::         :::    :::                                  ' )
print('                                        :+: :+:       :+:   :+:                                    ')
print('                                       +:+   +:+      +:+  +:+                                     ')
print('                                      +#++:++#++:     +#++:++                                      ')
print('                                      +#+     +#+     +#+  +#+                                     ')
print('                                      #+#     #+# #+# #+#   #+#  #+#                               ')
print('                                     ###     ### ### ###    ### ###')
print("\n"*2)
print('          :::    :::  ::::::::   ::::::::  ::::::::: ::::::::::: ::::::::::: :::     :::        ')
print('          :+:    :+: :+:    :+: :+:    :+: :+:    :+:    :+:         :+:   :+: :+:   :+:        ')
print('          +:+    +:+ +:+    +:+ +:+        +:+    +:+    +:+         +:+  +:+   +:+  +:+        ')
print('          +#++:++#++ +#+    +:+ +#++:++#++ +#++:++#+     +#+         +#+ +#++:++#++: +#+        ')
print('          +#+    +#+ +#+    +#+        +#+ +#+           +#+         +#+ +#+     +#+ +#+        ')
print('          #+#    #+# #+#    #+# #+#    #+# #+#           #+#         #+# #+#     #+# #+#        ')
print('          ###    ###  ########   ########  ###       ###########     ### ###     ### ########## ')
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
def BillSajavat():
    print("\n\n")
    print("""           ::::::::::    :::::::::   :::::::::::   :::          :::        
                        :+:    :+:      :+:       :+:          :+:        
                        +:+    +:+      +:+       +:+          +:+        
                        +#++:++#+       +#+       +#+          +#+        
                        +#+    +#+      +#+       +#+          +#+        
                        #+#    #+#      #+#       #+#          #+#        
                        #########   ###########   ##########   ##########"""  )
import pickle
import os
import time

class Patient:
    def __init__(self):
        self.pid = "xyz"
        self.pas = "0000"
        self.name ="abc"
        self.age = 00
        self.gender = "Male"
        self.disease = "jkl"
        self.Day = 00
        self.Date = "0-00-0000"
        self.Add ="abcdefgh"
        self.Ph = "0123456789"
    def patient(self):
        self.pid = str(input("Enter Patient's Email ID\t\t\t:"))
        self.pas = str(input("Enter The Password\t\t\t\t:"))
        self.name = str(input("Enter Your Name\t\t\t\t\t:"))
        self.age = int(input("Enter Your Age\t\t\t\t\t:"))
        self.gender = str(input("Enter Your Gender\t\t\t\t:"))
        self.disease = str(input("Enter Your Disease\t\t\t\t:"))
        self.Day = int(input("Enter No. Of Days Of Disease\t\t\t:"))
        self.Date = str(input("Enter Todays Date(dd-mm-yyyy)\t\t\t:"))
        self.Add = str(input("Enter Your Address\t\t\t\t:"))
        self.Ph = str(input("Enter Your Phone Number\t\t\t\t:"))
        print("\n")
        self.condition()
        if( self.condi=="SERIOUS!!!!"):
            print("\tYOU NEED TO ADMIT IMMEDIATELY!!!!")
            self.room()
            
    def condition(self):
        if(self.Day<=3):
            self.condi ="POOR"
        if(self.Day>3 and self.Day<=10):
            self.condi = "VERY POOR"
        if(self.Day>10):
            self.condi = "SERIOUS!!!!"
                
    def show(self):
        print("\t\t|DETAILS OF PATIENT|")
        print("\t\t","^"*20)
        print ("Patient's ID Is \t\t\t:",self.pid)
        print ("Password Is\t\t\t:","*"*len(self.pas))
        print ("Name Is\t\t\t\t:",self.name)
        print ("Age Is\t\t\t\t:",self.age)
        print ("Gender Is\t\t\t:",self.gender)
        print ("Disease Is\t\t\t:",self.disease)
        print ("Address Is\t\t\t:",self.Add)
        print ("Phone No. Is\t\t\t:",self.Ph)
        print ("Condition Is\t\t\t:",self.condi)
        print ("Room Cost Is\t\t\t:",self.cost)

    def showBed(self):
        print("Patient ID\t\t\tBed Type\t\tRoom No.\tDisease\tDoctor")
        print (self.pid,"\t\t\t",self.c)




class Doctor :
    def __init__(self):
        self.DrID="null"
        self.Pass="null"
        self.Name="null"
        self.Age=250
        self.Sex="null"
        self.Quali="null"
        self.Speci=0
        self.Fees=0
        self.Address="null"
        self.Phno=0
        self.Expe="null"
        self.Days="null"
        

    def InputDr(self):

        while True:
            self.DrID=str(input("\n\t\tEnter The Doctor ID \t\t\t: "))
            if self.Check1(self.DrID)!=0:
                self.DrID=self.DrID
                break
            else:
                print ("\n\t\t\tRe Enter ID and Password As ID Already Exist")
                continue
        
        self.Pass=str(input("\t\tEnter The Doctor Password \t\t: "))
        self.Name=str(input("\t\tEnter Doctor's Name \t\t\t: "))
        self.Age=int(input("\t\tEnter Doctor's Age \t\t\t: "))
        self.Sex=str(input("\t\tEnter Doctor's Gender (M/F) \t\t: "))
        self.Quali=str(input("\t\tEnter Doctor's Qualification\t\t: "))
        self.Speci=str(input("\t\tEnter Doctor's Speciality \t\t: "))
        self.Fees=int(input("\t\tEnter Doctor's Fees \t\t\t: "))
        self.Address=str(input("\t\tEnter Doctor's Address \t\t\t: "))
        self.Phno=int(input("\t\tEnter Doctor's Phone Number \t\t: "))
        self.Expe=str(input("\t\tEnter Doctor's Experience \t\t: "))
        self.Days=str(input("\t\tAvailability OF Doctor (M/W/F or T/T/S)\t: "))
        self.Time =str(input("\t\tEnter Doctor's Timings\t\t\t: ") )

    
    def Showdata(self):
        
        print ("\t\t", "_"*55)
        print("\n\t\t\t\t\tDETAILS")
        print ("\t\t", "_"*55)
        print("\n\t\t DOCTOR ID\t\t\t: ",self.DrID)
        print("\t\t DOCTOR'S NAME\t\t\t: ",self.Name)
        print("\t\t DOCTOR'S AGE\t\t\t: ",self.Age)
        print("\t\t DOCTOR'S GENDER\t\t: ",self.Sex)
        print("\t\t DOCTOR'S QUALIFICATION\t\t: ",self.Quali)
        print("\t\t DOCTOR'S SPECIALITY \t\t: ",self.Speci)
        print("\t\t DOCTOR'S FEES \t\t\t: ", self.Fees)
        print("\t\t DOCTOR'S ADDRESS\t\t: ",self.Address)
        print("\t\t DOCTOR'S PHONE NUMBER \t\t: ",self.Phno)
        print("\t\t DOCTOR'S EXPERIENCE \t\t: ", self.Expe)
        print("\t\t DOCTOR'S AVAILABLE DAYS\t: ",self.Days)
        

    def Showdata2(self):
        print( "\t",self.DrID, "\t\t\t", self.Name, "\t\t", self.Speci, "\t\t", self.Fees, "\t\t", self.Days)
    
    def Check1(self,ID):
            f=open("Doctor.txt", "rb")
            while True:
                try:
                    x=pickle.load(f)
                    if x.DrID==ID:
                        return 0
                except EOFError:
                    break
            f.close()
    
    def Doc(self):
        print("\t\t\t\t\t|DETAILS OF DOCTOR|")
        print("\t\t\t\t\t","^"*19)
        print
        print("\t\tNAME\t\t: ",self.Name,"\t\tDoctor ID\t: ",self.DrID)
        print
        print("\t\tQUALIFICATION   : ",self.Quali,"\t\tSPECIALITY\t: ",self.Speci)
        print("\n"*2)





class Emergency:
                
    def __init__(self):
        self.Status=None
        
    def patient(self):
        self.DrID=str(input("\n\t\tEnter The Doctor ID \t\t: "))
        self.Name = str(input("\t\tEnter Your Name\t\t\t: "))
        self.Disease = str(input("\t\tEnter Your Disease\t\t: "))
        self.Date = str(input("\t\tEnter Today's Date(dd-mm-yyyy)\t: "))
        self.Add = str(input("\t\tEnter Your Address\t\t: "))
        self.Status=str(input("\t\tEnter Your Status\t\t: "))
        self.Ph = str(input("\t\tEnter Phone Number\t\t: "))
        self.Bed=int(input("\t\tEnter The Bed Number \t\t: "))
            

    def Showdata2(self):
        print ("\t",self.Bed, "\t   ", self.Name, "\t", self.Date, "\t", self.Disease, "\t\t", self.Status,"\t", self.DrID)
        
    def Stat(self):
                    self.DrID=str(input("\n\t\tEnter The Doctor ID\t\t: "))
                    self.Status=str(input("\t\tEnter The New Status Of Patient\t:"))

    def show(self):
        print("\t\t|DETAILS OF PATIENT|")
        print("\t\t","^"*20)
        print ("\tName Is\t\t\t\t:",self.Name)
        print ("\tDisease Is\t\t\t:",self.Disease)
        print ("\tAddress Is\t\t\t:",self.Add)
        print ("\tPhone No. Is\t\t\t:",self.Ph)
        print ("\tCondition Is\t\t\t:",self.Status)
        print ("\tDate of ADDMISSION\t\t: ",self.Date)
        
                    

class Appointment :
    
    def __init__(self):
        self.DrID="null"
        self.Name="null"
        self.Address="null"
        self.Phno=0
        

    def InputDr(self,Phno,ID,Token,Date):
        self.Phno=Phno
        self.DrID=ID
        self.Date=Date
        self.Name=str(input("\t\tEnter Your Name \t\t\t: "))
        self.Address=str(input("\t\tEnter Your Address \t\t\t: "))
        self.Token=Token
    def Showdata(self):
        
        print ("\t", "_"*55)
        print("\n\t\t DETAILED INFORMATION")
        print("\t", "_"*55)
        print("\n\t DOCTOR ID\t\t\t= ",self.DrID,"\t",self.Pass)
        print("\t PATIENT'S NAME\t\t= ",self.Name)
        print("\t PATIENT'S ADDRESS\t= ",self.Address)
        print("\t PATIENT'S PHONE NUMBER \t= ",self.Phno)

    def Showdata2(self):
        print ("\t\t\t",self.Name, "\t\t", self.Phno, "\t\t", self.Token)
       
    
    def Check1(self,ID):
            f=open("Doctor.txt", "rb")
            while True:
                try:
                    x=pickle.load(f)
                    if x.DrID==ID:
                        return 0
                except EOFError:
                    break
            f.close()




   
#---------------------------------------Function-----------------------------------------------#

def Create():
    f=open("Doctor.txt","ab")
    D=Doctor()
    D.InputDr()
    pickle.dump(D,f)
    f.close()

def Show():
    f=open("Doctor.txt", "rb")
    while True:
        try:
            x=pickle.load(f)
            x.Showdata2()
        except EOFError:
            break
    f.close()

def Serch1():
    ch=str(input("\n\t\tEnter The Doctor ID \t\t: "))
    f=open("Doctor.txt", "rb")
    while True:
        try:
            x=pickle.load(f)
            if x.DrID==ch:
                x.Showdata()
                break
                
        except EOFError:
            break
    f.close()
        
def Dele():
    f1=open("Doctor.txt", "rb")
    f2=open("Temp.txt", "wb")
    ch=str(input("\n\t\tEnter Doctor ID to be Deleted\t: "))
    while True:
        try:
            x=pickle.load(f1)
            if x.DrID!=ch:
                pickle.dump(x,f2)
            elif x.DrID==ch:
                print ("\n\t\t\t\tDOCTOR IS REMOVED!!!!")
                print("\n\n\n")
            else:
                print ("\n\tDoctor ID Not Found")
        except EOFError:
            break
    f1.close()
    f2.close()
    os.remove("Doctor.txt")
    os.rename("Temp.txt","Doctor.txt")

def Update():
    f1=open("Doctor.txt", "rb")
    f2=open("Temp.txt", "wb")
    ch=str(input("\n\t\tEnter Doctor ID to be Updated\t: "))
    while True:
        try:
            x=pickle.load(f1)
            if x.DrID!=ch:
                pickle.dump(x,f2)
            if x.DrID==ch:
                x.InputDr()
                pickle.dump(x,f2)
            
        except EOFError:
            break
    f1.close()
    f2.close()
    os.remove("Doctor.txt")
    os.rename("Temp.txt","Doctor.txt")

def Check2(login,passw):
    f=open("Doctor.txt","rb")
    while True:
      try:
        a=pickle.load(f)
        if login==a.DrID and passw==a.Pass:
          return 0
        
      except EOFError:
        break
    f.close()


def Enter():
    f = open("Emergency.txt","ab")
    E = Emergency()
    E.patient()
    pickle.dump(E,f)
    f.close()


def Search(srch):
    f = open("Emergency.txt","rb")
    while True:
        try:
            a = pickle.load(f)
            if(a.Ph==srch):
                a.show()
                
                break
         
        except EOFError:
            break
    f.close()
    
def Deletion():
    f = open("Patient.txt","rb")
    f1 = open("temp.txt","wb")
    r = str(input("Enter the ID To Be Deleted"))
    while True:
        try:
            a = pickle.load(f)
            if(a.pid != r):
                pickle.dump(a,f1)
            elif(a.pid==r):
                print("ID REMOVED")
            else:
                print("ID NOT FOUND")
        except EOFError:
            break
    f.close()
    f1.close()
    os.remove("Patient.txt")
    os.rename("temp.txt","Patient.txt")
def Updation():
    f = open("Patient.txt","rb")
    f1 = open("temp.txt","wb")
    r = str(input("Enter Patient ID To Be Updated"))
    while True:
        try:
            a = pickle.load(f)
            if(a.pid != r):
                pickle.dump(a,f1)
            else:
                a.patient()
                pickle.dump(a,f1)
                
        except EOFError:
            break
    f.close()
    f1.close()
    os.remove("Patient.txt")
    os.rename("temp.txt","Patient.txt")
L=["E.N.T.","Cancer","Dental","Bone","Eye"]

def Search2():
    ch= int(input("\n\t\tEnter Your Choice\t\t: "))
    f= open("Doctor.txt","rb")
    print ("\n\tDoctor ID\t\tName\t\tSpeciality\t\tFees\tAvailability\n")
    while True:
        try:
            a = pickle.load(f)
            if(a.Speci==L[ch-1]):
                a.Showdata2()
                
                break
         
        except EOFError:
            break
    f.close()
def Dept():
    print ("\n\t\t\t\t1. E.N.T.")
    print ("\t\t\t\t2. Cancer")
    print ("\t\t\t\t3. Dental")
    print ("\t\t\t\t4. Bone")
    print ("\t\t\t\t5. Eye")


def Create2(Phno,ID,Token,Date):
    f=open("Appoint.txt","ab")
    A=Appointment()
    A.InputDr(Phno,ID,Token,Date)
    pickle.dump(A,f)
    f.close() 


def Check1(Phno):
    f=open("Appoint.txt", "rb")
    while True:
        try:
            x=pickle.load(f)
            if x.Phno==Phno:
              return 0
        except EOFError:
            break
    f.close()

def App(ID,Date):
    f=open("Appoint.txt", "rb")
    while True:
        try:
            x=pickle.load(f)
            if x.DrID==ID and x.Date==Date:
                x.Showdata2()
        except EOFError:
            break
    f.close()

def Check(ID):
    f=open("Doctor.txt", "rb")
    while True:
        try:
            x=pickle.load(f)
            if x.DrID==ID:
              return 0
        except EOFError:
            break
    f.close()

def Check3(ID,Date):
    Token=0
    f=open("Appoint.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            if x.DrID==ID and x.Date==Date:
                Token+=1
        except EOFError:
            break
    return Token

def Show2():
    f=open("Room.txt", "rb")
    print ("\n\t\t\tPatient's Phone Number\tNAME\t\tBED TYPE\tROOM NO\n")
    while True:
        try:
            x=pickle.load(f)
            print ("\t\t\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t",x[-1])
                            
        except EOFError:
            break
    f.close()

def Show3():
    f=open("Emergency.txt", "rb")
    print ("\n\tBed No\t Patient's Name\tDate\t\tDisease\t\tStatus\t   Doctor ID\n")
    while True:
        try:
            x=pickle.load(f)
            x.Showdata2()
                            
        except EOFError:
            break
    f.close()

def PatUP():
    f = open("Emergency.txt","rb")
    f1 = open("Temp.txt","wb+")
    r = str(input("\n\t\tPatient's Contact Number\t: "))
    while True:
        try:
            a = pickle.load(f)
            if(a.Ph != r):
                pickle.dump(a,f1)
            if a.Ph==r:
                a.Stat()
                pickle.dump(a,f1)
                print
                print("\t\t\t\tPATIENT'S CONDITION UPDATED")
                break
        except EOFError:
            break
    f.close()
    f1.close()
    os.remove("Emergency.txt")
    os.rename("Temp.txt","Emergency.txt")

def roomTest(pid):
    f = open("Room.txt","rb")
    while True:
        try:
            x = pickle.load(f)
            if(x[0]==pid):
                f.close()
                return True
                break
        except EOFError:
            break
    f.close()

def room(condi,Ph,name):
      f = open("Room.txt","ab")
      x=BedNo(Ph)
      while(True):
        if(condi=="Very Poor" or condi=="Serious"):
            print("\t\t\tYOU ARE ADVICED TO TAKE A ROOM")
            print("\n"*2)
            print("\t\t\t\tTYPE OF ROOMS ARE SHOWN BELOW")
            print
            print("\t\tRoom Type\t\tCost(PerDay)\t\tCODE")
            print("\t\tDELUX \t\t\t2000\t\t\t101")
            print("\t\tAC ROOM \t\t1500\t\t\t102")
            print("\t\tNON AC \t\t\t1000\t\t\t103")
            print
            if(condi=="Very Poor"):
                c = int(input("\n\tEnter The Code Of The Room\t\t:"))
                if(c==101):
                    if CheckD()<10:
                        print
                        print("\n\t\t\t   You Decided To Stay In DELUX ROOM")
                        cost = 2000*5
                        a = [Ph,name,c,x]
                        pickle.dump(a,f)
                        print
                        print ("\n\tRoom Cost Is\t\t\t:",cost)
                        break
                                                             
                    else:
                        print("\t\t\t\t\tSORRY !!!!")
                        print("\t\t\tDELUX Rooms Are FULL!!")
                        print("\t\tKINDLY TAKE ANOTHER TYPE OF ROOM")
                        continue
                        
                elif(c==102):
                    print
                    if CheckA()<10:
                        print
                        print("\n\t\t\t   You Decided To Stay In AC ROOM")
                        cost = 2000*5
                        a = [Ph,name,c,x]
                        pickle.dump(a,f)
                        print
                        print ("\n\tRoom Cost Is\t\t\t:",cost)
                        break
                                                             
                    else:
                        print("\t\t\t\t\tSORRY !!!!")
                        print("\t\t\tAC Rooms Are FULL!!")
                        print("\t\tKINDLY TAKE ANOTHER TYPE OF ROOM")
                        continue
                elif(c==103):
                    print
                    if CheckN()<10:
                        print
                        print("\n\t\t\t   You Decided To Stay In DELUX ROOM")
                        cost = 2000*5
                        a = [Ph,name,c,x]
                        pickle.dump(a,f)
                        print
                        print ("\n\tRoom Cost Is\t\t\t:",cost)
                        break
                                                             
                    else:
                        print("\t\t\t\t\tSORRY !!!!")
                        print("\t\t\tNON AC Rooms Are FULL!!")
                        print("\t\tKINDLY TAKE ANOTHER TYPE OF ROOM")
                        continue
                        
                else:
                    print("Enter The Correct Code")
            elif(condi=="Serious"):
                c = int(input("\tEnter The Code Of The Room\t\t: "))
                if(c==101):
                    if CheckD()<10:
                        print
                        print("\n\t\t\t   You Decided To Stay In DELUX ROOM")
                        cost = 2000*5
                        a = [Ph,name,c,x]
                        pickle.dump(a,f)
                        print
                        print ("\n\tRoom Cost Is\t\t\t:",cost)
                        break
                                                             
                    else:
                        print("\t\t\t\t\tSORRY !!!!")
                        print("\t\t\tDELUX Rooms Are FULL!!")
                        print("\t\tKINDLY TAKE ANOTHER TYPE OF ROOM")
                        continue
                elif(c==102):
                    print
                    if(CheckA()<10):              
                        print("\n\t\t\t   You Decided To Stay In AC ROOM")
                        cost = 2000*5
                        a = [Ph,name,c,x]
                        pickle.dump(a,f)
                        print
                        print( "\n\tRoom Cost Is\t\t\t:",cost)
                        break
                                                             
                    else:
                        print("\t\t\t\t\tSORRY !!!!")
                        print("\t\t\tAC Rooms Are FULL!!")
                        print("\t\tKINDLY TAKE ANOTHER TYPE OF ROOM")
                        continue
                elif(c==103):
                    print
                    if CheckN()<10:
                        print
                        print("\n\t\t\t   You Decided To Stay In DELUX ROOM")
                        cost = 2000*5
                        a = [Ph,name,c,x]
                        pickle.dump(a,f)
                        print
                        print ("\n\tRoom Cost Is\t\t\t:",cost)
                        break
                                                             
                    else:
                        print("\t\t\t\t\tSORRY !!!!")
                        print("\t\t\tNON AC Rooms Are FULL!!")
                        print("\t\tKINDLY TAKE ANOTHER TYPE OF ROOM")
                        continue
                        
                else:
                    print("\n\n\t\t\tEnter The Correct Code")
        else:
            print("You Dont Need A Room As Per Your CONDITION!!!!")
            break


def CheckD():
    count=0
    f=open("Room.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            count+=1
        except EOFError:
            break
    f.close()
    return count

def CheckA():
    count=0
    f=open("Room.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            for i in range(len(x)-1):
                if x[-2]==102:
                    count+=1
        except EOFError:
            break
    f.close()
    return count

def CheckN():
    count=0
    f=open("Room.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            for i in range(len(x)-1):
                if x[-2]==103:
                    count+=1
        except EOFError:
            break
    f.close()
    return count


def AdmissionE():
    ph=str(input("\n\tEnter The Patient's Phone Number\t: "))
    name = str(input("\tEnter Patient's Name\t\t\t: "))

    a =str(input("\n\tWant To Admit Patient(Y/N)\t\t: "))
    if(a in "Yy"):
        d = check5(ph)
        room(d,ph,name)
        DelBed(ph)
    else:
        
        BILL(ph)
        DelBed(ph)

   

def Serch(Dr):
    f=open("Doctor.txt", "rb")
    while True:
        try:
            x=pickle.load(f)
            if x.DrID==Dr:
                x.Doc()
                break
        except EOFError:
            break
    f.close()

def searchB(srch):
    f = open("Emergency.txt","rb")
    while True:
        try:
            a = pickle.load(f)
            if(a.Ph==srch):
                a.show()
                
                break
        except EOFError:
            break
    f.close()
def searchR(srch):
    f = open("Room.txt","rb")
    while True:
        try:
            a = pickle.load(f)
            if(a[0]==srch):
                return a[-2]
                
        except EOFError:
            break
    f.close()


def RoomCost(a):
    f = open("Room.txt","rb")
    while True:
        try:
                x = pickle.load(f)
                if(searchR(a)==101):
                    b = 2000*5
                    return b
                    break
                elif(searchR(a)==102):
                    b = 1500*5
                    return b
                    break
                elif(searchR(a)==103):
                    b = 1000*5
                    return b
                    break
                else:
                   return 0
        except EOFError:
            break

def BILL(ph):
    BillSajavat()
    print("\n"*2)
    b = str(input("\tEnter Discharge DATE\t: "))
    Dr = str(input("\tEnter Dr ID\t\t: "))
    searchB(ph)#Patient DETAILS
    m = int(input("\tEnter Medicin Charges\t: "))
    r = RoomCost(ph)
    GST = 0.18*(m + r)
    print("\tDISCHARGE DATE : ",b)
    Serch(Dr)#Doctor DETAILS
    print("\t\t\t\t\t  BILL DETAILS")
    print("\n")
    print("\t\t\t\tTYPE \t\t\t COST ")
    print("\n")
    print("\t\t\t\tMedicine\t\t  ",m)
    print("\t\t\t\tRoom \t\t\t  ",r)
    print("\t\t\t\tGST\t\t\t  ",GST)
    print("\n"*2)
    print("\t\t\t\tTOTAL COST\t\t  ",GST+r+m)
    print("\n\n")
def dele1(Ch,Date):
    f = open("Appoint.txt","rb")
    f1 = open("Temp1.txt","ab")
    while True:
        try:
            a = pickle.load(f)
            
            if a.Phno==Ch and a.Date==Date:
                print ("\n\t\t\t\tAPPOINTMENT CANCELLED")

            else:
                pickle.dump(a,f1)
                
        except EOFError:
            break
    f.close()
    f1.close()
    os.remove("Appoint.txt")
    os.rename("Temp1.txt","Appoint.txt")




def BedNo(ph):
    Token=0
    f=open("Room.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            if x[0]==ph:
                Token+=1
            else:
                Token+=1
        except EOFError:
            break
    return Token+1




def Check4(Ph):
    f=open("Emergency.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            if x.Ph==Ph:
                    f.close()
                    return True
        except EOFError:
                    break
    f.close()


def DelBed(Ph):
    if Check4(Ph)==True:
        f=open("Emergency.txt","rb")
        f2=open("Temp5.txt", "ab")
        while True:
            try:
                a = pickle.load(f)
                
                if a.Ph==Ph:
                    pass

                else:
                    pickle.dump(a,f2)
                    
            except EOFError:
                break
        f.close()
        f2.close()
        os.remove("Emergency.txt")
        os.rename("Temp5.txt","Emergency.txt")

def check5(Ph):
    f=open("Emergency.txt","rb")
    while True:
        try:
            x=pickle.load(f)
            if x.Ph==Ph:
                    f.close()
                    return x.Status
        except EOFError:
                    break
    f.close()
#---------------------------------------End Of Menu Driven------------------------------------#





#-------------------------------------All Menudriven------------------------------------------#

def Menudriven():
    while True:
        print ("\n")
        print ("\n\t\t\t\t\t  WELCOME \n")
        print ("\t\t\t","~"*45)
        print ("\t\t\t", "="*45)
        print ("\t\t\t","~"*45)
        print ("\n\t\t\t\t1. Login As Admin")
        print ("\t\t\t\t2. Login As Doctor")
        print ("\t\t\t\t3. For OPD")
        print ("\t\t\t\t4. For Emergency")
        print ("\t\t\t\t5. Exit\n")
        print ("\t\t\t","~"*45)
        print ("\t\t\t", "="*45)
        print ("\t\t\t","~"*45)
        print ("\n\n\n\n\n")
        choice=int(input("\n\t\tEnter your choice\t\t: "))
        if choice == 1:
            print ("\n\t\t\t\t        Sign UP")
            print ("\t\t\t\t\t", "~"*7)
            count=0

            print("\t\t\t      YOU HAVE IN TOTAL 3 ATTEMPTS")
            while count<3:
               
                login =str(input("\n\t\tEnter Login ID \t: "))
                passw = str(input("\t\tEnter Password\t: "))
                if login==AId and passw==APass:
                    print ("\n\t\t\t\t   Login Successfull")
                    print("\t\t\t\t  ","^"*17)
                    print("\n\n\n")
                    time.sleep(2)
                    Menudriven1()
                    break
                else:
                      print( "\n\t\t\t\t| Re Enter ID and Password |")
                      count+=1
                      print("\t\t\t\t| Attempts Used ",count,"\t   |")
                      continue
            if(count>3):
                print("\n\n")
                print("\t\tYOU HAVE EXCEEDE THE LIMIT OF ENTERING THE CORRECT DETAILS!!")
                print
                print("\t\t\t\t    TRY AFTER 24 HOURS!!")

            break
            
            
        elif choice==2:
            print ("\n\t\t\t\t\tSign UP")
            print ("\t\t\t\t\t", "~"*7)
            count=0
            while count<3:
                login =str(input("\n\t\tEnter Login ID\t\t\t: "))
                passw = str(input("\t\tEnter Password\t\t\t: "))
                if  Check2(login,passw)!=0:
                        print ("\n\tRe Enter ID and Pass")
                        count+=1
                        continue
                else:
                        time.sleep(2)
                        print
                        print ("\n\t\t\t\t   Login Successfull")
                        print("\t\t\t\t  ","^"*17)
                        print("\n"*3)
                        time.sleep(2)
                        Menudriven4(login)
                        break

                      

            
        elif choice==3:
                            print ("\n\t\t\t\t\t\tOPD\n")
                            print ("\t\t\t", "="*45)
                            Dept()
                            print("\t\t\t","="*45)
                            Search2()
                            ID=str(input("\n\t\tEnter The Doctor ID\t\t\t: "))
                            Date=str(input("\t\tEnter The Date\t\t\t\t:"))
                            print ("\n\t\tName(Patient)\t\tPhone Number\t\tToken No.\n")
                            App(ID,Date)
                            print ("\n\t\t\t\tTo Enter The Details Of Patient\n")
                            print ("\t\t\t\t", "~"*32)
                            while True:
                                Phno=str(input("\n\t\tEnter Your Phone No \t\t\t: "))
                                if Check1(Phno)!=0:
                                    Token=Check3(ID,Date)
                                    Create2(Phno,ID,Token+1,Date)
                                    print("\n\t\t\t\t\tTOKEN PROVIDED")
                                    break
                                else:
                                    print ("Token Number Is Already Given")
                                    break

        elif choice==4:
                        Menudriven6()
                        
                                                
            
        elif choice==5:
            
            print ("\n"*6)
            print ("\t\t\t\t", "_"*25)
            print ("\n\t\t\t\t\tTHANK YOU")
            print ("\t\t\t\t\t", "^"*9)
            print ("\n\t\t\t\t", "_"*25)
            print("\n"*6)
            break

        else:
            print ("\n\t\t\t\t!!Please Enter Correct Choice!!")
            continue



def Menudriven1():
    while True:
        print ("\n\t\t\t\t\tLoged In As ADMIN\n")
        print ("\t\t\t", "="*45)
        print ("\n\t\t\t\t1. Doctor")
        print ("\t\t\t\t2. Room")
        print ("\t\t\t\t3. Logout")
        print ("\n\t\t\t", "="*45)

        choice=int(input("\n\t\tEnter your choice\t\t= "))

        if choice==1:
            print("\n\n\n")
            Menudriven2()
            
        if choice==2:
            print("\n\n\n")
            MenuRoom()
            
                    
        if choice==3:
            print ("\n"*6)
            print ("\t\t\t\t", "_"*25)
            print ("\n\t\t\t\t\tTHANK YOU")
            print ("\t\t\t\t\t", "^"*9)
            print ("\n\t\t\t\t", "_"*25)
            print("\n"*6)
            break



        
 

def Menudriven2():
    while True:
        print ("\n\t\t\t\t\tTO ALTER A DOCTOR\n")
        print ("\t\t\t", "="*45)
        print ("\n\t\t\t\t1. To Enter Data of Doctor")
        print ("\t\t\t\t2. To Show Data Of A Doctor")
        print ("\t\t\t\t3. To Search A Doctor")
        print ("\t\t\t\t4. To Delete A Doctor")
        print ("\t\t\t\t5. To Update Data Of Doctor")
        print ("\t\t\t\t6. Exit")
        print ("\n\t\t\t", "="*45)
        choice=int(input("\n\t\tEnter your choice\t\t= "))
        if choice==1:
            print ("\n\t\t\t\tEnter The Details Of Doctor")
            print ("\t\t\t\t", "~"*27)
            Create()
            
        if choice==2:
            print ("\n\t\t\t\t|DETAILS OF DOCTOR'S IN  A.K. HOSPITAL|")
            print ("\t\t\t\t", "~"*40)
            print ("\tDoctor ID\t\tName\t\t\tSpeciality\t\tFees\t\tAvailability")
            print
            
            Show()
            
        if choice==3:
            print ("\n\t\t\t\tTo Search A Doctor's Detail")
            print ("\t\t\t\t", "~"*29)
            Serch1()
        if choice==4:
            print ("\n\t\t\t\tTo Delete A Doctor Data")
            print ("\t\t\t\t", "~"*23   )
            Dele()
            
        if choice==5:
            print ("\n\t\t\t\tTo Update Data Of A Doctor")
            print ("\t\t\t\t", "~"*26    )
            Update()
            
        if choice==6:
            
            print ("\n"*6)
            print ("\t\t\t\t", "_"*25)
            print ("\n\t\t\t\t\tTHANK YOU")
            print ("\t\t\t\t\t", "^"*9)
            print ("\n\t\t\t\t", "_"*25)
            print("\n"*6)
            break

def Menudriven4(ID):
    while True:
        print("\n"*5)
        print ("\n\t\t\t\t\tLoged In As Doctor\n")
        print ("\t\t\t", "="*45)
        print ("\n\t\t\t\t1. Appointments")
        print ("\t\t\t\t2. Update Condition of Patient")
        print ("\t\t\t\t3. Cancel An Appointment")
        print ("\t\t\t\t4. Exit")
        print ("\n\t\t\t", "="*45)

        choice=int(input("\n\t\tEnter your choice\t\t: "))
        print("\n"*3)

        if choice==1:
            print ("\n\t\t\t\t\tAPPOINTMENTS")
            print ("\t\t\t\t\t", "~"*12)
            Date=str(input("\n\t\tEnter The Date\t\t\t: "))
            print ("\n\t\t\tName(Patient)\tPhone Number\t\tToken No.\n")
            App(ID,Date)
            
        if choice==2:
            PatUP()

        if choice==3:
            print ("\n\t\t\t\tTO CANCEL APPOINTMENTS")
            print ("\t\t\t\t", "~"*23)
            print
            Date=str(input("\n\t\tEnter The Date\t\t: "))
            print ("\n\t\t\tName(Patient)\tPhone Number\tTime\tToken No.\n")
            print
            App(ID,Date)
            print
            ch=str(input("\n\t\tEnter The Phone Number To Cancell Appointment\t: "))
            dele1(ch,Date)
            
                    
        if choice==4:
            
            print ("\n"*6)
            print ("\t\t\t\t", "_"*25)
            print ("\n\t\t\t\t\tTHANK YOU")
            print ("\t\t\t\t\t", "^"*9)
            print ("\n\t\t\t\t", "_"*25)
            print("\n"*6)
            break


def Menudriven6():
        while True:
                        print ("\n\t\t\t\t\t  EMERGENCY\n")
                        print ("\t\t\t", "="*45)
                        print ("\n\t\t\t\t1. Admit A Patient")
                        print ("\t\t\t\t2. Patient's in Emergency Room")
                        print ("\t\t\t\t3. Update Data Of Patient")
                        print ("\t\t\t\t4. Discharge A Patient")
                        print ("\t\t\t\t5. Exit")
                        print ("\n\t\t\t", "="*45)
                        choice=int(input("\n\t\tEnter your choice\t\t: "))

                        if choice==1:
                            print ("\n\t\t\t\t\tTo Admit A Patient")
                            print ("\t\t\t\t\t", "~"*18)
                            Enter()
                            print("\n\t\t\t\t\tPATIENT ADMITTED")

                        if choice==2:
                            Show3()
                            
                        if choice==3:
                            PatUP()

                        if choice==4:
                            AdmissionE()
                            
                                    
                        if choice==5:
                            print ("\n"*6)
                            print ("\t\t\t\t", "_"*25)
                            print ("\n\t\t\t\t\tTHANK YOU")
                            print ("\t\t\t\t\t", "^"*9)
                            print ("\n\t\t\t\t", "_"*25)
                            print("\n"*6)
                            break


def MenuRoom():
                while True:
                        print ("\n\t\t\t\t\t    ROOMS\n")
                        print ("\t\t\t", "="*45)
                        
                        print ("\n\t\t\t\t1. List Of Patient's In Rooms")
                        print ("\t\t\t\t2. Exit")
                        print ("\n\t\t\t", "="*45)

                        choice=int(input("\n\t\tEnter your choice\t\t: "))
                        print("\n"*4)


                        if choice==1:
                            Show2()
                            
                                           
                        if choice==2:
                            print ("\n"*6)
                            print ("\t\t\t\t", "_"*25)
                            print ("\n\t\t\t\t\tTHANK YOU")
                            print ("\t\t\t\t\t", "^"*9)
                            print ("\n\t\t\t\t", "_"*25)
                            print("\n"*6)
                            break

                

Menudriven()
#-----------------------------------------End Of Menu Driven-----------------------#









