from application import Application
from listener import setup_event_handlers

def main():
    setup_event_handlers()
    app = Application()
    app.start()

if __name__ == '__main__':
    main()