from user import User
from event import post_event

class UserDatabase:
    def __init__(self):
        self._users = []
        self.current_user = None
        
    
    def create_user(self, name, email, password):
        u = User(name, email, password)
        self._users.append(u)
        self.current_user = u
        post_event("USER_REGISTERED", u)
        
    
    def get_user(self):
        return self._users.pop()
        
    # query_user
    
    # delete_user
    
    def logout(self):
        self.current_user = None