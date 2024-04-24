class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                found_contacts.append(contact)
        
        return found_contacts

    def update_contact(self, index, new_contact):
        if index >= 0 and index < len(self.contacts):
            self.contacts[index] = new_contact
        else:
            print("Invalid index")

    def delete_contact(self, index):
        if index >= 0 and index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid index")

# Example usage
contact_manager = ContactManager()

# Add contacts
contact_manager.add_contact(Contact("Huzaifa", "1234567890", "huzafa298.com", "karachi"))
contact_manager.add_contact(Contact("huzaifa", "0987654321", "huzafa298.com", "Nursery"))

# View contact list
print("Contact List:")
contact_manager.view_contact_list()

# Search for a contact
query = "Huzaifa"
print(f"Search results for '{query}':")
found_contacts = contact_manager.search_contact(query)
for contact in found_contacts:
    print(f"Name: {contact.name}, Phone: {contact.phone_number}")

# Update a contact
new_contact = Contact("Talha", "1112223333", "talha76@email.com", "Gulshan ")
contact_manager.update_contact(0, new_contact)
print("Updated contact list:")
contact_manager.view_contact_list()

# Delete a contact
contact_manager.delete_contact(1)
print("Updated contact list after deleting contact:")
contact_manager.view_contact_list()
