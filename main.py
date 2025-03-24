import matplotlib.pyplot as plot
import random
from collections import defaultdict, namedtuple

# create machine tuple called Machine and has three attribute as shown below
Machine = namedtuple('Machine', ['job_id', 'machine_id', 'duration'])


class Job:
    def __init__(self, job_id, machine):
        self.job_id = job_id
        self.machine = machine


def user():
    """to accept the data from the user"""
    jobs = []
    id = int(input("Enter your job id or 0 to exit: "))
    while id != 0:
        machines = []
        m = int(input("Enter your machine number or 0 to finish this job: "))
        while m != 0:
            time = int(input("Enter the execution time for this machine: "))
            machines.append(Machine(id, m, time))
            m = int(input("Enter your machine number or 0 to finish this job: "))
        jobs.append(Job(id, machines))
        id = int(input("Enter your job id or 0 to exit: "))
    return jobs


def mutate(chromosome):
    """ get any two index randomly from the chromosome, one at variable i and the second one at ii """
    """ then change their places"""
    i, ii = random.sample(range(len(chromosome)), 2)
    temp = chromosome[i]
    chromosome[i] = chromosome[ii]
    chromosome[ii] = temp


def crossover(parent_i, parent_ii):
    """let part variable have a random value between 1 and the length of the parent -1 "due to the indexing"""
    if len(parent_i) > 1:
        part = random.randint(1, len(parent_i) - 1)
    else:
        part = 1
    child_i = parent_i[:part] + parent_ii[part:]
    child_ii = parent_ii[:part] + parent_i[part:]
    return child_i, child_ii


def population_initialization(size, jobs):
    """determine the initial population"""
    population = []  # an empty list to store the population
    for s in range(size):
        chromosome = []
        for j in jobs:
            chromosome.append(j.machine)
        random.shuffle(chromosome)  # randomize the order of chromosomes in a sequence
        population.append(chromosome)  # add the new chromosome to the population
    return population


def fitness_function(chromosome):
    """the objective function that determine the best children which will be thw new parents """
    end_time = defaultdict(int)  # creates a dictionary with default integer value 0
    next_time = defaultdict(int)
    plan = defaultdict(list)  # creates a dictionary with an empty list
    # determine the schedule of our machines
    for machine in chromosome:  # ************
        for m in machine:
            start_time = max(end_time[m.machine_id], next_time[m.job_id])
            time = start_time + m.duration  # like an end time of the operation
            end_time[m.machine_id] = time
            next_time[m.job_id] = time
            plan[m.machine_id].append((start_time, time, m.job_id))

    score = max(end_time.values())  # return the best value of the successor to be the new parent
    return score, plan


def genetic_algorithm(jobs, population_size, generations, mutation_rate=0.1):
    """in this function we evaluate the genetic algorithm"""
    population = population_initialization(population_size, jobs)
    best_fitness = float('inf')  # huge value => infinity
    best_chromosome = None  # any chromosome can be better than this one at the beginning

    for g in range(generations):
        fitness_population = []
        for chromosome in population:
            score, plan = fitness_function(chromosome)
            fitness = score
            fitness_population.append((chromosome, fitness))

            if fitness < best_fitness:
                best_fitness = fitness
                best_chromosome = chromosome
                best_schedules = plan

        # sort the population depend on the second element of the fitness_population list in the ascending order
        fitness_population.sort(key=lambda x: x[1])
        new_population = []

        while len(new_population) < population_size:
            # select the first part of the fitness_population list by determining the middle point of the list
            # then choose two values randomly from the list
            parent_i, parent_ii = random.choices(fitness_population[:population_size // 2], k=2)
            child_i, child_ii = crossover(parent_i[0], parent_ii[0])

            if random.random() < mutation_rate:  # random.random() chose a random value between 0 and 1
                mutate(child_i)
            if random.random() < mutation_rate:
                mutate(child_ii)

            new_population.extend([child_i, child_ii])

        population = new_population[:population_size]

    return best_chromosome, best_schedules


def plotting(plan):
    """plot the chart using matplotlib.pyplot library"""
    fig, ax = plot.subplots(figsize=(5, 5))  # creates a figure and an axis, With 5 wide and 5 tall
    mach = sorted(plan.keys())   # Sort the schedule according to Key value
    # Generate a list of colors"determined by the number of machines "
    col = plot.cm.viridis(range(0, 256, 256 // len(mach)))
    # for Loop iterates through each machine
    # i:machine index ,,, m:current machine number ,,, op: operations assigned to the current machine.
    for i, (m, op) in enumerate(plan.items()):
        for start, end, job_id in op:  # start, end, job_id >> Start and End time For each id_Job
            # create a horizontal bar for the operation
            ax.barh(y=m, width=end - start, left=start, height=0.4, color=col[i], edgecolor='black')
            ax.text(x=start + (end - start) / 2, y=m, s=f'J{job_id}', color='white', va='center', ha='center', fontdict={'fontname': 'Times New Roman', 'fontsize': 20, 'fontweight':'bold'})
    # add label for the axis:
    ax.set_xlabel('time', fontdict={'fontname': 'Times New Roman', 'fontsize': 20, 'fontweight':'bold'})
    ax.set_ylabel('machines', fontdict={'fontname': 'Times New Roman', 'fontsize': 20, 'fontweight':'bold'})
    ax.set_yticks([m for m in mach])
    ax.set_yticklabels([f'machines {m}' for m in mach], fontdict={'fontname': 'Times New Roman', 'fontsize': 15, 'fontweight':'bold'})
    # add title
    ax.set_title('JSSP AI Chart ^_^', fontdict={'fontname': 'Times New Roman', 'fontsize': 20, 'fontweight':'bold'})
    plot.tight_layout()
    plot.show()


def main():
    #jobs = user()

    jobs = [
        Job(1, [Machine(1, 1, 10), Machine(1, 2, 5), Machine(1, 4, 12)]),
        Job(2, [Machine(2, 2, 7), Machine(2, 3, 15), Machine(2, 1, 8)]),
        Job(3, [Machine(3, 1, 9), Machine(3, 3, 6), Machine(3, 4, 8)]),
        Job(4, [Machine(4, 2, 4), Machine(4, 1, 11), Machine(4, 3, 7)]),
        Job(5, [Machine(5, 4, 5), Machine(5, 2, 8), Machine(5, 3, 10)]),
        Job(6, [Machine(6, 3, 12), Machine(6, 1, 6), Machine(6, 2, 9)]),
        Job(7, [Machine(7, 4, 7), Machine(7, 3, 4), Machine(7, 1, 10)]),
        Job(8, [Machine(8, 2, 11), Machine(8, 4, 8), Machine(8, 3, 6)]),
        Job(9, [Machine(9, 1, 13), Machine(9, 2, 7), Machine(9, 3, 9)]),
        Job(10, [Machine(10, 3, 5), Machine(10, 4, 9), Machine(10, 1, 8)])
    ]

    best_solution, schedules = genetic_algorithm(jobs, population_size=100, generations=50)

    print("Best Schedule:")
    for machine, ops in schedules.items():
        for start, end, job_id in ops:
            print(f"Machine {machine}: Job {job_id} from {start} to {end}")

    print(f"Score: {max([end for ops in schedules.values() for _, end, _ in ops])}")
    plotting(schedules)


if __name__ == "__main__":
    main()
