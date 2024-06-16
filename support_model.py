class Support:
    def __init__(self, first_name=None, last_name=None, country=None, gender=None, subjects=0, message=None):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.gender = gender
        self.subjects = subjects
        self.message = message
        self.errors = {}

    def validate(self):
        self.errors = {}
        if not self.first_name:
            self.errors["first_name"] = "First name required!"
        if not self.last_name:
            self.errors["last_name"] = "Last name required!"
        if not self.country:
            self.errors["country"] = "Country required!"
        if not self.gender:
            self.errors["gender"] = "Gender required!"
        if not self.message:
            self.errors["message"] = "Message required!"

        return False if self.errors else True
