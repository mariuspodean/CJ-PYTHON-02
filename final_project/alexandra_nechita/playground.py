from application import PersonalDevelopment, Physical, Spiritual, Emotional, Social, Intellectual, DomainsCollection, check_status, i_am_a_decorator, i_am_a_generator
import datetime
from time import sleep
from inspect import getgeneratorstate

Alexandra_dict_of_friends = {
    'Dan': ('0722222222', datetime.datetime(1988, 12, 5).strftime("%x")),
    'Larisa': ('0745111111', datetime.datetime(1991, 7, 5).strftime("%x")),
    'Mihaela': ('0744333333', datetime.datetime(1968, 5, 11).strftime("%x")),
    'Dan Adrian': ('0721555555', datetime.datetime(1966,11, 9).strftime("%x"))
}

Ale_DP = Physical('Desired Physical', {'sleep': 56, 'nutrition': 10500, 'physical_exercise': 7}, 23.0)
Ale_DSp = Spiritual('Desired Spiritual', {'charity': 1, 'meditation': 7, 'contemplation': 1}, 'buddhist')
Ale_DE = Emotional('Desired Emotional', {'identifying_emotions_in_self': 1, 'identifying_emotions_in_others': 3, 'managing_self_emotions': 3, 'managing_relationships': 7}, 120)
Ale_DSo = Social('Desired Social', {'monthly_message': 4, 'monthly_meeting': 1, 'randomly_calls': 2}, Alexandra_dict_of_friends)
Ale_DI = Intellectual('Desired Intellectual', {'daily_reading': 50, 'memory_exercises': 10, 'foreign_language': 105, 'online_classes': 1}, 'computer science')

Ale_AP = Physical('Actual Physical', {'sleep': 50, 'nutrition':10500, 'physical_exercise': 7}, 23.0)
Ale_ASp = Spiritual('Actual Spiritual', {'charity': 1, 'meditation': 7, 'contemplation': 1}, 'buddhist')
Ale_AE = Emotional('Actual Emotional',{'identifying_emotions_in_others': 3, 'managing_self_emotions': 3, 'managing_relationships': 7} , 120)
Ale_ASo = Social('Actual Social',{'monthly_message': 6, 'monthly_meeting': 3, 'randomly_calls': 2} , Alexandra_dict_of_friends)
Ale_AI = Intellectual('Actual Intellectual', {'daily_reading': 15, 'memory_exercises': 10, 'foreign_language': 105, 'online_classes': 1, 'group study': 1}, 'computer science')


print(f'{Ale_DP} \n{Ale_DSp} \n{Ale_DE} \n{Ale_DSo} \n{Ale_DI}')

print(Ale_DI.__repr__(), '\n')


Ale_DCollection = DomainsCollection('Alexandra\'s Desired Collection', (Ale_DP, Ale_DSp, Ale_DE, Ale_DSo, Ale_DI))
Ale_ACollection = DomainsCollection('Alexandra\'s Actual Collection', (Ale_AP, Ale_ASp, Ale_AE, Ale_ASo, Ale_AI))

print(Ale_DCollection)


print(f'Desired state on physical is greater than actual state: {Ale_DP > Ale_AP}')
print(f'Desired state on spiritual is equal with actual state: {Ale_DSp == Ale_ASp}')
print(f'Desired state on emotional is greater than actual state: {Ale_DE > Ale_AE}')
print(f'Desired state on social is lesser than actual state: {Ale_DSo < Ale_ASo}')
print(f'Desired state on intellectual is lesser than actual state: {Ale_DI < Ale_AI}')


check_status(Ale_DCollection, Ale_ACollection)

Ale_DP.save_state()

gen = i_am_a_generator(Alexandra_dict_of_friends)

# The code block below should be included in a coroutine in order not to block the execution of the app
while True:
    try:
        print(getgeneratorstate(gen))
        print(f'Please recommend \u001b[35mEquilibrium\u001b[0m app to your friend, {next(gen)}')
        sleep(2)
    except StopIteration:
        print('Thank you for recommending us to all your friends!\u2665')
        print(getgeneratorstate(gen))
        break