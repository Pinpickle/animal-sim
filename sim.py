from collections import namedtuple
from random import random, choice

FIELD_SIZE = 100

Animal = namedtuple('Animal', ['x', 'y', 'sex', 'age'])
Config = namedtuple('Config', [
    'male_birth_mortality',
    'female_birth_mortality',
    'death_rate',
    'birth_chance',
    'max_age',
])

SEXES = ['m', 'f']

def random_animal(sex = None):
    if sex == None:
        sex = choice(SEXES)
    return Animal(x=FIELD_SIZE * random(), y=FIELD_SIZE * random(), sex=sex, age=0)

def create_babies(count, sex):
    return [random_animal(sex=sex) for _ in range(count)]

def step_sim(animals, config):
    def should_animal_live(animal):
        return (random() > config.death_rate) and (animal.age < config.max_age)

    def kill_animals(animals):
        return filter(should_animal_live, animals)

    new_animals = []

    for animal in kill_animals(animals):
        if (animal.sex == 'f') and (animal.age >= 2) and (random() < config.birth_chance):
            new_animal = random_animal()
            death_roll = random()
            if (((death_roll > config.male_birth_mortality) and (new_animal.sex == 'm')) or
                    ((death_roll > config.female_birth_mortality) and (new_animal.sex == 'f'))):
                new_animals.append(new_animal)

        new_animals.append(animal._replace(age=animal.age + 1))

    return new_animals
