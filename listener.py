from time import sleep
from event import subscribe

def send_email_message(user):
    print(f'Email: User {user.name} with email {user.email} has just signed up!')
    
def send_discord_message(user):
    print(f'Discord: User {user.name} with email {user.email} has just signed up!')

def send_slack_message(user):
    print(f'Slack: User {user.name} with email {user.email} has just signed up!')
    

# container for all the messages that will be send when this event fires
# all these messages are for when users register
# event_type = USER_REGISTERED
def handle_user_registered_event(user):
    send_email_message(user)
    send_discord_message(user)
    send_slack_message(user)
    sleep(3)
    

def send_user_reset_message(user):
    print('Please enter the new password: ')   

# container for all the messages when you forget your password
# event_type = USER_FORGOT_PASSWD
def handle_user_password_forgotten_event(user):
    print(f'New password has been sent to email: {user.email}')
    send_user_reset_message(user)
    

# adds the function to the indicated event_type
def setup_event_handlers():
    subscribe("USER_REGISTERED", handle_user_registered_event)
    subscribe("USER_FORGOT_PASSWD", handle_user_password_forgotten_event)