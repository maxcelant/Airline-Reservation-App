class User:
    
    def __init__(self, name, password):
        self._name = name
        self._password = password
    
    def __repr__(self):
        return  f'{self._name}'
        