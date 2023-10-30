'''
Southern Alberta Institute of Technology (SAIT)
Date: August 07, 2023

Software Development program
Object-oriented Programming I

ASSIGNMENT 4 - Project: Classes

Group members:
    Rafael Santos Coelho
    Mohammed Sameer Malek
    Aryan Ashishkumar Amin

Alberta Hospital software
Patient class
'''

class Patient:
    def __init__(self, id="", name="", disease="", gender="", age=0):
        pass

    def get_patient_id(self):
        pass

    def get_patient_name(self):
        pass

    def get_patient_disease(self):
        pass

    def get_patient_gender(self):
        pass

    def get_patient_age(self):
        pass

    def set_patient_id(self, new_id):
        pass

    def set_patient_name(self, new_name):
        pass

    def set_patient_disease(self, new_disease):
        pass

    def set_patient_gender(self, new_gender):
        pass

    def set_patient_age(self, new_age):
        pass

    def __str__(self):
        pass

class Patient:
    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(patient):
        return f"{patient.id}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}\n"

    def enter_patient_info():
        id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        return Patient(id, name, disease, gender, age)

def read_patients_file():
    patients = []
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split("_")
                if len(parts) == 5:
                    id, name, disease, gender, age = parts
                    patients.append(Patient(id, name, disease, gender, age))
    except FileNotFoundError:
        pass
    return patients

def search_patient_by_id(patients, patient_id):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    return None

def display_patient_info(patient):
    print("Patient Information:")
    print(f"ID: {patient.id}")
    print(f"Name: {patient.name}")
    print(f"Disease: {patient.disease}")
    print(f"Gender: {patient.gender}")
    print(f"Age: {patient.age}")

def edit_patient_info_by_id(patients):
    patient_id = input("Enter the patient ID to edit: ")
    patient = search_patient_by_id(patients, patient_id)
    if patient:
        print("Enter new information:")
        patient.name = input("Name: ")
        patient.disease = input("Disease: ")
        patient.gender = input("Gender: ")
        patient.age = input("Age: ")
        write_list_of_patients_to_file(patients)
        print("Patient information updated.")
    else:
        print("Cannot find the patient.")

def display_patients_list(patients):
    for patient in patients:
        display_patient_info(patient)
        print()

def format_patient_info_for_file(patient):
    formatted_info = f"{patient.id}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}\n"
    return formatted_info

def write_list_of_patients_to_file(patients):
    with open("patients.txt", "w") as file:
        for patient in patients:
            file.write(format_patient_info_for_file(patient))
def enter_patient_info():
    while True:
        try:
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            disease = input("Enter patient disease: ")
            gender = input("Enter patient gender: ")
            age = input("Enter patient age: ")
            return Patient(id, name, disease, gender, age)
        except Exception as e:
            print("Invalid input. Please try again.", e)

def add_patient_to_file(patients):
    new_patient = enter_patient_info()
    patients.append(new_patient)
    write_list_of_patients_to_file(patients)
    print("New patient added.")

def main():
    patients = read_patients_file()

    while True:
        print("\nMenu:")
        print("1. Search Patient by ID")
        print("2. Display Patients List")
        print("3. Edit Patient Information")
        print("4. Add New Patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            patient = search_patient_by_id(patients, patient_id)
            if patient:
                display_patient_info(patient)
            else:
                print("Can't find the patient...")
        elif choice == "2":
            display_patients_list(patients)
        elif choice == "3":
            edit_patient_info_by_id(patients)
        elif choice == "4":
            add_patient_to_file(patients)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
