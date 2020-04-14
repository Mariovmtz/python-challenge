"""------------------------------------------------------------------
PyBoss
Mario Vicente Martinez E.
2020-04-13
------------------------------------------------------------------"""
# If true returns first name before space, if false returns last name, if name do not contains space returns everything
def parseName(name:str, ret:bool) -> str:
    if " " in name and ret:
        name = name[:name.find(" ")]
    elif " " in name:
        name = name[name.find(" "):]
    return name
#---------------------------------------------
def parseDate(dateStr:str) -> str:
    dateStr = f"{dateStr[5:7]} / {dateStr[-2:]} / {dateStr[:4]} " 
    return dateStr
 #---------------------------------------------
def parseSsn(ssn:str) -> str:
    ssn = f"***-**-{ssn[-4:]}"
    return ssn

us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
import os, csv

employees_csv = os.path.join("Resources/","employee_data.csv")
outFile = os.path.join("employees_out.csv")

with open (employees_csv, encoding = 'utf-8') as csvFile:
    
    for _ in range(2):
        next(csvFile)

    reader = csv.reader(csvFile, delimiter = ",")
    
    with open (outFile, "w", encoding = 'utf-8') as out:  
        writer = csv.writer(out, delimiter = ",")
        headers = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
        writer.writerow(headers)
        
        for row in reader:
            if len(row) == 5 and row[0] != "Emp Id":
                new_row = []
                new_row.append(row[0])
                new_row.append(parseName(row[1], True))
                new_row.append(parseName(row[1], False))
                new_row.append(parseDate(row[2]))
                new_row.append(parseSsn(row[3]))
                new_row.append(us_state_abbrev.get(row[4],"Unknown"))
                writer.writerow(new_row)