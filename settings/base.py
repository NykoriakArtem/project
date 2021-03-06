import os

URL = "https://ce.contrastsecurity.com/Contrast"


class Contrast:
    def __init__(self):
        self.admin_user = self.AdminUser()

    class AdminUser:
        def __init__(self):
            self.email = os.getenv("ADMIN_USER_EMAIL")
            self.pw = os.getenv("ADMIN_USER_PASSWORD")
            self.auth = os.getenv("USER_AUTH")
            self.api_key = os.getenv("USER_API_KEY")
