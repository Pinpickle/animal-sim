import draw_sim
import sim
import csv_sim

CONFIG = sim.Config(
    # The chance that, each year, any given animal will die
    death_rate=0.2,
    # The chance that a female has of giving birth each year
    birth_chance=1,
    # The chance that a new male will die
    male_birth_mortality=0.2,
    # The chance that a new female will diea
    female_birth_mortality=0.2,
    # The max age of an animal before it "dies of old age"
    max_age=20
)

START_ANIMALS = sim.create_babies(25, 'f') + sim.create_babies(25, 'm')

## Uncomment out to draw the sim
draw_sim.run_and_draw_sim(START_ANIMALS, CONFIG)

## Uncomment out to run the sim and save to csv
# csv_sim.run_and_save_sim(START_ANIMALS, CONFIG, years=100, filename="sim.csv")
