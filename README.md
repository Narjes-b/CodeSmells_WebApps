# CodeSmells_WebApps

This is a replication package of the paper titled "A Longitudinal Exploratory Study on the Prevalence,Co-occurence, and Impact of Code Smells in WebApplications"

In this package you will find:

1- For every studied project, we provide the associated datasets including the LOC and code churn values for all smelly and non smelly files.

2- We provide in the folder "Script", the scripts we used to:

  (1) extract all files LOC, code churn, changes types, commits, and identify all bug-inducing commits related to every file. [FindingFault-Inducing-CommitsAndFault-Fixing-Comits.py]
  
  (2) the script to get all issues state and ID [FindingIssuesStateAndID.java].
  
  (3) the apriori algorithm implementation [AprioriAlgorithm.py]
  
  (4) the code smells occurrence frequency [CodeSmellsOccurrenceFrequency.py]

3- The OccAllApp.csv contain all types of code smells found in each smelly file of the 400+ studied releases.
