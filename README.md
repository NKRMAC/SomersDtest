# Somers' D test

## Python

OK, her er et program der genererer nogle tilfældige data til at teste Somers' D beregninger.

Programmet kan enten generere data (`gen = True`) eller indlæse en csv-fil (Eksempel vedlagt).

Data grupperes og køres igennem både `scipy.stats.somersd(x,y)`, hvor `x` er uafhængig og `y` er afhængig. Herudover laves en manuel beregning. Som det ses, er resultaterne ens. Jeg får i hvert fald lige nu:
```
Somers' D on grouped data: 0.3605724332358525
Manual Somers' D: 0.3605724332358525
```

Der defineres også et binary target (`y_binarized`), og Somers' D beregnes for rangordningsevnen af `x` (grupperet) for dette target. Jeg får:
```
Somers' D on binary target: 0.23608705755461923
Manual Somers' D: 0.23608705755461923
```
for samme syntaks som før (`scipy.stats.somersd(x,y)`) og manuel beregning. Hvis jeg i stedet vender syntaksen (`scipy.stats.somersd(y,x)`) som vi snakkede om var en mulighed, får jeg nu:
```
Somers' D on binary target: 0.5168007140663391
Manual Somers' D: 0.5168007140663391
```

## SAS

Så ligger der også et SAS-program, der gør det samme. Programmet suger csv-filen direkte fra Github.

### PROC LOGISTIC (Binært tilfælde)

Her bruges `PROC LOGISTIC` til at beregne Somers' D for det binære target. Jeg får et Somers' D på 0.516801, hvilket svarer til at bytte variablene om i Python.

### PROC FREQ (Grupperet tilfælde)

Her er jeg ikke nået **så** langt. Jeg kan godt køre PROC FREQ, men jeg er ikke helt sikker på, hvad der sker.

Hvis jeg kører det her:
```
PROC FREQ 
    DATA=somersd           
    NOPRINT;
          TABLES x_group * y_group / MEASURES;
          OUTPUT OUT=somersdout
          (KEEP = _SMDCR_
          RENAME = (_SMDCR_ = somers_d))
          MEASURES;
RUN;
```
Så får jeg Somers' D = 0.3605724332, men eftersom jeg ikke helt forstår, syntaksen, så ved jeg ikke, hvad det er et argument for.

## Næste skridt

Jeg skal have kørt datasættet igennem vores custom Somers' D makroer og set, hvad der sker...