from validator import Validator

class Support:
    def __init__(self, first_name=None, last_name=None, email=None, country=None, gender=None, subjects=0, message=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.gender = gender
        self.subjects = subjects
        if message:
            message = message.split("\n")
        self.message = message
        self.errors = {}


    def validate(self):
        self.errors = {}
        if not self.first_name:
            self.errors["first_name"] = "First name required!"
        else:
            try:
                Validator.validate_name(self.first_name)
            except ValueError as error:
                self.errors["first_name"] = error

        if not self.last_name:
            self.errors["last_name"] = "Last name required!"
        else:
            try:
                Validator.validate_name(self.last_name)
            except ValueError as error:
                self.errors["last_name"] = error

        if not self.email:
            self.errors["email"] = "Email required!"
        else:
            try:
                Validator.validate_email(self.email)
            except ValueError as error:
                self.errors["email"] = error

        if not self.country:
            self.errors["country"] = "Country required!"
        else:
            try:
                Validator.validate_country(self.country)
            except ValueError as error:
                self.errors["country"] = error

        if not self.gender:
            self.errors["gender"] = "Gender required!"
        if not self.message:
            self.errors["message"] = "Message required!"

        return False if self.errors else True

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "country": self.country,
            "gender": self.gender,
            "subjects": self.subjects,
            "message": self.message,
            "errors": self.errors,
        }
