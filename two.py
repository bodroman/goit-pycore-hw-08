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

def main():
    # Створюємо адресну книгу
    address_book = AddressBook()

    # Відновлюємо попередній стан адресної книги
    address_book.load_from_file("address_book.pkl")

    # Цикл програми наступний:
    while True:
        print("\n1. Додати контакт")
        print("2. Показати всі контакти")
        print("3. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            address_book.add_contact(name, phone)
            # Зберігаємо адресну книгу після додавання контакту
            address_book.save_to_file("address_book.pkl")
            print("Контакт успішно додано!")
        elif choice == '2':
            print("Контакти:")
            for contact in address_book.contacts:
                print(f"Ім'я: {contact['name']}, Телефон: {contact['phone']}")
        elif choice == '3':
            # Зберігаємо адресну книгу перед виходом з програми
            address_book.save_to_file("address_book.pkl")
            print("Дякую за використання програми!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
