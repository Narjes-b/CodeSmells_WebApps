from pydriller import RepositoryMining,GitRepository
from pprint import pprint
from datetime import date
#compute codechurn
from pydriller.metrics.process.code_churn import CodeChurn
import re

repos= GitRepository("/Users/bessghaiernarjess/Documents/PhD_ETS/git/joomla-cms")
#keywords = 29
Keywords = ["fix","fixed","fixes","fixing","close","closed","closes","closing","bug","bugs","error","errors",
            "defect","defects","issue","issues","failure","failures","crush","crushes","patch","patches","resolves",
            "resolved","resolving","solve","solving","solves","solved"]

i=0
i1=0  
ch=""
ch1=""
NbBugs=0
NbFiles=0

fix=0
fixed=0
fixes=0
fixing=0
close=0
closed=0
closes=0
closing=0
bug=0
bugs=0
error=0
errors=0
defect=0
defects=0
issue=0
issues=0
failure=0
failures=0
crush=0
crushes=0
patch=0
patches=0
resolves=0
resolved=0
resolving=0
solve=0
solving=0
solves=0
solved=0

nbCommits=0
BuggyCommits=""
FirstCommit="00d8ab3abd2558501592dc73fecfbe46bb56522f"
CurrentCommit="e5dc4beb39b7edbbd4eec187dad7162798b77da2"
FoundKeywords=""

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())  
      #all modified files in every Commit between two Releases
for Commit in RepositoryMining("/Users/bessghaiernarjess/Documents/PhD_ETS/git/joomla-cms",from_commit=FirstCommit, 
                                to_commit=CurrentCommit, only_modifications_with_file_types=['.php']).traverse_commits():
   
     #WE IDENTIFY ALL MODIFIED FILES IN ONE SINGLE FAULT-FIXING COMMITS
     for modified_file in Commit.modifications:
       
        #for  c in Keywords:
         #  if c.lower() in Commit.msg:
            #CHECK IF KEYWORDS EXIST
       string=Commit.msg.lower()
       word = words_in_string(Keywords, string)
       s=list(word)
       for d in RepositoryMining("/Users/bessghaiernarjess/Documents/PhD_ETS/git/joomla-cms",single=FirstCommit).traverse_commits():
            #print("FirstCommit "+ d.committer_date.strftime("%Y-%m-%d"))   
            #AT LEAST ONE KEYWORD EXISTS, WITH PHP EXTENSION AND THE DATE IS SUPERIOR THAN THE FIRST RELEASE
        if len(s)!=0 and ".php" in modified_file.filename and Commit.committer_date>d.committer_date :
            code_churn=int(modified_file.added)+int(modified_file.removed)
            print('Hash= {} ** keyword= {} ** file_name= {} ** commit_date= {} LOC= {} Code Churn= {} (+{} , -{})'
                  .format(Commit.hash,s,modified_file.filename,Commit.committer_date.strftime("%Y-%m-%d"),modified_file.nloc,code_churn,modified_file.added,modified_file.removed))
            NbFiles+=1
            nbCommits+=1
            print(Commit.msg)
            
            if "fix" in s:fix+=1
            if "fixed" in s:fixed+=1
            if "fixes" in s:fixes+=1
            if "fixing" in s:fixing+=1
            if "close" in s:close+=1
            if "closed" in s:closed+=1
            if "closes" in s:closes+=1
            if "closing" in s:closing+=1
            if "bug" in s:bug+=1
            if "bugs" in s:bugs+=1
            if "error" in s:error+=1
            if "errors" in s:errors+=1
            if "defect" in s:defect+=1
            if "defects" in s:defects+=1
            if "issue" in s:issue+=1
            if "issues" in s:issues+=1
            if "failure" in s:failure+=1
            if "failures" in s:failures+=1
            if "crush" in s:crush+=1
            if "crushes" in s:crushes+=1
            if "patch" in s:patch+=1
            if "patches" in s:patches+=1
            if "resolves" in s:resolves+=1
            if "resolved" in s:resolved+=1
            if "resolving" in s:resolving+=1
            if "solve" in s:solve+=1
            if "solving" in s:solving+=1
            if "solves" in s:solves+=1
            if "solved" in s:solved+=1
#             
            #print(Commit.msg)
            #get files code modifications
             #== displays all code modifications
            #print(modified_file.diff)
            diff =modified_file.diff
            #print(diff)
            parsed_diff= repos.parse_diff(diff)
            #pprint(parsed_diff)
            
            #GET ALL BUGGY COMMITS
            bug_inducing_commits=repos.get_commits_last_modified_lines(Commit,modified_file)
            #print(bug_inducing_commits)
            BuggyCommits=bug_inducing_commits
            #print(BuggyCommits)
            
            #x = re.search("(?<=\')(.*?)(?=\')", str(BuggyCommits))
            #print(x)
            #match=re.findall("(?<=\')(.*?)(?=\')", str(BuggyCommits))
            match=re.findall("(?<=\ ')[a-zA-Z0-9 ]*", str(BuggyCommits)) 
            #print(match)
            match1=re.findall("(?<=\ {')[a-zA-Z0-9 ]*", str(BuggyCommits))
            #print(match1)
            
            NbBugs=len(match)+len(match1)
            
            print("Number of buggy commits before and after introduction of smells= "+ str(NbBugs))
