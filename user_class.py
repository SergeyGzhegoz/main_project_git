class Registration():
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.phone} - {self.email}"
