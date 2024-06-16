class Support:
    def __init__(self, first_name, last_name, gender, subjects, message):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.subjects = subjects
        self.message = message
        self.errors = {}

    def validate(self):
        if not self.first_name:
            self.errors["first_name"] = "First name required!"
        if not self.last_name:
            self.errors["last_name"] = "Last name required!"
        if not self.gender:
            self.errors["gender"] = "Gender required!"
        if not self.subjects:
            self.errors["subjects"] = "Subjects required!"
        if not self.message:
            self.errors["message"] = "Message required!"
