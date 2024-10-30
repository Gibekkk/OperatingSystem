def prints(processes, worksheet):
    i = 1
    worksheet.write(f'A{i}', f"process")
    worksheet.write(f'B{i}', f"arrival_time")
    worksheet.write(f'C{i}', f"burst_time")
    worksheet.write(f'D{i}', f"remaining_time")
    worksheet.write(f'E{i}', f"waiting_time")
    worksheet.write(f'F{i}', f"complete_time")
    worksheet.write(f'G{i}', f"turn_around_time")
    for process in processes:
        i += 1
        worksheet.write(f'A{i}', f"{process.PID}")
        worksheet.write(f'B{i}', f"{process.arrival_time}")
        worksheet.write(f'C{i}', f"{process.burst_time}")
        worksheet.write(f'D{i}', f"{process.remaining_time}")
        worksheet.write(f'E{i}', f"{process.waiting_time}")
        worksheet.write(f'F{i}', f"{process.complete_time}")
        worksheet.write(f'G{i}', f"{process.turn_around_time}")
        
def display(processes):
    for process in processes:
        print(f"process: {process.PID}, arrival_time: {process.arrival_time}, burst_time: {process.burst_time}, remaining_time: {process.remaining_time}, waiting_time: {process.waiting_time}, complete_time: {process.complete_time}, turn_around_time: {process.turn_around_time}")
        
def fcfs(processes):
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrival_time == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.arrival_time < lowest.arrival_time and q.remaining_time > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remaining_time > 0:
                            lowest = q
                    else:
                        if q.arrival_time < lowest.arrival_time and q.remaining_time > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remaining_time -= 1
            running.turn_around_time += 1
            if running.remaining_time == 0:
                finishedJob += 1
                running.complete_time = time
                running = None
        
        for q in queue:
            q.waiting_time += 1
            q.turn_around_time += 1
        time += 1
    return processes

def sjfPree(processes):
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrival_time == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.remaining_time < lowest.remaining_time and q.remaining_time > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remaining_time > 0:
                            lowest = q
                    else:
                        if q.remaining_time < lowest.remaining_time and q.remaining_time > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remaining_time -= 1
            running.turn_around_time += 1
            if running.remaining_time == 0:
                finishedJob += 1
                running.complete_time = time
                running = None
        
        for q in queue:
            q.waiting_time += 1
            q.turn_around_time += 1
        time += 1
    return processes

def ljfPree(processes):
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrival_time == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                highest = running
                for q in queue:
                    if q.remaining_time > highest.remaining_time and q.remaining_time > 0:
                        highest = q
                if highest is not running:
                    queue.remove(highest)
                    queue.append(running)
                    running = highest
        else:
            if len(queue) > 0:
                highest = None
                for q in queue:
                    if highest is None:
                        if q.remaining_time > 0:
                            highest = q
                    else:
                        if q.remaining_time > highest.remaining_time and q.remaining_time > 0:
                            highest = q
                if highest is not None:
                    queue.remove(highest)
                    running = highest

        if running is not None:
            running.remaining_time -= 1
            running.turn_around_time += 1
            if running.remaining_time == 0:
                finishedJob += 1
                running.complete_time = time
                running = None
        
        for q in queue:
            q.waiting_time += 1
            q.turn_around_time += 1
        time += 1
    return processes

def sjfNonPree(processes):
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrival_time == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is None:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remaining_time > 0:
                            lowest = q
                    else:
                        if q.remaining_time < lowest.remaining_time and q.remaining_time > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remaining_time -= 1
            running.turn_around_time += 1
            if running.remaining_time == 0:
                finishedJob += 1
                running.complete_time = time
                running = None
        
        for q in queue:
            q.waiting_time += 1
            q.turn_around_time += 1
        time += 1
    return processes

def roundRobin(processes, quantum_time):
    counter = quantum_time
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):    
        if counter == 0:
            if running is not None:
                running.start_time = time
                queue.append(running)
                running = None
            counter = quantum_time
            
        for process in processes:
            if process.arrival_time == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.start_time < lowest.start_time and q.remaining_time > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remaining_time > 0:
                            lowest = q
                    else:
                        if q.start_time < lowest.start_time and q.remaining_time > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remaining_time -= 1
            running.turn_around_time += 1
            if running.remaining_time == 0:
                finishedJob += 1
                running.complete_time = time
                running = None
                counter = quantum_time + 1
        
        counter -= 1
        
        for q in queue:
            if q.remaining_time > 0:
                q.waiting_time += 1
                q.turn_around_time += 1
        
        time += 1
    return processes