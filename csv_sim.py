import csv
import sim

def run_and_save_sim(animals, config, years, filename):
    with open("results/" + filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Year', 'Count'])

        for year in range(years + 1):
            writer.writerow([str(year), str(len(animals))])
            animals = sim.step_sim(animals, config)
