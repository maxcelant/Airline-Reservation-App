from user import User

class UserDatabase:
    def __init__(self):
        self._users = []
        self.current_user = None
        
    
    def create_user(self, name, password):
        u = User(name, password)
        self._users.append(u)
        self.current_user = u
    
    
    def logout(self):
        self.current_user = None