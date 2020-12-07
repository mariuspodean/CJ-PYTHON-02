import logging

class PersonalDevelopment:
    
    def __init__(self, name, dict_of_activities):
        self.name = name
        self.dict_of_activities = dict_of_activities
        
    def __eq__(self, other):
        for activity, frequency in self.items():
            if activity not in other.dict_of_activities:
                return False
            else:
                if frequency != other.dict_of_activities[activity]:
                    return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self,other):
        return not self.__eq__(other) and not self.__gt__(other)
       
    def __gt__(self, other):
        sum_of_percentages = 0
        for activity, frequency in self.items():
            if activity not in other.dict_of_activities:
                return True
            else:
                dif = frequency - other.dict_of_activities[activity]
                percentage_of_frequencies = dif / frequency * 100
                sum_of_percentages += percentage_of_frequencies
        return sum_of_percentages > 0

class MixinPrint:
    
    def __str__(self):
        star_line = '*' * (len(self.name) + 4) + '\n'
        string = f'{star_line} \n {self.name} \n {star_line} \n'     
        for index, (keys, values) in enumerate(self.items(), 1):
            string += f'{index}. {keys}: {values} \n'
        string += f'\n {star_line}'
        return (string)       

class Physical(PersonalDevelopment, MixinPrint):
    
    def __init__(self, name, dict_of_activities, BMI):
        super().__init__(name, dict_of_activities)
        self.BMI = BMI
    
    def __getitem__(self, activity):
        return self.dict_of_activities[activity]
        
    def __setitem__(self, activity, goal):
        self.dict_of_activities[activity] = goal
    
    def __iter__(self):
        return iter(self.dict_of_activities)
    
    def __delitem__(self, activity):
        del self.dict_of_activities[activity]
        
    def __len__(self):
        return len(self.dict_of_activities)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return super().__gt__(other)
    
    def __lt__(self,other):
        return not self.__eq__(other) and not self.__gt__(other)
           
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return (self.name, self.dict_of_activities, self.BMI)
        
    
class Spiritual(PersonalDevelopment, MixinPrint):
    
    def __init__(self, name, dict_of_activities, spiritual_views):
            super().__init__(name, dict_of_activities)
            self.spiritual_views = spiritual_views
        
    def __getitem__(self, activity):
        return self.dict_of_activities[activity]
        
    def __setitem__(self, activity, goal):
        self.dict_of_activities[activity] = goal
    
    def __iter__(self):
        return iter(self.dict_of_activities)
    
    def __delitem__(self, activity):
        del self.dict_of_activities[activity]
        
    def __len__(self):
        return len(self.dict_of_activities)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return super().__gt__(other)
    
    def __lt__(self,other):
        return not self.__eq__(other) and not self.__gt__(other)
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return (self.name, self.dict_of_activities, self.spiritual_views)

class Emotional(PersonalDevelopment, MixinPrint):
    
    def __init__(self, name, dict_of_activities, EQ):
            super().__init__(name, dict_of_activities)
            self.EQ = EQ
    
    def __getitem__(self, activity):
        return self.dict_of_activities[activity]
        
    def __setitem__(self, activity, goal):
        self.dict_of_activities[activity] = goal
    
    def __iter__(self):
        return iter(self.dict_of_activities)
    
    def __delitem__(self, activity):
        del self.dict_of_activities[activity]
        
    def __len__(self):
        return len(self.dict_of_activities)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return super().__gt__(other)
    
    def __lt__(self,other):
        return not self.__eq__(other) and not self.__gt__(other)
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return (self.name, self.dict_of_activities, self.EQ)
    

class Social(PersonalDevelopment, MixinPrint):
    
    def __init__(self, name, dict_of_activities, dict_of_friends):
            super().__init__(name, dict_of_activities)
            self.dict_of_friends = dict_of_friends
    
    def __getitem__(self, activity):
        return self.dict_of_activities[activity]
        
    def __setitem__(self, activity, goal):
        self.dict_of_activities[activity] = goal
    
    def __iter__(self):
        return iter(self.dict_of_activities)
    
    def __delitem__(self, activity):
        del self.dict_of_activities[activity]
        
    def __len__(self):
        return len(self.dict_of_activities)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return super().__gt__(other)
    
    def __lt__(self,other):
        return not self.__eq__(other) and not self.__gt__(other)
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return (self.name, self.dict_of_activities, self.dict_of_friends)
    

class Intellectual(PersonalDevelopment, MixinPrint):
        
    def __init__(self, name, dict_of_activities, field_of_interest):
        super().__init__(name, dict_of_activities)
        self.field_of_interest = field_of_interest
        
    def __getitem__(self, activity):
        return self.dict_of_activities[activity]
        
    def __setitem__(self, activity, goal):
        self.dict_of_activities[activity] = goal
    
    def __iter__(self):
        return iter(self.dict_of_activities)
    
    def __delitem__(self, activity):
        del self.dict_of_activities[activity]
        
    def __len__(self):
        return len(self.dict_of_activities)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return super().__gt__(other)
    
    def __lt__(self,other):
        return not self.__eq__(other) and not self.__gt__(other)
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return (self.name, self.dict_of_activities, self.field_of_interest)

class DomainsCollection():
    
    def __init__(self, name, domains_collection):
        self.name = name
        self.domains_collection = domains_collection
        
    def __getitem__(self, index):
        return self.domains_collection[index]

    def __len__(self):
        return len(self.domains_collection)
    
    def __str__(self):
        domains_names_list = []
        for domain in self.domains_collection:
            domains_names_list.append(domain.name)
        return (f'{self.name} contains the following domains: {domains_names_list}')
    
    def __repr__(self):
        return (self.name, self.domains_collection)

def i_am_a_decorator(function):
    def inner_function(*args):
        printing_list = function(*args)
        for (domain, status) in printing_list:
            if status == 'equal':
                print(f'\u001b[32m\u2b9e\u001b[0m Congrats! You reached your goal on {domain}! Keep up the good work! ')
            elif status == 'greater':
                print(f'\u001b[36m\u2b9d\u001b[0m Wow! You exceeded the expectations on {domain}! Keep it all in equilibrium! ')
            else:
                print(f'\u001b[31m\u2b9f\u001b[0m You did not reach your goal this week on {domain}! Level up next week!')
        return function
        
    return inner_function
    
@i_am_a_decorator
def check_status (desired_state_collection, actual_state_collection):
    printing_list = []
    for index in range(5):
        if desired_state_collection[index] == actual_state_collection[index]:
            printing_list.append((desired_state_collection[index].name, 'equal'))
        elif desired_state_collection[index] > actual_state_collection[index]:
            printing_list.append((desired_state_collection[index].name, 'lesser'))
        else:
            printing_list.append((desired_state_collection[index].name, 'greater'))
    return printing_list
        
        
    

