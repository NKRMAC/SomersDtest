# Somers' D test

OK, her er et program der genererer nogle tilfældige data til at teste Somers' D beregninger.

Programmet kan enten generere data (`gen = True`) eller indlæse en csv-fil (Eksempel vedlagt).

Data grupperes og køres igennem både `scipy.stats.somersd` og en manuel beregning. Som det ses, er resultaterne ens. Jeg får i hvert fald lige nu:
```
Somers' D on grouped data: 0.3605724332358525
Manual Somers' D: 0.3605724332358525
```

Der defineres også et binary target (`y_binarized`), og Somers' D beregnes for rangordningsevnen af `x` (grupperet) for dette target. Jeg får:
```
Somers' D on binary target: 0.23608705755461923
Manual Somers' D: 0.23608705755461923
```
for samme syntaks som før (`scipy.stats.somersd(x,y)`) og manuel beregning. Hvis jeg i stedet vender syntaksen som vi snakkede om var en mulighed, får jeg nu:
```
Somers' D on binary target: 0.5168007140663391
Manual Somers' D: 0.5168007140663391
```
