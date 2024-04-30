from datetime import datetime
from django.utils.timezone import make_aware
from healthApp.models import *
from accounts.models import CustomUser

# ORDER IS doctor, patient, cares_for, doctor_specialties, hospitals, procedure, works_at, oversees, medication, drug_manufacturer, manufactured_by, insurance company,
# insurance policy, covers, covered_by, prescribes


def populateData():
    createMultipleTestUsers()
    createMultipleCaresFor()
    createMultipleDoctorSpecialties()
    createMultipleHospitals()
    createMultipleProcedures()
    createMultipleWorksAt()
    createMultipleOversees()
    createMultipleMedications()
    createMultipleDrugManufacturers()
    createMultipleManufacturedBy()
    createMultipleInsuranceCompanies()
    createMultipleInsurancePolicies()
    createMultipleCovers()
    createMultipleCoveredBy()
    createMultiplePrescribes()


def createTestUser(healthID, password, userKind, Age, Phone_num, Address, email, Fname, Lname):
    user_data = {
        'healthID': healthID,
        'password': password,
        'email': email,
        'userKind': userKind,
        'Age': Age,
        'Phone_num': Phone_num,
        'Address': Address,
        'first_name': Fname,
        'last_name': Lname
    }
    user = CustomUser.objects.create_user(**user_data)
    user.set_password(password)
    user.save()


def createMultipleTestUsers():
    healthIDs = ["123456789", "987654321",
                 "456789012", "890123456", "321098765", "234567890", "567890123", "678901234", "789012345", "800000000", "100000001", "100000002", "100000003", "100000004", "100000005",
                 "100000006", "100000007", "100000008", "100000009", "100000010"]
    userKinds = ['doctor', 'doctor', 'doctor', 'doctor', 'doctor', 'doctor', 'doctor', 'doctor', 'doctor', 'doctor',
                 'patient', 'patient', 'patient', 'patient', 'patient', 'patient', 'patient', 'patient', 'patient', 'patient',]
    passwords = ['doctor123', 'doctor123', 'doctor123', 'doctor123', 'doctor123', 'doctor123', 'doctor123', 'doctor123', 'doctor123', 'doctor123','patient123', 'patient123', 'patient123', 'patient123', 'patient123', 'patient123', 'patient123', 'patient123', 'patient123', 'patient123']
    Ages = ['10', '23', '44', '43', '1', '2', '5', '90', '42', '55',
            '10', '23', '44', '43', '1', '2', '5', '90', '42', '55']
    phone_numbers = ["5551234567", "9876543210", "1234567890", "8765432109", "2345678901", "5550001111", "5551112222", "5552223333", "5553334444",
                     "5554445555", "5551234567", "9876543210", "1234567890", "8765432109", "2345678901", "5550001111", "5551112222", "5552223333", "5553334444", "5554445555"]
    addresses = ["123 Main St", "456 Oak St", "789 Elm St", "987 Pine St", "345 Maple Ave",
                 "567 Birch Blvd", "890 Cedar Ln", "234 Spruce Dr", "876 Pine Ave", "543 Elm Blvd", "123 Main St", "456 Oak St", "789 Elm St", "987 Pine St", "345 Maple Ave",
                 "567 Birch Blvd", "890 Cedar Ln", "234 Spruce Dr", "876 Pine Ave", "543 Elm Blvd"]
    emails = [
        "alice.johnson@example.com",
        "bob.smith@example.com",
        "carol.davis@example.com",
        "david.miller@example.com",
        "emma.wilson@example.com", "frank.white@example.com", "grace.brown@example.com", "harry.green@example.com",
        "isabel.king@example.com", "jack.davis@example.com", "jerry.Seinfeld@example.com",
        "George.Costanza@example.com",
        "cosmo.kramer@example.com",
        "charlie.miller@example.com",
        "elaine.bennis@example.com", "frank.costanza@example.com", "newman.paul@example.com", "george.washington@example.com",
        "benajamin.franklin@example.com", "abraham.lincoln@example.com"
    ]
    fnames = ["Alice", "Bob", "Carol", "David", "Emma",
              "Frank", "Grace", "Harry", "Isabel", "Jack", "Jerry", "George", "Kramer", "Charlie", "Elaine", "Frank", "Newman", "George", "Benjamin", "Abraham",]
    lnames = ["Johnson", "Smith", "Davis", "Miller", "Wilson",
              "White", "Brown", "Green", "King", "Davis", "Seinfeld", "Costanza", "Cosmo", "Miller", "Bennis", "Costanza", "Paul", "Washington", "Franklin", "Lincoln"]

    for i in range(20):
        createTestUser(healthIDs[i], passwords[i], userKinds[i], Ages[i],
                       phone_numbers[i], addresses[i], emails[i], fnames[i], lnames[i])

