import os
import random
import time
import numpy as np


def calc_makespan(sequence, proccessing_time, number_of_jobs, number_of_machines):
   
    completion_times = [0] * number_of_jobs  #tempi di completamento dei job; si aggiorna attraversando tutte le macchine 

    for machine_no in range(0, number_of_machines):
        for slot in range(number_of_jobs):
            job_ct = completion_times[slot]
            if slot > 0:
                job_ct = max(completion_times[slot - 1], completion_times[slot])
            completion_times[slot] = job_ct + proccessing_time[sequence[slot]][machine_no]
    return completion_times[number_of_jobs - 1]

# inizializzazione popolazione
def initialize_population(population_size, number_of_jobs):
    population = []
    i = 0
    while i < population_size:
        individual = list(np.random.permutation(number_of_jobs))
        if individual not in population: #potrei generare più volte la stessa sequenza
            population.append(individual)
            i += 1
    return population

# incrocio sequenze
def crossover(parents):
    parent1 = parents[0]
    parent2 = parents[1]
    length_of_parent = len(parent1)
    first_point = int(length_of_parent / 2 - length_of_parent / 4)
    second_point = int(length_of_parent - first_point)
    intersect = parent1[first_point:second_point]

    child = []
    index = 0
    for pos2 in range(len(parent2)):
        if first_point <= index < second_point:
            child.extend(intersect)
            index = second_point
        if parent2[pos2] not in intersect: #potrei avere 2 volte lo stesso job nella sequenza
                child.append(parent2[pos2])
                index += 1

    return child

def mutation(solution):
    
    mutated_solution = list(solution)
    solution_length = len(solution)
    swap_positions = list(np.random.permutation(np.arange(solution_length))[:2])
    first_job = solution[swap_positions[0]]
    second_job = solution[swap_positions[1]]
    mutated_solution[swap_positions[0]] = second_job
    mutated_solution[swap_positions[1]] = first_job
    return mutated_solution

def get_max_makespan(population, processing_time, n_jobs, n_machines):
    max_value = 0
    for individual in population:
        value = calc_makespan(individual, processing_time, n_jobs, n_machines)
        if value > max_value:
            max_value = value
    return max_value

def get_fitness(population, processing_time, n_jobs, n_machines):
    fitness_list = []
    max_makespan = get_max_makespan(population, processing_time,  n_jobs, n_machines)
    for sequence in population:
        fitness_tuple = (max_makespan - calc_makespan(sequence, processing_time, n_jobs, n_machines), sequence)
        fitness_list.append(fitness_tuple)
    return fitness_list

def get_cumulated_fitnesses(fitness_list):
    cumulated_fitnesses = []
    total_fitness = 0
    for fitness_item in fitness_list:
        total_fitness += fitness_item[0]
        
    #print('fitness totale della popolazione: ')    
    #print(total_fitness)
    print('fitness cumulata per sequenza: ')
    
    fitness_sum = 0
    for fitness_item in fitness_list:
        fitness_sum += fitness_item[0]
        cumulated_fitness = fitness_sum/total_fitness
        print((cumulated_fitness, fitness_item[1]))
        cumulated_fitnesses.append((cumulated_fitness, fitness_item[1]))
        
    #print('cumulated_fitnesses:')
    #print(cumulated_fitnesses)
    
    return cumulated_fitnesses

def get_parents(population, processing_time, n_jobs, n_machines):
    fitness_list = get_fitness(population, processing_time, n_jobs, n_machines)
    cumulated_fitnesses = get_cumulated_fitnesses(fitness_list)
    cumulated_fitnesses.sort(key=lambda x: x[0])
    parents = []
    a = random.uniform(0,1)
    b = random.uniform(0,1)
    #print('')
    #print('a: ')
    #print(a)
    #print('b: ')
    #print(b)
    for cf in cumulated_fitnesses:
        if cf[0] > a:
            parents.append(cf[1])
            break
    for cf in cumulated_fitnesses:
        if cf[0] > b:
            parents.append(cf[1])
            break 
    print('\n')
    print('genitori selezionati:')
    print(parents[0])
    print(parents[1])
    print('\n')
    return parents

def update_population(population, children,processing_time,no_of_jobs,no_of_machines):
    costed_population = []
    for individual in population:
        ind_makespan = (calc_makespan(individual, processing_time, no_of_jobs, no_of_machines), individual)
        costed_population.append(ind_makespan)
    costed_population.sort(key=lambda x: x[0], reverse=True)

    costed_children = []
    for individual in children:
        ind_makespan = (calc_makespan(individual, processing_time, no_of_jobs, no_of_machines), individual)
        costed_children.append(ind_makespan)
    costed_children.sort(key=lambda x: x[0])
    for child in costed_children:
        if child not in population:
            population.append(individual)
            population.remove(costed_population[0][1])
            break