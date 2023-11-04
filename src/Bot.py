from AddressBook import AddressBook, Name, Phone, Birthday, Email, Status, Note, Record
from abc import ABC, abstractmethod


class Bot:
    def __init__(self):
        self.book = AddressBook()
        self.view = ConsoleView()

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            display_congratulations(self.book.congratulate())
        elif action == 'view':
            self.view.display(self.book)
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")


class View(ABC):
    @abstractmethod
    def display(self, data):
        pass


class ConsoleView(View):
    def display(self, data):
        for record in data:
            print("_" * 50)
            print(f"Name: {record['name']}")
            print(f"Phones: {', '.join(record['phones'])}")
            if record['birthday']:
                birth = record['birthday'].strftime("%d/%m/%Y")
                print(f"Birthday: {birth}")
            print(f"Email: {record['email']}")
            print(f"Status: {record['status']}")
            print(f"Note: {record['note']}")

    def display_congratulations(self, data):
        print(data)