# The below methods of createTestDoctor, createMultipleTestDoctor, createTestPatient, createMultipleTestPatient, are no longer used since doctor and patient creation is tied to user creation instead. We've left them in just for reference.

# def createTestDoctor(id, name, phone_num, email):
#     testDoctor = Doctor(Medical_ID_Number=id, Name=name,
#                         Phone_num=phone_num, Email=email)
#     testDoctor.save()


# def createMultipleDoctors():
#     medical_id_numbers = ["123456789", "987654321",
#                           "456789012", "890123456", "321098765", "234567890", "567890123", "678901234", "789012345", "800000000"]
#     names = ["Alice Johnson", "Bob Smith",
#              "Carol Davis", "David Miller", "Emma Wilson", "Frank White", "Grace Brown",
#              "Harry Green", "Isabel King", "Jack Davis"]
#     phone_numbers = ["5551234567", "9876543210",
#                      "1234567890", "8765432109", "2345678901", "5550001111",
#                      "5551112222", "5552223333", "5553334444", "5554445555"]
#     emails = [
#         "alice.johnson@example.com",
#         "bob.smith@example.com",
#         "carol.davis@example.com",
#         "david.miller@example.com",
#         "emma.wilson@example.com", "frank.white@example.com", "grace.brown@example.com", "harry.green@example.com",
#         "isabel.king@example.com", "jack.davis@example.com"
#     ]

#     # Call createTestDoctor method with the values
#     for i in range(len(medical_id_numbers)):
#         createTestDoctor(
#             id=medical_id_numbers[i],
#             name=names[i],
#             phone_num=phone_numbers[i],
#             email=emails[i])

# # Create test data for Patient model


# def createTestPatient(health_id, email, age, fname, mname, lname, phone_num, address):
#     testPatient = Patient(health_ID=health_id, Email=email, Age=age, FName=fname,
#                           MName=mname, LName=lname, Phone_num=phone_num, Address=address)
#     testPatient.save()


# def createMultiplePatients():
#     health_ids = ["100000001", "100000002", "100000003", "100000004", "100000005",
#                   "100000006", "100000007", "100000008", "100000009", "100000010"]
#     emails = ["patient1@example.com", "patient2@example.com", "patient3@example.com",
#               "patient4@example.com", "patient5@example.com",
#               "patient6@example.com", "patient7@example.com", "patient8@example.com",
#               "patient9@example.com", "patient10@example.com"]
#     ages = [25, 30, 22, 40, 28, 35, 32, 45, 27, 38]
#     fnames = ["Patient", "Patient", "Patient", "Patient", "Patient",
#               "Patient", "Patient", "Patient", "Patient", "Patient"]
#     mnames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#     lnames = ["Doe", "Smith", "Johnson", "Miller", "Wilson",
#               "Jones", "White", "Brown", "Green", "King"]
#     phone_numbers = ["5551111111", "5552222222", "5553333333",
#                      "5554444444", "5555555555", "5556666666",
#                      "5557777777", "5558888888", "5559999999", "5550000000"]
#     addresses = ["123 Main St", "456 Oak St", "789 Elm St", "987 Pine St", "345 Maple Ave",
#                  "567 Birch Blvd", "890 Cedar Ln", "234 Spruce Dr", "876 Pine Ave", "543 Elm Blvd"]

#     for i in range(10):
#         createTestPatient(
#             health_id=health_ids[i],
#             email=emails[i],
#             age=ages[i],
#             fname=fnames[i],
#             mname=mnames[i],
#             lname=lnames[i],
#             phone_num=phone_numbers[i],
#             address=addresses[i]
#         )

# Create test data for Hospital model


def createTestHospital(hospital_id, name, address, phone_num):
    testHospital = Hospital(Hospital_ID=hospital_id, Name=name, Address=address, Phone_num=phone_num)
    testHospital.save()


def createMultipleHospitals():
    hospital_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    names = ["General Hospital", "City Medical Center", "Unity Healthcare", "Hope Hospital",
             "Central Clinic", "Community Health Center", "Sunrise Medical Center",
             "Metropolitan Hospital", "Eagle Ridge Medical Center", "Harmony Clinic"]
    addresses = ["123 Health St", "456 Care Blvd", "789 Wellness Ave", "987 Healing Ln", "345 Medical Dr",
                 "567 Community St", "890 Sunrise Blvd", "234 Metro Ave", "876 Eagle Ln", "543 Serenity Dr"]
    phone_numbers = ["5551110000", "5552221111", "5553332222", "5554443333", "5555554444",
                     "5556665555", "5557776666", "5558887777", "5559998888", "5550009999"]

    for i in range(10):
        createTestHospital(
            hospital_id=hospital_ids[i],
            name=names[i],
            address=addresses[i],
            phone_num=phone_numbers[i]
        )

# Create test data for Procedure model


def createTestProcedure(procedure_id, procedure_date, procedure_type, duration_hours, name, result, patient_health_id, hospital_id):
    testProcedure = Procedure(Procedure_ID=procedure_id, Procedure_Date=procedure_date, Procedure_Type=procedure_type,
                              Duration_hours=duration_hours, Name=name, Result=result, Patient_Health_ID_id=patient_health_id, Hospital_ID_id=hospital_id)
    testProcedure.save()


def createMultipleProcedures():
    procedure_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    procedure_dates = [
        make_aware(datetime(2023, 1, 15, 9, 30)),
        make_aware(datetime(2023, 2, 20, 8, 0)),
        make_aware(datetime(2023, 3, 25, 10, 15)),
        make_aware(datetime(2023, 4, 10, 9, 45)),
        make_aware(datetime(2023, 5, 5, 11, 30)),
        make_aware(datetime(2023, 6, 30, 12, 20)),
        make_aware(datetime(2023, 7, 12, 13, 15)),
        make_aware(datetime(2023, 8, 8, 15, 0)),
        make_aware(datetime(2023, 9, 18, 16, 35)),
        make_aware(datetime(2023, 10, 22, 10, 45)),
        make_aware(datetime(2024, 9, 22, 11, 45)),
        make_aware(datetime(2023, 8, 9, 10, 00)),
    ]
    procedure_types = ["Surgery", "Checkup", "MRI", "X-Ray", "Dental",
                       "Physical Therapy", "Colonoscopy", "Blood Test", "Endoscopy", "CT Scan", "Blood work", "PET Scan"]
    durations = [3, 1, 2, 1, 1, 2, 4, 1, 3, 2, 1, 5]
    names = ["Appendectomy", "Procedure 2", "Procedure 3", "Procedure 4", "Procedure 5",
             "Procedure 6", "Procedure 7", "Procedure 8", "Procedure 9", "Procedure 10", "Check for glycemia", "Brain Cancer screening"]
    results = ["Successful", "Normal", "Abnormal", "Negative", "Excellent",
               "Improving", "Good", "Positive", "Clear", "Stable", "N/A", "Negative"]
    patient_health_ids = ["100000001", "100000002", "100000003", "100000004", "100000005",
                          "100000006", "100000007", "100000008", "100000009", "100000010", "100000001", "100000001"]
    hospital_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5]

    for i in range(12):
        createTestProcedure(
            procedure_id=procedure_ids[i],
            procedure_date=procedure_dates[i],
            procedure_type=procedure_types[i],
            duration_hours=durations[i],
            name=names[i],
            result=results[i],
            patient_health_id=patient_health_ids[i],
            hospital_id=hospital_ids[i]
        )


