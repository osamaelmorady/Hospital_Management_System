from tkinter import *


Intervals=["2:00","2:30","3:00","3:30","4:00","4:30"]
Reservations={}

#-------------------------------- Cancel Reservation Tab -----------------------------------------#   
'''
def CancelReservationClose() :
    cancelreservation.destroy()
    managementtab.deiconify()

def CancelReservation() :
    global cancelreservation
    managementtab.withdraw()
    cancelreservation=Toplevel(clinic)
    cancelreservation.title("CancelReservation")
    cancelreservation.geometry("600x400+400+250")
    
    
    but2=Button(cancelreservation,text='Back to Management System',width=30\
    ,command=CancelReservationClose)
    but2.place(x=150,y=320)
'''
#-------------------------------- Make Reservation Tab -----------------------------------------#     

#close the make reservations window    
def MakeReservationClose() :
    makereservation.destroy()
    managementtab.deiconify()

#show the table of reservations    
def ShowReservation ()  :
    Times=list()
    IDs=list()
    Names=list()
    Ages=list()
    Genders=list()
    label1=Label(makereservation,text="Time").place(x=50,y=120)
    label2=Label(makereservation,text="ID",width=3).place(x=105,y=120)
    label3=Label(makereservation,text="NAME",width=30).place(x=140,y=120)
    label4=Label(makereservation,text="Age").place(x=400,y=120)
    label5=Label(makereservation,text="Gender").place(x=500,y=120)
    i=0
    for time in Reservations.keys() :
        Times.append(Label(makereservation,text=' '+time))
        Times[i].place(x=50,y=155+30*i)
        IDs.append(Label(makereservation,text=Reservations[time][0],width=5))
        IDs[i].place(x=105,y=155+30*i)
        Names.append(Label(makereservation,text=Reservations[time][1],width=30))
        Names[i].place(x=140,y=155+30*i)
        Ages.append(Label(makereservation,text=Reservations[time][2],width=3))
        Ages[i].place(x=400,y=155+30*i)
        Genders.append(Label(makereservation,text=Reservations[time][3],width=5))
        Genders[i].place(x=500,y=155+30*i)
        i+=1
    
#Get the reservations schedule from the file (reservations.txt) and put it into dict (Reservations)     
def LoadReservation () :
    try :
        file=open("reservations.txt",'r')
    except :
        file=open("reservations.txt",'x')
        file=open("reservations.txt",'r')
    lines=file.readlines() 
    for line in lines :
        T_in=line.find("TIME:")
        ID_in=line.find("ID:")
        N_in=line.find("NAME:")
        A_in=line.find("AGE:")
        G_in=line.find("GENDER:")
            
        R_time=(line[T_in+5:ID_in]).strip()
        R_ID=line[ID_in+3:N_in].strip()
        R_name=line[N_in+5:A_in].strip()
        R_age=line[A_in+4:G_in].strip()
        R_gender=line[G_in+7:].strip()
            
        Reservations[R_time]=(R_ID,R_name,R_age,R_gender)
    file.close()
            
#export reservation to file (reservations.txt) 
def RecordReservation() :
    id=Reserved_ID.get().lower().strip()
    time=Reserved_time.get().lower().strip()
    name=' '
    age=' '
    gender=' '
    flag=0
    file4=open("idlist.txt",'r')
    line0=file4.readline().split(' # ')
    if id in line0 :
        file1=open("database.txt",'r')
        lines=file1.readlines()
        line=''
        for line in lines :
            id_ind=line.find("ID:")
            name_ind=line.find("NAME:")
            age_ind=line.find("AGE:")
            gender_ind=line.find("GENDER:")
            
            id_val=line[id_ind+3:name_ind].strip()
            if id_val==id :
                name=line[name_ind+5:age_ind].strip().lower()
                age=line[age_ind+4:gender_ind].strip().lower()
                gender=line[gender_ind+7:].strip().lower()
                flag=1
                break
            else :
                pass
        file1.close() 
    else : 
        name=' '
        age=' '
        gender=' '
        id=' '
    file4.close()
    
    LoadReservation ()
    ShowReservation ()
    
    file=open("reservations.txt",'r')
    old_reservations=file.readlines()
    file.close()
    
    file2=open("reservations.txt",'w')
    new_reservations="".join(old_reservations)

    if flag==1 :
        line="TIME: "+ time +' '+"ID: "+ id +' '+"NAME: " +name+\
                ' '+"AGE: " +age+' '+"GENDER: "+ gender+' '+" \n" 
        file2.write(new_reservations+line)

    else :
        line="TIME: "+ time +' '+"ID: "+ ' ' +' '+"NAME: " +' '+\
                ' '+"AGE: " +' '+' '+"GENDER: "+ ' '+' '+" \n" 
        file2.write(new_reservations+line)
        
    file2.close()

    LoadReservation ()
    ShowReservation ()
        

