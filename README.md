# Replication package

This is a replication package of the paper titled "A Longitudinal Exploratory Study on the Prevalence,Co-occurence, and Impact of Code Smells in Web Applications"

In this package you will find:

1. For every studied project, we provide the associated datasets including the LOC and code churn values for all smelly and non smelly files.

2. We provide in the folder ``Script``, the scripts we used to:
    - extract all files LOC, code churn, changes types, commits, and identify all bug-inducing commits related to every file. [``FindingFault-Inducing-CommitsAndFault-Fixing-Comits.py``](https://github.com/Narjes-b/CodeSmells_WebApps/blob/master/Scripts/FindingFault-Inducing-CommitsAndFault-Fixing-Comits.py)
    - the script to get all issues state and ID [``FindingIssuesStateAndID.java``](https://github.com/Narjes-b/CodeSmells_WebApps/blob/master/Scripts/FindingIssuesStateAndID.java).
    - the apriori algorithm implementation [``AprioriAlgorithm.py``](https://github.com/Narjes-b/CodeSmells_WebApps/blob/master/Scripts/AprioriAlgorithm.py)
    - the code smells occurrence frequency [``CodeSmellsOccurrenceFrequency.py``](https://github.com/Narjes-b/CodeSmells_WebApps/blob/master/Scripts/CodeSmellsOccurrenceFrequency.py)

3. The ``OccAllApp.csv`` contain all types of code smells found in each smelly file of the 400+ studied releases.
