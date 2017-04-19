import draw_sim
import sim
import csv_sim

CONFIG = sim.Config(
    death_rate=0.1,
    birth_chance=0.5,
)

START_ANIMALS = sim.create_babies(50)

## Uncomment out to draw the sim
# draw_sim.run_and_draw_sim(START_ANIMALS, CONFIG)

## Uncomment out to run the sim and save to csv
csv_sim.run_and_save_sim(START_ANIMALS, CONFIG, years=100, filename="sim.csv")