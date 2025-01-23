# Somers' D test

OK, her er et program der genererer nogle tilfældige data til at teste Somers' D beregninger.

Programmet kan enten generere data (`gen = True`) eller indlæse en csv-fil (Eksempel vedlagt).

Data grupperes og køres igennem både `scipy.stats.somersd` og en manuel beregning. Som det ses, er resultaterne ens. Jeg får i hvert fald lige nu:
```
Somers' D on grouped data: 0.3605724332358525
Manual Somers' D: 0.3605724332358525
```