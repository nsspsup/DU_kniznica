
# models/member.py

class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Member {self.name}>"
