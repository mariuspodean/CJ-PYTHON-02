class University (object):
    def __init__(self, university_name, sort, location):
        self.university_name = university_name
        self.type = sort
        self.location = location
    
    def description (self):
        return f'The university {self.university_name} from {self.location}'
        
    
    def is_from_location(self, location):
        if self.location == location:
            return True
        else:
             return False

Asachi = University ("Gheorghe Asachi", "public", "Iasi")
UAIC = University ("Alexandra Ioan Cuza", "public", "Iasi")
BBolyai = University ("Babeș-Bolyai", "public", "Cluj-Napoca")
PAndrei= University ("Petre Andrei", "private", "Iasi")

print (Asachi.description())
print (UAIC.is_from_location('Iasi'))

class Faculty (University):
    def __init__(self, university_name, sort, location, faculty_name, nr_places, tax, duration):
        self.faculty_name = faculty_name
        self.nr_places = nr_places
        self.tax = tax
        self.duration = duration
        super().__init__(university_name, sort, location)

    def description (self):
       university_description = super().description()
       return f'{university_description}, Faculty {self.faculty_name}'
    
    def total_tax(self):
        return (self.tax * self.duration)

AC = Faculty ("Gheorghe Asachi", "public","Iasi", "Automatica si Calculatoare", 200, 5000, 4)
Filosofie = Faculty ("Alexandru Ioan Cuza", "public", "Iasi","Facultatea de Filosfie", 250, 1500, 3)
Drept = Faculty ("Petre Andrei", "private", "Iasi", "FAcultatea de Drept", 200, 3000, 4)

print (AC.description())
print (Filosofie.total_tax())

           
        


