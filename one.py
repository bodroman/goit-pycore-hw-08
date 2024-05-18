import pickle

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({'name': name, 'phone': phone})

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.contacts, f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            print("File not found. Starting with an empty address book.")

# Послідовність використання коду:

# Створюємо об'єкт адресної книги
address_book = AddressBook()

# Додаємо контакти до адресної книги
address_book.add_contact("Bob", "2323232323")
address_book.add_contact("Jane", "1212121212")

# Зберігаємо адресну книгу у файл
address_book.save_to_file("address_book.pkl")

# Відновлюємо адресну книгу з файлу
address_book.load_from_file("address_book.pkl")

# Виводимо контакти з відновленої адресної книги
print("Contacts in the address book:")
for contact in address_book.contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}")
