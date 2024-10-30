from Process import Process
from functions import *
import pandas as pd
import xlsxwriter as xlsx

data_output_path = 'Data/Output'
data_input_path = 'Data/Input'
debugPath = 'debugProcesses'
originalPath = 'processes'
debug = False

def run(process):
    workBookName = process + 'Output'
    processes = []
    data = pd.read_excel(f'{data_input_path}/{debugPath if debug else originalPath}.xlsx')
    for i in range(0, len(data)):
        processes.append(Process(data['PID'][i], data['arrival_time'][i], data['Burst_time'][i]))
        
    Workbook = xlsx.Workbook(f'{data_output_path}/{workBookName}.xlsx')
    Worksheet = Workbook.add_worksheet()
    
    results = None
    match process:
        case 'fcfs':
            results = fcfs(processes)
        case 'sjfNonPree':
            results = sjfNonPree(processes)
        case 'sjfPree':
            results = sjfPree(processes)
        case 'ljfPree':
            results = ljfPree(processes)
        case 'roundRobin':
            results = roundRobin(processes, 12)
            
    if results is not None:
        prints(results, Worksheet)
        
    Workbook.close()

print(f"{'Debugging Process Started:' if debug else 'Counting Process Started:'}")
run('fcfs')
run('sjfNonPree')
run('sjfPree')
run('ljfPree')
run('roundRobin')
print(f"Process Completed! Please Check The Outuput Folder In {data_output_path} Path!")