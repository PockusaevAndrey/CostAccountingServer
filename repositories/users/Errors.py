class UserIsExists(Exception):
    def __init__(self):
        super().__init__("User is exists")
