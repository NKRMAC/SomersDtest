%let proxy = http://webproxy.nykreditnet.net:8080;
%let url = https://raw.githubusercontent.com/NKRMAC/SomersDtest/master/somersd.csv;
%let output_file = somersd.csv;

/* Extract the path from &_SASPROGRAMFILE */
%let current_path=%substr(&_SASPROGRAMFILE, 1, %length(&_SASPROGRAMFILE) - %length(%scan(&_SASPROGRAMFILE, -1, /)));

%put &current_path.;

/* Construct the full file path */
%let full_path = &current_path/&output_file;

/* Use FILENAME PIPE to execute the curl command */
filename download pipe "curl -x &proxy -o &full_path &url";

/* Execute the command */
data _null_;
    infile download;
    input;
run;

/* Read the CSV file into a SAS dataset */
proc import datafile="&full_path"
    out=somersd
    dbms=csv
    replace;
    getnames=yes;
run;

/* Clean up */
filename download clear;


/* Use PROC LOGISTIC to calculate Somers' D directly for binarized variable */
ods output Association=assoc;
proc logistic data=somersd;
    model y_binarized(event='1') = x_group;
run;

/* Experimenting with PROC FREQ... */
PROC FREQ 
    DATA=somersd           
    NOPRINT;
          TABLES x_group * y_group / MEASURES;
          OUTPUT OUT=somersdout
          (KEEP = _SMDCR_
          RENAME = (_SMDCR_ = somers_d))
          MEASURES;
RUN;
