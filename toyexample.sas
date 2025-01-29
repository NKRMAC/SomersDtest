data example;
    input x y;
    datalines;
1 1
2 3
3 3
4 5
5 4
;
run;

proc logistic data=example;
    model y = x;
    ods output Association=assoc;
run;

proc print data=assoc;
run;

proc freq data=example;
  tables y*x / measures;
run;