def MakeReservation() :
    global makereservation
    global Reserved_ID
    global Reserved_time
    managementtab.withdraw()
    makereservation=Toplevel(clinic)
    makereservation.title("Make Reservation ")
    makereservation.geometry("600x400+400+250")
    
    label1=Label(makereservation,text="Enter ID : ")
    label1.place(x=50,y=30)
    Reserved_ID=StringVar()
    ent5=Entry(makereservation,textvariable=Reserved_ID,width=30)
    ent5.place(x=200,y=30)
    
    label2=Label(makereservation,text="Enter Time : ").place(x=50,y=70)
    Reserved_time=StringVar()
    box1=Spinbox(makereservation,values=Intervals,textvariable=Reserved_time,width=8)
    box1.place(x=200,y=70)
    label3=Label(makereservation,text="Pm ").place(x=270,y=70)
    
    but2=Button(makereservation,text='Make Reservation',width=15,command=RecordReservation)
    but2.place(x=450,y=50)
    
    but3=Button(makereservation,text='Back to Management System',width=30\
    ,command=MakeReservationClose)
    but3.place(x=150,y=360)
    
    LoadReservation ()
    ShowReservation ()
    

#----------------------------------- Edit Patient Tab ------------------------------------------------#     
    
def OverWritePatientData() :
    patientid=str(Patient_ID.get())
    patientname=str(Patient_Name.get())
    patientage=str(Patient_Age.get())
    patientgender=str(Patient_Gender.get())
    try :
        file1=open("idlist.txt",'r')
    except :
        file1=open("idlist.txt",'x')
        file1=open("idlist.txt",'r')

    line=file1.readline().split(' # ')
    
    if patientid not in line :
        label1=Label(editpatient,text="ID Not Exist")
        label1.place(x=350,y=50)
        
    else  :   
        label1=Label(editpatient,text="                                       ")
        label1.place(x=350,y=50)
        searched_index=line.index(patientid)
        file2=open("database.txt",'r')
        olddata=file2.readlines()
        olddata[searched_index]="ID:"+' '+patientid+'  '+"NAME:"+' '+patientname+'  '\
                    +"AGE:"+' '+patientage+'  '+"GENDER:"+' '+patientgender+'  \n'
        file2.close()
        
        file2=open("database.txt",'w')
        newfile="".join(olddata)
        file2.write(newfile)
        file2.close()
        

def WritePatientData() :
    patientid=str(Patient_ID.get())
    patientname=str(Patient_Name.get())
    patientage=str(Patient_Age.get())
    patientgender=str(Patient_Gender.get())
    try :
        file1=open("idlist.txt",'r')
    except :
        file1=open("idlist.txt",'x')
        file1=open("idlist.txt",'r')

    line=file1.readline().split(' # ')
    if patientid in line :
        label1=Label(addpatient,text="ID Already Exist")
        label1.place(x=350,y=50)
    else  :   
        label1=Label(addpatient,text="                                       ")
        label1.place(x=350,y=50)
        file2=open("database.txt",'a')
        file2.write("ID:"+' '+patientid+'  '+"NAME:"+' '+patientname+'  '\
        +"AGE:"+' '+patientage+'  '+"GENDER:"+' '+patientgender+'  \n')
        file2.close()
        file1=open("idlist.txt",'a')
        file1.write(patientid+' # ')
        file1.close()

