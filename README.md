# permutation-flowshop
Genetic algorythm for the permutation flowshop problem implemented in python

## Job scheduling con algoritmo genetico

Ci sono m macchine e n posti di lavoro. Ogni job contiene esattamente m operazioni. L'i-esima operazione del lavoro deve essere eseguita sulla i-esima macchina. Nessuna macchina può eseguire più di un'operazione contemporaneamente. Per ogni operazione di ogni lavoro, viene specificato il tempo di esecuzione.
Le operazioni all'interno di un lavoro devono essere eseguite nell'ordine specificato. La prima operazione viene eseguita sulla prima macchina, poi (quando la prima operazione è terminata) la seconda operazione sulla seconda macchina, e così via fino all'ennesima operazione. Tuttavia, i lavori possono essere eseguiti in qualsiasi ordine.
L'obiettivo è quello di completare tutti i job nel minore tempo possibile, ovvero minimizzare il makespan.

### Ipotesi iniziali
Si considera un problema dove ci sono m macchine indipendenti, scheduling non preemptive e tempo di rilascio nullo per tutti i job, quindi i job posso essere eseguiti in qualsiasi istante e senza interruzioni.
Il modello di scheduling può essere modellato nel modo seguente:
F_m || C_max
