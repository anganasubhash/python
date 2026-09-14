#5. Hospital Queue System
#Write a function patient_queue().
#•  Store patient names in a list.
#•  Display all patients using a loop.
#•  Remove the first patient.
#•  Add a new patient at the end.
#•  Search whether a patient is in the queue.
def patient_queue():
    for i in patient_name:
        print(i)
    patient_name.remove(patient_name[0])
    print(patient_name)
    patient_name.append("meenu")
    print(patient_name)
    print("Rahul" in patient_name)

patient_name=["Anjana","Rahul","Krishnaveni","Rithu"]
patient_queue()