# Create test data for Medication model
def createTestMedication(din, cost, dosage, name):
    testMedication = Medication(DIN=din, Cost=cost, Dosage=dosage, Name=name)
    testMedication.save()


def createMultipleMedications():
    dins = ["987654321", "123456789", "345678901", "567890123", "789012345",
            "234567890", "876543210", "901234567", "456789012", "098765432"]
    costs = [10.5, 15.2, 8.0, 12.3, 9.9, 14.7, 11.0, 13.5, 16.8, 10.0]
    dosages = ["Take one pill daily", "Take two pills with meals", "As needed for pain", "Apply to affected area twice daily",
               "Take with water before bedtime", "Take one capsule every 6 hours", "Take three times a day", "Apply a thin layer every morning",
               "Take one tablet after meals", "Take as directed by your doctor"]
    names = ["Penicillin", "Levothyroxine", "Metformin", "Simvastatin", "Hydrocodone",
             "Vancomycin", "Albuterol", "Accutane", "atorvastatin", "amlodipine",]

    for i in range(10):
        createTestMedication(
            din=dins[i],
            cost=costs[i],
            dosage=dosages[i],
            name=names[i]
        )

# Create test data for Insurance_Company model


def createTestInsuranceCompany(company_name, address, phone_num):
    testInsuranceCompany = Insurance_Company(Insurance_name=company_name, Address=address, Phone_num=phone_num)
    testInsuranceCompany.save()


def createMultipleInsuranceCompanies():
    company_names = ["ABC Insurance", "XYZ Assurance", "SecureCare Insurance", "GlobalGuard Policies", "SureShield",
                     "SafeHarbor Insurance", "Peace of Mind Assurance", "EliteCoverage", "Guardian Insurance", "WellSure Policies"]
    addresses = ["123 Insurance St", "456 Coverage Ave", "789 Policy Lane", "987 Assurance Blvd", "345 Benefit Dr",
                 "567 Security Rd", "890 Protection Blvd", "234 Policy Innovation St", "876 Safety Ave", "543 Care Lane"]
    phone_numbers = ["5551111111", "5552222222", "5553333333", "5554444444", "5555555555",
                     "5556666666", "5557777777", "5558888888", "5559999999", "5550000000"]

    for i in range(10):
        createTestInsuranceCompany(
            company_name=company_names[i],
            address=addresses[i],
            phone_num=phone_numbers[i]
        )

# Create test data for Insurance_Policy model


def createTestInsurancePolicy(insurance_name, policy_id, coverage, monthly_cost):
    testInsurancePolicy = Insurance_Policy(Insurance_name_id=insurance_name, Policy_id=policy_id, Coverage=coverage, Monthly_Cost=monthly_cost)
    testInsurancePolicy.save()


def createMultipleInsurancePolicies():
    company_names = ["ABC Insurance", "XYZ Assurance", "SecureCare Insurance", "GlobalGuard Policies", "SureShield",
                     "SafeHarbor Insurance", "Peace of Mind Assurance", "EliteCoverage", "Guardian Insurance", "WellSure Policies"]

    policy_ids = ["A12345678", "B23456789", "C34567890", "D45678901", "E56789012",
                  "F67890123", "G78901234", "H89012345", "I90123456", "J01234567"]

    coverages = [80, 90, 75, 85, 95, 70, 88, 92, 78, 87]
    monthly_costs = [50, 60, 40, 55, 70, 35, 58, 65, 48, 62]

    for i in range(10):
        createTestInsurancePolicy(
            insurance_name=company_names[i],
            policy_id=policy_ids[i],
            coverage=coverages[i],
            monthly_cost=monthly_costs[i]
        )

# Create test data for Doctor_Specialties model


def createTestDoctorSpecialties(doctor_id, specialty):
    testDoctorSpecialties = Doctor_Specialties(Doctor_Medical_ID_Number_id=doctor_id, Specialty=specialty)
    testDoctorSpecialties.save()


