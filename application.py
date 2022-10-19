from time import sleep
import os 

from userdb import UserDatabase

class Application:
    
    is_signed_in: bool
    
    def __init__(self):
        self.user_database = UserDatabase()
        self.is_signed_in = False
        
    
    def start(self):
        print('Welcome to the Airlines Reservation Application')
        sleep(1.2)
        self.verification()
        pass
        
    
    def verification(self):
        if self.is_signed_in:
            self.main_menu()
                    
        if not self.is_signed_in:
            choice = input('You are not signed in, Would you like to? [Y/y] to Sign In: ')
            if choice.lower() == 'y':
                self.user_signin()
                return
            
            print('Cannot continue without signing in...Quitting application')
            return
        
    
    def main_menu(self):
        os.system('clear')
        print('Menu Options: ')
        while self.is_signed_in:
            self.print_menu_options()
            choice = input(f'What would you like to do {self.user_database.current_user}?: ')
            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.join_flight()
            elif choice == "3":
                self.logout()
            else:
                break
    
    
    def print_menu_options(self):
        print('[1] View Available Flights')
        print('[2] Join a Flight')
        print('[3] Logout')

    
    def view_flights(self):
        pass
    
    
    def join_flight(self):
        pass
       
    
    def user_signin(self):
        name = input('Please enter your full name: ')
        password = input('Please enter your password: ')
        self.user_database.create_user(name, password)
        self.is_signed_in = True
        self.verification()
        
    
    def logout(self):
        self.is_signed_in = False
        self.user_database.logout()
        
        
        
    