def EditPatientClose():
    editpatient.destroy()
    managementtab.deiconify()
        
def EditPatient():
    global Patient_ID
    global Patient_Name
    global Patient_Age
    global Patient_Gender
    global editpatient
    managementtab.withdraw()
    editpatient=Toplevel(clinic)
    editpatient.title("Edit Patient data")
    editpatient.geometry("600x400+400+250")
    
    label1=Label(editpatient,text="Patient ID : ")
    label1.place(x=50,y=50)
    Patient_ID=StringVar()
    ent1=Entry(editpatient,textvariable=Patient_ID,width=30)
    ent1.place(x=150,y=50)
    
    label2=Label(editpatient,text="Patient Name : ")
    label2.place(x=50,y=100)
    Patient_Name=StringVar()
    ent2=Entry(editpatient,textvariable=Patient_Name,width=30)
    ent2.place(x=150,y=100)
    
    label3=Label(editpatient,text="Patient Age : ")
    label3.place(x=50,y=150)
    Patient_Age=StringVar()
    ent3=Entry(editpatient,textvariable=Patient_Age,width=30)
    ent3.place(x=150,y=150)
    
    label4=Label(editpatient,text="Patient Gender : ")
    label4.place(x=50,y=200)
    Patient_Gender=StringVar()
    ent4=Entry(editpatient,textvariable=Patient_Gender,width=30)
    ent4.place(x=150,y=200)
    
    but=Button(editpatient,text='Enter',width=40,command=OverWritePatientData)
    but.place(x=150,y=250)
    
    but2=Button(editpatient,text='Back to Management System',width=30,command=EditPatientClose)
    but2.place(x=150,y=320)

#----------------------------------- Add Patient Tab ------------------------------------------------# 
    
def AddPatientClose():
    addpatient.destroy()
    managementtab.deiconify()
        
def AddPatient() :
    global Patient_ID
    global Patient_Name
    global Patient_Age
    global Patient_Gender
    global addpatient
    managementtab.withdraw()
    addpatient=Toplevel(clinic)
    addpatient.title("Add Patient")
    addpatient.geometry("600x400+400+250")
    
    label1=Label(addpatient,text="Patient ID : ")
    label1.place(x=50,y=50)
    Patient_ID=StringVar()
    ent1=Entry(addpatient,textvariable=Patient_ID,width=30)
    ent1.place(x=150,y=50)
    
    label2=Label(addpatient,text="Patient Name : ")
    label2.place(x=50,y=100)
    Patient_Name=StringVar()
    ent2=Entry(addpatient,textvariable=Patient_Name,width=30)
    ent2.place(x=150,y=100)
    
    label3=Label(addpatient,text="Patient Age : ")
    label3.place(x=50,y=150)
    Patient_Age=StringVar()
    ent3=Entry(addpatient,textvariable=Patient_Age,width=30)
    ent3.place(x=150,y=150)
    
    label4=Label(addpatient,text="Patient Gender : ")
    label4.place(x=50,y=200)
    Patient_Gender=StringVar()
    ent4=Entry(addpatient,textvariable=Patient_Gender,width=30)
    ent4.place(x=150,y=200)
    
    but=Button(addpatient,text='Enter',width=40,command=WritePatientData)
    but.place(x=150,y=250)
    
    but2=Button(addpatient,text='Back to Management System',width=30,command=AddPatientClose)
    but2.place(x=150,y=320)

#--------------------------------------------------------------------------------------------------#
#----------------------------------- Admin MODE Login ---------------------------------------------# 
#--------------------------------------------------------------------------------------------------#
    
def AdminModeclose():
    managementtab.destroy()
    clinic.deiconify()

