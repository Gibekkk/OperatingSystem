class Process:
    def __init__(self, PID, arrival_time, burst_time):
        self.PID = PID
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.remaining_time = burst_time
        self.complete_time = 0
        self.turn_around_time = 0