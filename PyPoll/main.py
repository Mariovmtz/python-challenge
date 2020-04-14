"""------------------------------------------------------------------
PyPoll
Mario Vicente Martinez E.
2020-04-13
------------------------------------------------------------------"""
import os, csv

def outputResult(candidates:dict) -> str:
    winner = max(candidates, key=candidates.get)
    total_votes = sum(candidates.values())
    
    rstr = f"Election Results {os.linesep}"
    rstr = f"{rstr}----------------------------------{os.linesep}"
    rstr = f"{rstr}Total Votes: {total_votes}{os.linesep}" 
    rstr = f"{rstr}----------------------------------{os.linesep}" 

    for key, value in candidates.items():
        rstr = f"{rstr}{key}: {round(value / total_votes * 100,2)}% ({value}){os.linesep}" 

    rstr = f"{rstr}----------------------------------{os.linesep}" 
    rstr = f"{rstr}Winner: {winner}{os.linesep}" 
    rstr = f"{rstr}----------------------------------{os.linesep}"   
    return rstr
#--------------------------------------------
def writeToFile(FileName:str, outputStr:str) -> None:
    outFile = os.path.join("analysis/" ,FileName + ".txt")
    
    with open (outFile, "w", encoding = 'utf-8') as out:
        out.write(outputStr)
#--------------------------------------------

# EXECUTION BEGINS HERE

elections_csv = os.path.join("Resources/","election_data.csv")

with open (elections_csv, encoding = 'utf-8') as csvFile:
    next(csvFile) #SKIPPING 1ST ROW 
    #TRYING DICTREADER INSTEAD OF READER, THIS WILL SAVE EACH ROW IN A DICTIONARY AND NOT IN A LIST
    reader = csv.DictReader(csvFile, delimiter = ",")
    candidates = {}  

    for row in reader:
        current_candidate = row['Candidate']
        
        #Exclude records when candidate is None or Candidate = Candidate
        if current_candidate not in (None, "Candidate"):
        
            if not current_candidate in candidates:
                candidates[current_candidate] = 0

            candidates[current_candidate] += 1

print(outputResult(candidates))
writeToFile ("analysis", outputResult (candidates))
# EXECUTION ENDS HERE


    

