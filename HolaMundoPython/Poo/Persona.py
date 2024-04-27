


class Person:


    id = None
    name = None
    last_name = None
    phone = None
    mail = None
    city = None


    def __init__(self, id, name, last_name, phone, mail, city):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._mail = mail
        self._city = city

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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

#id = 3

#id(3)

#id_return = id()

Person.persona


persona.name= "Pepito"
sujeto = Person.name()

print(sujeto)