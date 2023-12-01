import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            print("File not found")

    def search_contacts(self, search_cont):
        matching_contacts = []
        for contact in self.contacts:
            if (
                search_cont.lower() in contact.name.lower() or
                search_cont.lower() in contact.phone.lower()
            ):
                matching_contacts.append(contact)
        return matching_contacts

