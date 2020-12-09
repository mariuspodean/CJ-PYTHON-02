#nu mai stiu cum am rezolvat asta: https://python.scoalainformala.ro/lecture_notes/Lesson_8/Lesson_8.html#mutable-default-parameters-example-of-a-painfull-bug
#e ok asa?

def save_city_and_poi(name, poi=None):
    if not poi:
        poi = []
    poi.append(f'Primaria {name}')
    print(f'{name},{poi}')
  

save_city_and_poi('Bucuresti', ['Teatru', 'Muzeu'])
save_city_and_poi('Cluj-Napoca')
save_city_and_poi('Oradea')