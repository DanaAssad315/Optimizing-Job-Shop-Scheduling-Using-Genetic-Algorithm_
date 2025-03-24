Genetic Algorithm for Job Shop Scheduling

1. Project Overview
This project implements a scheduling system using a Genetic Algorithm (GA) to optimize job shop scheduling in a manufacturing environment. The system determines the optimal sequence and timing for each job, aiming to minimize production time and maximize throughput.

2. How Genetic Algorithm Works?

A genetic algorithm is an AI-based optimization technique inspired by natural selection. It consists of:
- Population: A set of potential solutions.
- Chromosomes: Individual solutions in the population.
- Genes: Elements within a chromosome representing specific aspects of the solution.
- Fitness Function: Evaluates the effectiveness of each solution.
- Genetic Operators: Improve offspring quality using selection, crossover, and mutation.
- Selection Process: Chooses individuals for reproduction based on their fitness.

3. Algorithm Workflow

* Initialization: Generate an initial population of schedules.

* Fitness Assignment: Evaluate the fitness of each schedule.

* Selection: Choose the best schedules for reproduction.

* Reproduction: Apply crossover and mutation to generate new schedules.

* Termination: Repeat the process until a termination condition is met.

Problem Formulation
Chromosome Representation: Each chromosome is a list of job sequences, where each job consists of multiple operations.
Crossover: Exchanges subsequences between parent chromosomes to produce better offspring.
Mutation: Introduces diversity by swapping operations within a chromosome.
Objective Function: Evaluates the efficiency of a generated schedule and aims to minimize total completion time.


Course: Artificial Intelligence (ENCS3340)
Department: Electrical & Computer Engineering
Faculty: Faculty of Engineering & Technology/ BirzeitUniversity 

Date: May 20, 2024

