


class Person:

    def __init__(self, id,name, last_name, mail, phone):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._mail = mail
        self._phone = phone

    users = {}

    #Getter and Setter
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone


    # Metodos propios

    def create_person(self):
        self._id = int(input("Id:"))
        self._name = input("Name: ")
        self._last_name = input("LastName: ")
        self._mail = input("Mail: ")
        self._phone = input("Phone: ")





    def __str__(self):
        print = f"""
        id: {self._id},
        name:{self._name},
        last_name: {self._last_name},
        Mail: {self._mail},
        Phone: {self._phone}
        """
        return print