def createMultipleDoctorSpecialties():
    medical_id_numbers = ["123456789", "987654321", "456789012", "890123456", "321098765",
                          "234567890", "567890123", "678901234", "789012345", "800000000", "123456789", "123456789"]
    specialties = ["Cardiology", "Dermatology", "Endocrinology", "Gastroenterology", "Hematology",
                   "Neurology", "Oncology", "Pediatrics", "Psychiatry", "Rheumatology", "Oncology", "Hematalogy"]

    for i in range(12):
        createTestDoctorSpecialties(
            doctor_id=medical_id_numbers[i],
            specialty=specialties[i]
        )

# Create test data for Works_At model


def createTestWorksAt(doctor_id, hospital_id):
    testWorksAt = Works_At(Medical_ID_id=doctor_id, Hospital_ID_id=hospital_id)
    testWorksAt.save()


def createMultipleWorksAt():
    medical_ids = ["123456789", "987654321", "456789012", "890123456", "321098765",
                   "234567890", "567890123", "678901234", "789012345", "800000000", "123456789", "123456789"]
    hospital_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5]

    for i in range(12):
        createTestWorksAt(
            doctor_id=medical_ids[i],
            hospital_id=hospital_ids[i]
        )

# Create test data for Manufactured_By model


def createTestManufacturedBy(din, drug_manufacturer_id):
    testManufacturedBy = Manufactured_By(DIN_id=din, Drug_Manufacturer_Id_id=drug_manufacturer_id)
    testManufacturedBy.save()


def createMultipleManufacturedBy():
    dins = ["987654321", "123456789", "345678901", "567890123", "789012345",
            "234567890", "876543210", "901234567", "456789012", "098765432", "987654321", "456789012", "234567890"]
    manufacturer_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 4]

    for i in range(13):
        createTestManufacturedBy(
            din=dins[i],
            drug_manufacturer_id=manufacturer_ids[i]
        )

# Create test data for Drug_Manufacturer model


def createTestDrugManufacturer(manufacturer_id, name, address, phone_num):
    testDrugManufacturer = Drug_Manufacturer(Id=manufacturer_id, Name=name, Address=address, Phone_num=phone_num)
    testDrugManufacturer.save()


def createMultipleDrugManufacturers():
    manufacturer_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    names = ["PharmaTech Innovations", "MediSynth Labs", "BioCure Solutions", "Precision Pharma Systems", "VitaGen Pharmaceuticals",
             "NanoMed Health Sciences", "GeneFusion Therapeutics", "SynthoCare BioPharma", "OmniVax Industries", "MolecularHeal Pharmaceuticals"]
    addresses = ["123 Pharma St", "456 Biotech Ave", "789 Health Lane", "987 Science Blvd", "345 Medicine Dr",
                 "567 Research Rd", "890 Innovation Blvd", "234 Wellness St", "876 Life Ave", "543 Cure Lane"]
    phone_numbers = ["5551111111", "5552222222", "5553333333", "5554444444", "5555555555",
                     "5556666666", "5557777777", "5558888888", "5559999999", "5550000000"]

    for i in range(10):
        createTestDrugManufacturer(
            manufacturer_id=manufacturer_ids[i],
            name=names[i],
            address=addresses[i],
            phone_num=phone_numbers[i]
        )

# Create test data for CaresFor model


def createTestCaresFor(patient_health_id, doctor_id):
    testCaresFor = CaresFor(Patient_Health_ID_id=patient_health_id, Doctor_Medical_ID_Number_id=doctor_id)
    testCaresFor.save()


def createMultipleCaresFor():
    # Assuming you have 10 doctors and 10 patients already created
    doctor_ids = ["123456789", "987654321", "456789012", "890123456", "321098765",
                  "234567890", "567890123", "678901234", "789012345", "800000000", "987654321", "123456789"]

    patient_health_ids = ["100000001", "100000002", "100000003", "100000004", "100000005",
                          "100000006", "100000007", "100000008", "100000009", "100000010", "100000001", "100000002"]

    for i in range(12):
        createTestCaresFor(
            patient_health_id=patient_health_ids[i],
            doctor_id=doctor_ids[i]
        )

