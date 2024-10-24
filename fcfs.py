class Process:
    def __init__(self, PID, arrival_time, burst_time):
        self.PID = PID
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = None
        self.remaining_time = burst_time
        self.complete_time = None
        self.turn_around_time = None

processes = [
    Process("P1", 2, 8),
    Process("P2", 0, 4),
    Process("P3", 1, 9),
    Process("P4", 3, 5),
    Process("P5", 4, 4),
    ]

def fcfs(processes):
    time = 0
    queue = []
    while len(queue) < len(processes):
        for process in processes:
            if process.arrival_time == time:
                queue.append(process.PID)
        time+=1
    time = 0

    for PID in queue:
        for process in processes:
            if process.PID == PID:
                if process.remaining_time > 0:
                    process.waiting_time = time-process.arrival_time
                    process.turn_around_time = time
                    while process.remaining_time > 0:
                        time+=1
                        process.remaining_time-=1
    return processes

def prints(processes):
    for process in processes:
        print(f"process: {process.PID}, arrival_time: {process.arrival_time}, burst_time: {process.burst_time}, remaining_time: {process.remaining_time}, waiting_time: {process.waiting_time}, turn_around_time: {process.turn_around_time}")

prints(fcfs(processes))