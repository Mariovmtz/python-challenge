"""------------------------------------------------------------------
PyBank
Mario Vicente Martinez E.
2020-04-13
------------------------------------------------------------------"""
import os, csv, operator

def updateAmount(resultDic:dict, key:str, op, chgAvg:float, monthName:str) -> None:
    if op(resultDic[key]['amount'] ,chgAvg):
        resultDic[key]['month_name'] = monthName
        resultDic[key]['amount'] = chgAvg
#--------------------------------------------

def outputResult(resultDic:dict) -> str:
    rstr = f"Financial Analysis {os.linesep}"
    rstr = f"{rstr}---------------------------------- {os.linesep}"
    rstr = f"{rstr}Total months: {resultDic['total_months']} {os.linesep}"
    rstr = f"{rstr}Total : ${resultDic['net_amount']} {os.linesep}"
    rstr = f"{rstr}Average Change : ${resultDic['changes_avg']} {os.linesep}"
    rstr = f"{rstr}Greatest Increase in Profits: {resultDic['greatest_inc']['month_name']} (${resultDic['greatest_inc']['amount']}) {os.linesep}"
    rstr = f"{rstr}Greatest Decrease in Profits: {resultDic['greatest_dec']['month_name']} (${resultDic['greatest_dec']['amount']}) {os.linesep}"
    return rstr
#--------------------------------------------
def writeToFile(FileName:str, outputStr:str) -> None:
    outFile = os.path.join("analysis/" ,FileName + ".txt")
    
    with open (outFile, "w", encoding = 'utf-8') as out:
        out.write(outputStr)
#--------------------------------------------

# EXECUTION BEGINS HERE

results = {'total_months':0,
           'net_amount':0,
           'changes_avg':0,
           'greatest_inc':
                        {'month_name':'',
                         'amount':0},
           'greatest_dec':
                        {'month_name':'',
                         'amount':0}
        }

budget_csv = os.path.join("Resources/","budget_data.csv")

with open (budget_csv, encoding = 'utf-8') as csvFile:
    reader = csv.reader(csvFile, delimiter = ",")

    next(reader)
    last_amount = 0

    for row in reader:
        month_name = row[0]
        current_amount = float(row[1])
        current_change_avg = 0

        results['total_months'] += 1
        results['net_amount'] += current_amount

        if results['total_months'] != 1:
            current_change_avg = current_amount  - last_amount
            results['changes_avg'] += current_change_avg
        
        updateAmount (results, 'greatest_inc', operator.lt, current_change_avg, month_name)
        updateAmount (results, 'greatest_dec', operator.gt, current_change_avg, month_name)
  
        last_amount = current_amount

results['changes_avg'] = round(results['changes_avg'] / (results['total_months'] - 1),2)

print(outputResult (results))
writeToFile ("analysis", outputResult (results))
# EXECUTION ENDS HERE

