from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name + self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone_number, email, job, company, work_phone_number):
        super().__init__(first_name, last_name, phone_number, email)
        self.job = job
        self.company = company
        self.work_phone_number = work_phone_number

    def contact(self):
        print(f"Wybieram numer {self.work_phone_number} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name + self.last_name)

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()

        if contact_type == "business":
            job = fake.job()
            company = fake.company()
            work_phone_number = fake.phone_number()
            contacts.append(BusinessContact(first_name, last_name, phone_number, email, job, company, work_phone_number))
        else:
            contacts.append(BaseContact(first_name, last_name, phone_number, email))

    return contacts

base_contacts = create_contacts("base", 5)
business_contacts = create_contacts("business", 5)

print("Base Contacts:")
for contact in base_contacts:
    print(contact)
    contact.contact()
    print(f"Label length: {contact.label_length}\n")

print("Business Contacts:")
for contact in business_contacts:
    print(contact)
    contact.contact()
    print(f"Label length: {contact.label_length}\n")