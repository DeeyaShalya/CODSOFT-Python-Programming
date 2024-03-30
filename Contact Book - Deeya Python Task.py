#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)

                for idx, contact in enumerate(self._contacts):
                    if contact.name.lower() == name.lower():
                        del self._contacts[idx]

                print(' ')
                print('UPDATE CONTACT')
                name = str(input('Contact name: '))
                phone = str(input('Contact phone: '))
                email = str(input('Contact email: '))

                contact = Contact(name, phone, email)
                self._contacts.append(contact)
                self._save()
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('***************')
        print('Not found!')
        print('***************') 

def run():
    if not os.path.exists('contacts.csv'):
        with open('contacts.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'phone', 'email'])

    contact_book = ContactBook()

    while True:
        command = str(input('''
            What would you like to do?

            [a]dd contact
            [u]pdate contact
            [s]earch contact
            [d]elete contact
            [l]ist contacts
            [q]uit
        '''))

        if command == 'a':
            name = str(input('Enter contact name: '))
            phone = str(input('Enter contact phone number: '))
            email = str(input('Enter contact email: '))

            contact_book.add(name, phone, email)

        elif command == 'u':
            name = str(input('Enter contact name: '))

            contact_book.update(name)

        elif command == 's':
            name = str(input('Enter contact name: '))

            contact_book.search(name)

        elif command == 'd':
            name = str(input('Enter contact name: '))

            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 'q':
            break
        else:
            print('Command not found.')

if __name__ == '__main__':
    run()


# In[ ]:




