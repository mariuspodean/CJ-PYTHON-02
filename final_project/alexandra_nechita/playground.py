from application import PersonalDevelopment, Physical, Spiritual, Emotional, Social, Intellectual, DomainsCollection, check_status, i_am_a_decorator, i_am_a_generator
import datetime
from time import sleep
from inspect import getgeneratorstate


Alexandra_desired_physical = {
    'sleep': 56,
    'nutrition': 10500,
    'physical_exercise': 7
}

Alexandra_desired_spiritual = {
    'charity': 1,
    'meditation': 7,
    'contemplation': 1
}

Alexandra_desired_emotional = {
    'identifying_emotions_in_self': 1,
    'identifying_emotions_in_others': 3,
    'managing_self_emotions': 3,
    'managing_relationships': 7
}

Alexandra_desired_social = {
    'monthly_message': 4,
    'monthly_meeting': 1,
    'randomly_calls': 2
}

Alexandra_desired_intellectual = {
    'daily_reading': 50,
    'memory_exercises': 10,
    'foreign_language': 105,
    'online_classes': 1
}

Alexandra_dict_of_friends = {
    'Dan': ('0722222222', datetime.datetime(1988, 12, 5).strftime("%x")),
    'Larisa': ('0745111111', datetime.datetime(1991, 7, 5).strftime("%x")),
    'Mihaela': ('0744333333', datetime.datetime(1968, 5, 11).strftime("%x")),
    'Dan Adrian': ('0721555555', datetime.datetime(1966,11, 9).strftime("%x"))
}

Alexandra_actual_physical = {}
Alexandra_actual_spiritual = {}
Alexandra_actual_emotional = {}
Alexandra_actual_social = {
    'monthly_message': 6,
    'monthly_meeting': 1,
    'randomly_calls': 2
}
Alexandra_actual_intellectual = {
    'daily_reading': 50,
    'memory_exercises': 10,
    'foreign_language': 105,
    'online_classes': 1
}

Alexandra_Actual_Physical = Physical('Alexandra\'s Actual Physical', Alexandra_actual_physical, 23.0)
Alexandra_Actual_Spiritual = Spiritual('Alexandra\'s Actual Spiritual', Alexandra_actual_spiritual, 'buddhist')
Alexandra_Actual_Emotional = Emotional('Alexandra\'s Actual Emotional', Alexandra_actual_emotional, 120)
Alexandra_Actual_Social = Social('Alexandra\'s Actual Social', Alexandra_actual_social, Alexandra_dict_of_friends)
Alexandra_Actual_Intellectual = Intellectual('Alexandra\'s Actual Intellectual', Alexandra_actual_intellectual, 'computer science')

Alexandra_Desired_Physical = Physical('Alexandra\'s Desired Physical', Alexandra_desired_physical, 23.0)
Alexandra_Desired_Spiritual = Spiritual('Alexandra\'s Desired Spiritual', Alexandra_desired_spiritual, 'buddhist')
Alexandra_Desired_Emotional = Emotional('Alexandra\'s Desired Emotional', Alexandra_desired_emotional, 120)
Alexandra_Desired_Social = Social('Alexandra\'s Desired Social', Alexandra_desired_social, Alexandra_dict_of_friends)
Alexandra_Desired_Intellectual = Intellectual('Alexandra\'s Desired Intellectual', Alexandra_desired_intellectual, 'computer science')

print(Alexandra_Desired_Physical)
print(Alexandra_Desired_Spiritual)
print(Alexandra_Desired_Emotional)
print(Alexandra_Desired_Social)
print(Alexandra_Desired_Intellectual)
print(Alexandra_Desired_Intellectual.__repr__())

intellectual_activities = list(Alexandra_Desired_Intellectual.keys())
print('The activities list for intellectual domain is', intellectual_activities, '\n')

intellectual_activities_and_details = list(Alexandra_Desired_Intellectual.items())
print('The activities list for intellectual domain, with the corresponding details, is', intellectual_activities_and_details, '\n')

Alexandra_desired_collection = (Alexandra_Desired_Physical, Alexandra_Desired_Spiritual, Alexandra_Desired_Emotional, Alexandra_Desired_Social, Alexandra_Desired_Intellectual)
Alexandra_actual_collection = (Alexandra_Actual_Physical, Alexandra_Actual_Spiritual, Alexandra_Actual_Emotional, Alexandra_Actual_Social, Alexandra_Actual_Intellectual)

Alexandra_Desired_Collection = DomainsCollection('Alexandra\'s Desired Collection', Alexandra_desired_collection)
Alexandra_Actual_Collection = DomainsCollection('Alexandra\'s Actual Collection', Alexandra_actual_collection)
print(Alexandra_Desired_Collection)

Dan_physical = {
    'sleep': 56,
    'nutrition': 10500,
    'physical_exercise': 7
}

Dana_physical = {
    'sleep': 50,
    'nutrition': 10500,
    'physical_exercise': 7
}

Darius_physical = {
    'sleep': 60,
    'nutrition': 10500,
    'physical_exercise': 7
}

Mara_physical = {
    'sleep': 57,
    'nutrition': 10500,
    'physical_exercise': 7,
    'medical check': 1
}

Mihai_physical = {
    'sleep': 56,
    'nutrition': 10500,
    'physical_exercise': 7,
    'medical check': 1
}

Mioara_physical = {
    'sleep': 50,
    'nutrition': 10500,
    'physical_exercise': 7,
    'medical check': 1
}

Bogdan_physical = {
    'sleep': 80,
    'nutrition': 10500
    
}

Ioana_physical = {
    'sleep': 64,
    'nutrition': 10500
    
}

Andreea_physical = {
    'sleep': 63,
    'nutrition': 10500
    
}

Dan_Physical = Physical('Dan\'s Physical', Dan_physical, 23)
Dana_Physical = Physical('Dana\'s Physical', Dana_physical, 23)
Darius_Physical = Physical('Darius\'s Physical', Darius_physical, 23)
Mara_Physical = Physical('Mara\'s Physical', Mara_physical, 23)
Mihai_Physical = Physical('Mihai\'s Physical', Mihai_physical, 23)
Mioara_Physical = Physical('Mioara\'s Physical', Mioara_physical, 23)
Bogdan_Physical = Physical('Bogdan\'s Physical', Bogdan_physical, 23)
Ioana_Physical = Physical('Ioana\'s Physical', Ioana_physical, 23)
Andreea_Physical = Physical('Andreea\'s Physical', Andreea_physical, 23)

print(Alexandra_Desired_Physical==Dan_Physical)
print(Alexandra_Desired_Physical>Dana_Physical)
print(Alexandra_Desired_Physical<Darius_Physical)
print(Alexandra_Desired_Physical>Mara_Physical)
print(Alexandra_Desired_Physical<Mioara_Physical)
print(Alexandra_Desired_Physical==Mihai_Physical)
print(Alexandra_Desired_Physical>Bogdan_Physical)
print(Alexandra_Desired_Physical<Ioana_Physical)
print(Alexandra_Desired_Physical==Andreea_Physical)

check_status(Alexandra_Desired_Collection, Alexandra_Actual_Collection)

Alexandra_Desired_Physical.save_state()

gen = i_am_a_generator(Alexandra_dict_of_friends)

while True:
    try:
        print(getgeneratorstate(gen))
        print(f'Please suggest this app to your friend {next(gen)}')
        sleep(2)
    except StopIteration:
        print('Thank you for suggesting us to all you friends')
        break