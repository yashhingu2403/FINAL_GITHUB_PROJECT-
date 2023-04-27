# In this class of doctors information it will give the out put as per doctore names is give in which it will depict the doctor ID,
# name, in which thing they have specialised in, till what time they will be available, what they have learned to become the doctor means their degree
# and last thing in which room he/she can be available means the room number. For which here we have define the function as per our convenience. 
class Doctorinformation():
    def __init__(self,doctor_id,name,specialization,working,qual,room):
        self.Doctorid = doctor_id
        self.Name = name
        self.Specialization = specialization
        self.Working_Time = working
        self.Qualification = qual
        self.Room_Number = room
    def set_Doctorid(self,Doctorid):
        self.Doctorid = Doctorid    
    def set_Name(self,Name):
        self.Name = Name
    def set_Specialization(self,Specialization):
        self.Specialization = Specialization
    def set_Working_Time(self,Working_Time):
        self.Working_Time = Working_Time
    def set_Qualification(self,Qualification):
        self.Qualification = Qualification
    def set_Room_Number(self,Room_Number):
        self.Room_Number = Room_Number
    def get_DoctorID(self):
        return (self.Doctorid)    
    def get_Name(self):
        return (self.Name)
    def get_Specialization(self):
        return (self.Specialization)
    def get_Working_Time(self):
        return (self.Working_Time)
    def get_Qualification(self):
        return (self.Qualification)
    def get_Room_Number(self):
        return (self.Room_Number)
    def __str__(self):
        return (f"{self.Doctorid}_{self.Name}_{self.Specialization}_{self.Working_Time}_{self.Qualification}_{self.Room_Number}")
# in this class of doctors manager it shows the doctor list with the name , id , specaility, time at which they are available, qualification, 
# room number where they will be available and after which their is one set which is set in "data" to show the doctors list with the data
# data stored of doctors. after which it can be search for the doctors for the by name, id , speciality , etc 
class DoctorsManager():
    def __init__(self):
        self.DoctorList = []
        self.readdoctorsfile()
    def format_dr_info(self,Doctor_information):
        return (Doctor_information.__str__())
    def enter_dr_info(self):
        id = input("Enter the doctor's ID : ")
        name = input("enter the doctor's Name : ")
        speciality = input("enter the doctor's Specialty : ")
        time = input("enter the doctor's Timing (e.g., 7am-10pm): ")
        qualification = input("enter the doctor's Qualification : ")
        room_number = input("enter  the doctor's Room Number : ")
        doc = Doctorinformation(id,name,speciality,time,qualification,room_number)
        return (doc)
    def readdoctorsfile(self):
        with open("doctors.txt", "r") as doctorfile:
            for doctor_lines in doctorfile:
                data = doctor_lines.strip().split('_')
                doctor = Doctorinformation(data[0],data[1],data[2],data[3],data[4],data[5])
                self.DoctorList.append(doctor)
    def search_doctor_by_id(self):
        id = str(input("Enter doctor ID: "))
        #t = 0
        for doctors in self.DoctorList:
            if doctors.DoctorID == id:
                self.D_doctor_info(self.DoctorList[0])
                self.D_doctor_info(doctors)
                return 
        print("Can't find the doctor with the same ID on the system")
    def search_doctor_by_name(self):
        name = str(input('enter doctor name: '))
        for doctor in self.DoctorList:
            if doctor.Name == name:
                self.D_doctor_info(self.DoctorList[0])
                self.D_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system")
    def D_doctor_info(self,doctors):
           print(f" {doctors.DoctorID:<10}{doctors.Name:<20}{doctors.Specialization:<14}{doctors.Working_Time:<20}{doctors.Qualification:<15}{doctors.Room_Number:<12}")
    def D_doctors_list(self):
        for doctors in self.DoctorList:
            self.D_doctor_info(doctors)
    def edit_doctor_info(self):
        Doctor_id= int(input("Please enter the id of the doctor that you want to edit their information:  "))
        for doctor in self.DoctorList: 
             if str(doctor.get_DoctorID()) == str(Doctor_id):
                Dr_name = input("Enter new Name : ")
                Dr_specialization = input("Enter new Specilist in : ")
                Dr_working_time = input("Enter new Timing : ")
                Dr_Qualification = input("Enter new Qualification : ") 
                Dr_room_number = input("Enter new Room number: ")
                self.Writelistofdoctorstofile()
                print(f"Doctor whose id is {doctor.get_DoctorID()} edited")
                return
             else:
                continue
        print("Cannot find the doctor...")     
    def Writelistofdoctorstofile(self):
        with open("doctors.txt", "w") as list:
            for doctor in self.DoctorList:
                list.write(self.format_dr_info(doctor)+"\n")
    def add_dr_info(self):
        newDoctors = self.enter_dr_info()
        self.DoctorList.append(newDoctors)
        with open("doctors.txt", "a") as list:
            list.write(self.format_dr_info(newDoctors))
        print(" Doctor whose id is ",str(newDoctors.get_DoctorID()),"has been added.")
