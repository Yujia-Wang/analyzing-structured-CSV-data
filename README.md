##  Aurthor: Yujia(BoBo) Wang
##  Date: 2017-09-21

##  Description:

This program has several functions to process and analyze CSV files.

## Function:

min <field>: return the minimum value of the data in the field.
Example:
>Enter Function and Field: min TotalPopulation
0

max <field>: return the maximum value of the data in the field.
Example:
>Enter Function and Field: max TotalPopulation
9947

avg <field>: return the average value of the data in the field.
Example:
>Enter Function and Field: avg TotalPopulation
33241

search <field> <value>: return all the information that matches the search requirement.
Example:
>Enter Function and Field: search ZipCode 90031
ZipCode: 90031 
TotalPopulation: 39316 
MedianAge: 33.5 
TotalMales: 19546 
TotalFemales: 19770 
TotalHouseholds: 11156 
AverageHouseholdSize: 3.49

range <field> <min> <max>: return all the information that matches the search requirement, and display in ascending order according to the field.
Example:
>Enter Function and Field: range TotalMales 3500 4000
-------------------
ZipCode: 90401 
TotalPopulation: 6722 
MedianAge: 37.8 
TotalMales: 3524 
TotalFemales: 3198 
TotalHouseholds: 4188 
AverageHouseholdSize: 1.49
-------------------
ZipCode: 93591 
TotalPopulation: 7285 
MedianAge: 30.9 
TotalMales: 3653 
TotalFemales: 3632 
TotalHouseholds: 1982 
AverageHouseholdSize: 3.67
-------------------
ZipCode: 90211 
TotalPopulation: 8434 
MedianAge: 40.6 
TotalMales: 3849 
TotalFemales: 4585 
TotalHouseholds: 3706 
AverageHouseholdSize: 2.28
-------------------
ZipCode: 91020 
TotalPopulation: 8415 
MedianAge: 40.2 
TotalMales: 3966 
TotalFemales: 4449 
TotalHouseholds: 3385 
AverageHouseholdSize: 2.43
-------------------

quit: quit the program.
