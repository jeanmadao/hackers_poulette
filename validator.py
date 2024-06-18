import re

class Validator:
    @staticmethod
    def validate_name(name):
        regex = r"^[a-zA-Z]+(-[a-zA-Z])*$"
        if not re.match(regex, name):
            raise ValueError("Not a valid name!")
        return True

    @staticmethod
    def validate_email(email):
        regex = r"^\w+@\w+.\w{2,}$"
        if not re.match(regex, email):
            raise ValueError("Not a valid email address!")
        return True