# in this class patient it will  be telling about  pid, name, disease, gender , age and all other data of the patients 
class Patient:
    def __init__(self,pid,name,Disease,gender,age):
        self.pid=pid
        self.name=name
        self.Disease=Disease
        self.gender=gender
        self.age=age
    def set_pid(self,new_pid):
        self.pid=new_pid
    def set_name(self,new_name):
        self.name=new_name
    def set_disease(self,new_disease):
        self.disease=new_disease
    def set_gender(self,new_gender):
        self.gender=new_gender
    def set_age(self,new_age):
        self.age=new_age
    def get_pid(self):
        return self.pid
    def get_name(self):
        return self.name
    def get_disease(self):
        return self.Disease
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def __str__(self):
        return (f"{self.pid}_{self.name}_{self.Disease}_{self.gender}_{self.age}")
# in this class of patient manager here is will ask the user to enter the deatils of the patients in which it will ask the id, name,disease 
# gender and age. as a fix out put was there so the data of patients is stored in data in line 159 where it will show the data of the 
# patients. after which it will display the patients list for which we have define the functions 
class PatientManager:
    def __init__(self):
        self.patientsList = []
        self.read_patients_file()
    def format_patient_info_for_file(self, patient):
        return patient.__str__()
    def enter_patient_info(self):
        id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender : ")
        age = input("Enter patient age: ")
        pttnt = Patient(id,name,disease,gender,age)
        return pttnt
    def read_patients_file(self):
        with open("patients.txt","r") as patient_file:
            for patient_line in patient_file :
              data = patient_line.strip().split("_")
              patient = Patient(data[0],data[1],data[2],data[3],data[4])
              self.patientsList.append(patient)
    def search_patient_by_id(self):
        patient_id = str(input("Enter patient ID: "))
        for patient in self.patientsList:
            if str(patient.get_pid()) == str(patient_id):
                self.display_patient_info(self.patientsList[0])
                self.display_patient_info(patient)
                return
        print("Can't find the Patient with the same id on the system")
    def display_patient_info(self, Patientinfo):
        print(f" {Patientinfo.pid:<10}  {Patientinfo.name:<10}  {Patientinfo.disease:<10}  {Patientinfo.gender:<10}  {Patientinfo.age:<10}")
    def edit_patient_info_by_id(self):
        patient_id = int(input("Please enter the id of the Patient that you want to edit their information : "))
        for patient in self.patientsList:
            if str(patient.get_pid()) == str(patient_id):
                patient_name = input("Enter new Name: ")
                patient_disease = input("Enter new disease: ")
                patient_gender = input("Enter new gender : ")
                patient_age = input("Enter new age: ")
                patient.set_name(patient_name)
                patient.set_disease(patient_disease)
                patient.set_gender(patient_gender)
                patient.set_age(patient_age)
                self.writelistofpatientstofile()
                print(f"Patient whose id is {patient.get_pid()} has been added.")
                return
            else:
                continue
        print("Cannot find the patient...")
    def display_patients_list(self):
        for patient in self.patientsList:
            self.display_patient_info(patient)
    def writelistofpatientstofile(self):
        with open("patients.txt", "w") as list:
            for patient in self.patientsList:
                a=self.format_patient_info_for_file(patient)
                list.write(a+"\n")
    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.patientsList.append(patient)
        with open("patients.txt", "a") as list:
            list.write("\n")
            list.write(self.format_patient_info_for_file(patient))
        print(f"New patient whose id is {patient.get_pid()} has been  added.")
# in this last class of hospital management we have discuss and the is the main class in this code as when the user run this code it will 
# mainly start from this class and where it will ask the user to enter that what informartion do you what like the user wants pateints 
# list or the doctor list or data about them and all. For instance, if the user enter the value  then it will direct jump to another 
# class and run the data which we have allocated to value  1. 
class Management:
    def init(self):
        self.doctormanager = DoctorsManager()
        self.patientmanager = PatientManager()
    def Menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Managment system ")
            print("Select from the following options, or select 3 to stop: ")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit Program")
            Management_menu =input("Enter your choice (1-3): ")
            if Management_menu == "1":
                self.drsubmenu()
            elif Management_menu == "2":
                self.patients_submenu()
            elif Management_menu == "3":
                print("Thank you for coming.Bye!")
                break
    def drsubmenu(self):
        while True:
            print("Doctor Menu: ")
            print("1 -  Display doctors list")
            print("2 -  Search for doctor by ID")
            print("3 -  Search for doctor by name")
            print("4 -  Add Doctor")
            print("5 -  Edit Doctor info")
            print("6 -  Back to The  Main Menu")
            func=DoctorsManager()
            doctors_menu = input("Enter your choice (1-6): ")
            if doctors_menu == "1":
                func.D_doctors_list()
            elif doctors_menu == "2":
                func.search_doctor_by_id()
            elif doctors_menu == "3":
                func.search_doctor_by_name()
            elif doctors_menu == "4":
                func.add_dr_info()
            elif doctors_menu == "5":
                func.edit_doctor_info()
            elif doctors_menu == "6":
                break
    def patients_submenu(self):
        while True:
            print("Patient's Menu")
            print("1. Display patients list")
            print("2. Search for patient by ID")
            print("3. Add a new patient")
            print("4. Edit patient information")
            print("5. Return to Main Menu")
            func1=PatientManager()
            case = input("Enter your choice (1-5): ")
            if case == "1":
                func1.display_patients_list()
            elif case == "2":
                func1.search_patient_by_id()
            elif case == "3":
                func1.add_patient_to_file()
            elif case == "4":
                func1.edit_patient_info_by_id()
            elif case == "5":
                break  
s= Management()
s.Menu()