# Create test data for Oversees model


def createTestOversees(procedure_id, doctor_id):
    testOversees = Oversees(Procedure_ID_id=procedure_id, Doctor_Medical_ID_Number_id=doctor_id)
    testOversees.save()


def createMultipleOversees():
    medical_ids = ["123456789", "987654321", "456789012", "890123456", "321098765",
                   "234567890", "567890123", "678901234", "789012345", "800000000", "123456789", "123456789", "567890123", "678901234", "800000000"]
    procedure_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 11, 11, 12]

    for i in range(15):
        createTestOversees(
            doctor_id=medical_ids[i],
            procedure_id=procedure_ids[i]
        )

# Create test data for Prescribes model


def createTestPrescribes(doctor_id, patient_health_id, medication_din):
    testPrescribes = Prescribes(Doctor_Medical_ID_Number_id=doctor_id, Patient_Health_ID_id=patient_health_id, Medication_DIN_id = medication_din)
    testPrescribes.save()


def createMultiplePrescribes():
    medical_ids = ["123456789", "987654321", "456789012", "890123456", "321098765",
                   "234567890", "567890123", "678901234", "789012345", "800000000", "123456789", "123456789", "321098765", "123456789"]

    health_ids = ["100000001", "100000002", "100000003", "100000004", "100000005",
                  "100000006", "100000007", "100000008", "100000009", "100000010", "100000001", "100000008", "100000001", "100000009"]

    dins = ["987654321", "123456789", "345678901", "567890123", "789012345",
            "234567890", "876543210", "901234567", "456789012", "098765432", "345678901", "345678901", "901234567", "876543210"]

    for i in range(14):
        createTestPrescribes(
            doctor_id=medical_ids[i],
            patient_health_id=health_ids[i],
            medication_din=dins[i]
        )

# Create test data for Covered_By model


def createTestCoveredBy(patient_health_id, insurance_name, policy_id):
    testCoveredBy = Covered_By(Health_ID_id=patient_health_id, Insurance_name_id=insurance_name, Policy_id_id=policy_id)
    testCoveredBy.save()


def createMultipleCoveredBy():
    health_ids = ["100000001", "100000002", "100000003", "100000004", "100000005",
                  "100000006", "100000007", "100000008", "100000009", "100000010", "100000001"]

    policy_ids = ["A12345678", "B23456789", "C34567890", "D45678901", "E56789012",
                  "F67890123", "G78901234", "H89012345", "I90123456", "J01234567", "H89012345"]

    company_names = ["ABC Insurance", "XYZ Assurance", "SecureCare Insurance", "GlobalGuard Policies", "SureShield",
                     "SafeHarbor Insurance", "Peace of Mind Assurance", "EliteCoverage", "Guardian Insurance", "WellSure Policies", "EliteCoverage"]

    for i in range(11):
        createTestCoveredBy(
            patient_health_id=health_ids[i],
            policy_id=policy_ids[i],
            insurance_name=company_names[i]
        )

# Create test data for Covers model


def createTestCovers(insurance_name, policy_id, din):
    testCovers = Covers(Insurance_name_id=insurance_name, Policy_id_id=policy_id, DIN_id=din)
    testCovers.save()


def createMultipleCovers():
    policy_ids = ["A12345678", "B23456789", "C34567890", "D45678901", "E56789012",
                  "F67890123", "G78901234", "H89012345", "I90123456", "J01234567", "A12345678", "A12345678"]

    company_names = ["ABC Insurance", "XYZ Assurance", "SecureCare Insurance", "GlobalGuard Policies", "SureShield",
                     "SafeHarbor Insurance", "Peace of Mind Assurance", "EliteCoverage", "Guardian Insurance", "WellSure Policies", "ABC Insurance", "ABC Insurance"]

    dins = ["987654321", "123456789", "345678901", "567890123", "789012345",
            "234567890", "876543210", "901234567", "456789012", "098765432", "123456789", "345678901"]

    for i in range(12):
        createTestCovers(
            policy_id=policy_ids[i],
            insurance_name=company_names[i],
            din=dins[i]
        )
