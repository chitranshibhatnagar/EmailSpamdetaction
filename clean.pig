enron = LOAD 'enron_dataset.txt' USING PigStorage(',') as (message:chararray, from:chararray, to:chararray, subject:chararray);
enron = DISTINCT enron;
sub_enron = LIMIT enron 5;
DUMP sub_enron
filtered_enron = FILTER enron BY subject != '';
filtered_enron_2 = LIMIT filtered_enron 5;
DUMP filtered_enron_2;
STORE filtered_enron_2 INTO 'enron_filtered_dataset.txt' USING PigStorage(',');