def CheckData() :
    global managementtab
    AdminName=adminname_entry.get()
    AdminPassword=adminpassword_entry.get()
    adminname_entry.delete(0,END)
    adminpassword_entry.delete(0,END)
    if AdminName=='' :
        if AdminPassword=='' :
            adminlogintab.destroy()
            
            managementtab=Toplevel(clinic)
            managementtab.title("Admin Mode")
            managementtab.geometry("400x300+500+300")
            but0=Button(managementtab,text='Add Patient',width=30,command=AddPatient)
            but0.place(x=75,y=50)
            but1=Button(managementtab,text='Edit Patient',width=30,command=EditPatient)
            but1.place(x=75,y=100)
            but2=Button(managementtab,text='Make/Cancel a Reservation',width=30,command=MakeReservation)
            but2.place(x=75,y=150)
            #but3=Button(managementtab,text='Cancel a Reservation',width=30,command=CancelReservation)
            #but3.place(x=75,y=200)
            but4=Button(managementtab,text='Back to ModeScreen',width=20,command=AdminModeclose)
            but4.place(x=150,y=250)
        else :
            lab3=Label(adminlogintab,text="Incorrect UserName/Password")
            lab3.place(x=100,y=150)
    else :
            lab3=Label(adminlogintab,text="Incorrect UserName/Password")
            lab3.place(x=100,y=150)

def ModeScreenBack():
    adminlogintab.destroy()
    clinic.deiconify()
        
def AdminLoginTab() :
    clinic.withdraw()
    global adminname_entry
    global adminpassword_entry
    global AdminName
    global AdminPassword
    global adminlogintab
    global login
    AdminName=StringVar()
    AdminPassword=StringVar()
    adminlogintab=Toplevel(clinic)
    adminlogintab.title("Login")
    adminlogintab.geometry("400x250+500+300")
    lab1=Label(adminlogintab,text="  UserName :")
    lab1.place(x=0,y=25)
    adminname_entry=Entry(adminlogintab,textvariable=AdminName,text='  ')
    adminname_entry.place(x=150,y=25)
    lab2=Label(adminlogintab,text="  Password :")
    lab2.place(x=0,y=50)
    adminpassword_entry=Entry(adminlogintab,textvariable=AdminPassword,text=' ',show='*')
    adminpassword_entry.place(x=150,y=50)
    login=Button(adminlogintab,text="Sign in",command=CheckData)
    login.place(x=100,y=100)
    back1=Button(adminlogintab,text="Back to ModeScreen",width=20,command=ModeScreenBack)
    back1.place(x=100,y=200)  

#----------------------------------------------------------------------------------------------# 
#----------------------------------- USER MODE ------------------------------------------------#  
#----------------------------------------------------------------------------------------------#   

def ViewReservationclose() :
    viewveservation.withdraw()
    userlogintab.deiconify()

def ViewReservation() :
    global viewveservation
    userlogintab.withdraw()
    viewveservation=Toplevel(clinic)
    viewveservation.title("View today's Reservation")
    viewveservation.geometry("600x400+400+250")
    LoadReservation ()
    
    Times=list()
    IDs=list()
    Names=list()
    Ages=list()
    Genders=list()
    label1=Label(viewveservation,text="Time").place(x=50,y=50)
    label3=Label(viewveservation,text="NAME").place(x=190,y=50)
    label4=Label(viewveservation,text="Age").place(x=400,y=50)

    i=0
    for time in Reservations.keys() :
        Times.append(Label(viewveservation,text=' '+time))
        Times[i].place(x=50,y=100+30*i)
        
        Names.append(Label(viewveservation,text=Reservations[time][1]))
        Names[i].place(x=190,y=100+30*i)
        Ages.append(Label(viewveservation,text=Reservations[time][2]))
        Ages[i].place(x=400,y=100+30*i)

        i+=1

    but2=Button(viewveservation,text='Back to Management System',width=30\
    ,command=ViewReservationclose)
    but2.place(x=150,y=320)

def PatientRecordClose() :
    viewpatientrecord.withdraw()
    userlogintab.deiconify()

