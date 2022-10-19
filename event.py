
subscribers = dict()

# this is how you add functions to that event type
def subscribe(event_type: str, func):
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(func)
    

# this actually performs the action of displaying the events
def post_event(event_type: str, data):
    if event_type not in subscribers:
        return
    
    for func in subscribers[event_type]:
        func(data)
        