# permutation-flowshop
Genetic algorythm for the permutation flowshop problem implemented in python

Flow shop scheduling problems are scheduling problems in which the flow control shall enable an appropriate sequencing for each job and for processing on a set of machines or with other resources 1,2,...,m in compliance with given processing orders. It maintains the constant flow of processing jobs is preferred with a minimum of idle time and a minimum of waiting time. A flowshop consists of M machines in series and N
different jobs available for processing at time zero. Each machine can handle only one job at a time. Each job is continuously processed on M available machines in the same technological order.

### Hypothesis
We consider a problem where there are m independent machines, non-preemptive scheduling and zero release time for all jobs, so jobs can be executed at any time and without interruption. The scheduling model can be modeled as follows:
F_m || C_max