#             for i in match: 
#               print(i)   
#             for i1 in match1: 
#               print(i1)
#           #EXTRACT ALL BUGGY COMMITS FROM THE LISTS
            if  NbBugs !=0:
            ##GET buggy commits date and difference with the fixing commits
              #for d in RepositoryMining("/Users/bessghaiernarjess/Documents/PhD_ETS/git/joomla-cms",single=FirstCommit).traverse_commits():
              print("FirstCommit "+ d.committer_date.strftime("%Y-%m-%d"))
              
              for i in match: 
                 for c in RepositoryMining("/Users/bessghaiernarjess/Documents/PhD_ETS/git/joomla-cms",single=i).traverse_commits():
                   
                   f_date = date(int(d.committer_date.strftime("%Y")), int(d.committer_date.strftime("%m")), int(d.committer_date.strftime("%d")))
                   l_date = date(int(c.committer_date.strftime("%Y")), int(c.committer_date.strftime("%m")), int(c.committer_date.strftime("%d")))
                   days = l_date-f_date 
                   #print(days.days)
                   for buggy_file in c.modifications:
               #EXTRACT THE CODE CHURN OF TARGETED FILE MODIFIED BY THE BUGGY COMMIT        
                    if buggy_file.old_path==modified_file.old_path:
                      code_churn_buggy=int(buggy_file.added)+int(buggy_file.removed)
                     #LOC=int(modified_file.nloc)+int(buggy_file.added)-int(buggy_file.removed)
                                            
               #MAKE SURE WE ONLY EXTRACT BUGS INTRODUCED AFTER THE INTRODUCION OF SMELLS
                      if c.committer_date>d.committer_date:
                       print('{} {}  {} days_till_first_bug_occurrence={} code_churn= {}'.format(c.hash,buggy_file.filename,c.committer_date.strftime("%Y-%m-%d"),days.days,code_churn_buggy))
              #print(i.author_date.strftime("%Y-%m-%d"))   
            
            
            
 

              for i1 in match1:
                 for c1 in RepositoryMining("/Users/bessghaiernarjess/Documents/PhD_ETS/git/joomla-cms",single=i1).traverse_commits():
 
                    f_date = date(int(d.committer_date.strftime("%Y")), int(d.committer_date.strftime("%m")), int(d.committer_date.strftime("%d")))
                    l_date = date(int(c1.committer_date.strftime("%Y")), int(c1.committer_date.strftime("%m")), int(c1.committer_date.strftime("%d")))
                    days = l_date-f_date 
                    #print(days.days)
                    for buggy_file1 in c1.modifications:
                     if buggy_file1.old_path==modified_file.old_path:   
                      code_churn_buggy1=int(buggy_file1.added)+int(buggy_file1.removed)
                     #LOC=int(modified_file.nloc)+int(buggy_file1.added)-int(buggy_file1.removed)
                      if c1.committer_date>d.committer_date:
                       print('{} {}  {} days_till_first_bug_occurrence= {} code_churn= {}'.format(c1.hash,buggy_file1.filename,c1.committer_date.strftime("%Y-%m-%d"),days.days,code_churn_buggy1))
              #print(i.author_date.strftime("%Y-%m-%d"))   
            
            NbBugs=0
            
            
            
            
            print("-----------------------------------------")
            print("-----------------------------------------")
            
            FoundKeywords=""
           #Count the frequency of keywrods use  

print("NbFiles= "+str(NbFiles))
print("nbCommits= "+str(nbCommits))
print("fix= "+str(fix))
print("fixed= "+str(fixed))
print("fixes= "+str(fixes))
print("fixing= "+str(fixing))
print("close= "+str(close))
print("closed= "+str(closed))
print("closes=" +str(closes))
print("closing=" +str(closing))
print("bug= "+str(bug))
print("bugs= "+str(bugs))
print("error= "+str(error))
print("errors= "+str(errors))
print("defect= "+str(defect))
print("defects= "+str(defects))
print("issue= "+str(issue))
print("issues= "+str(issues))
print("failure= "+str(failure))
print("failures= "+str(failures))
print("crush= "+str(crush))
print("crushes= "+str(crushes))
print("resolves= "+str(resolves))
print("resolved= "+str(resolved))
print("resolving= "+str(resolving))
print("solve= "+str(solve))
print("solved= "+str(solved))
print("solves= "+str(solves))
print("solving= "+str(solving))
print("patch= "+str(patch))
print("patches= "+str(patches))

           