def ViewUserInfo() :
    label2=Label(viewpatientrecord,text="ID",width=5).place(x=50,y=120)        
    label3=Label(viewpatientrecord,text="NAME",width=30).place(x=80,y=120)
    label4=Label(viewpatientrecord,text="Age").place(x=350,y=120)
    label5=Label(viewpatientrecord,text="Gender").place(x=450,y=120)

    patientid=str(USER_ID.get()).strip()
    file1=open("idlist.txt",'r')
    line=file1.readline().split(' # ')
    
    if patientid in line :
        label1=Label(viewpatientrecord,text="                                       ")
        label1.place(x=420,y=60)
   
        file1=open("database.txt",'r')
        lines=file1.readlines()
        for line in lines :
            id_ind=line.find("ID:")
            name_ind=line.find("NAME:")
            age_ind=line.find("AGE:")
            gender_ind=line.find("GENDER:")
            
            id_val=line[id_ind+3:name_ind].strip()
            if  id_val==patientid :
                name =line[name_ind+5:age_ind].strip().lower()
                age=line[age_ind+4:gender_ind].strip().lower()
                gender=line[gender_ind+7:].strip().lower()
                label21=Label(viewpatientrecord,text=patientid,width=5).place(x=50,y=160)        
                label31=Label(viewpatientrecord,text=name,width=30).place(x=80,y=160)
                label41=Label(viewpatientrecord,text=age,width=3).place(x=350,y=160)
                label51=Label(viewpatientrecord,text=gender,width=5).place(x=450,y=160)
                break
            else :
                pass
    else  :   
        label1=Label(viewpatientrecord,text="ID Not Exist")
        label1.place(x=420,y=60)
    
def ViewPatientRecord() :
    global viewpatientrecord
    global USER_ID
    userlogintab.withdraw()
    viewpatientrecord=Toplevel(clinic)
    viewpatientrecord.title("Patient Record")
    viewpatientrecord.geometry("600x400+400+250")
    
    label1=Label(viewpatientrecord,text="Enter ID : ")
    label1.place(x=50,y=30)
    USER_ID=StringVar()
    ent5=Entry(viewpatientrecord,textvariable=USER_ID,width=30)
    ent5.place(x=200,y=30)
    
    but3=Button(viewpatientrecord,text='Show Info',width=15\
    ,command=ViewUserInfo)
    but3.place(x=420,y=25)  
    
    but2=Button(viewpatientrecord,text='Back to Management System',width=30\
    ,command=PatientRecordClose)
    but2.place(x=150,y=320)    

def UserModeclose():
    userlogintab.withdraw()
    clinic.deiconify()    
    
def UserLoginTab() :
    global userlogintab
    clinic.withdraw()
    
    userlogintab=Toplevel(clinic)
    userlogintab.title("User Mode")
    userlogintab.geometry("400x250+500+300")
    but0=Button(userlogintab,text='View Patient Record',width=30,command=ViewPatientRecord)
    but0.place(x=50,y=50)
    but1=Button(userlogintab,text="View Today's Reservations",width=30,command=ViewReservation)
    but1.place(x=50,y=100)
    but4=Button(userlogintab,text='Back to ModeScreen',width=20,command=UserModeclose)
    but4.place(x=50,y=150)    
    
#----------------------------------------------------------------------------------------------# 
#----------------------------------- MODE Selection -------------------------------------------#  
#----------------------------------------------------------------------------------------------#     
    
def ModeScreen() :
    global clinic
    clinic=Tk()
    clinic.title("Clinic Management System")
    clinic.geometry("400x300+500+300")
    clinic.wm_iconbitmap("download.ico")
    admin_button=Button(clinic,text='Admin',font=2,height=2,width=20,command=AdminLoginTab)
    admin_button.place(x=90,y=100)
    admin_button.flash()
    user_button=Button(clinic,text='User',font=2,height=2,width=20,command=UserLoginTab)
    user_button.place(x=90,y=200)
    user_button.flash()
    clinic.mainloop()    
