import configparser

config=configparser.RawConfigParser()
config.read(r"C:\\Users\\rezwana.shaik\\PycharmProjects\\registerpage.py\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getbaseurl():
        url=config.get("details","baseurl")
        return url

    @staticmethod
    def enterfirstname():
        firstname = config.get("details", "firstname")
        return firstname

    @staticmethod
    def enterlastname():
        lastname = config.get("details", "lastname")
        return lastname

    @staticmethod
    def enteremail():
        email = config.get("details", "email")
        return email

    @staticmethod
    def entertelephone():
        telephone = config.get("details", "telephone")
        return telephone

    @staticmethod
    def enterpassword():
        password = config.get("details", "password")
        return password

    @staticmethod
    def enterconfirmpassword():
        confirmpassword = config.get("details", "confirm_password")
        return confirmpassword





