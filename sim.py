from collections import namedtuple
from random import random, choice

FIELD_SIZE = 100

Animal = namedtuple('Animal', ['x', 'y', 'sex', 'age'])
Config = namedtuple('Config', ['death_rate', 'birth_chance'])

GENDERS = ['m', 'f']

def random_animal():
    return Animal(x=FIELD_SIZE * random(), y=FIELD_SIZE * random(), sex=choice(GENDERS), age=0)

def create_babies(count):
    return [random_animal() for _ in range(count)]

def step_sim(animals, config):
    def kill_animals(animal):
        return filter(lambda _: random() > config.death_rate, animals)

    new_animals = []

    for animal in kill_animals(animals):

        if (animal.sex == 'f') and (animal.age >= 2) and (random() < config.birth_chance):
            new_animals.append(random_animal())

        new_animals.append(animal._replace(age=animal.age + 1))

    return new_animals
