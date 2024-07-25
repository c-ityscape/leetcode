class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        time = {}
        
        # Start time for the first task is 0
        prev_time = 0
        
        for i in range(len(logs)):
            employee_id = logs[i][0]
            leave_time = logs[i][1]
            
            # Calculate the duration of the current task
            duration = leave_time - prev_time
            
            # Update the dictionary with the maximum duration for each employee
            if employee_id in time:
                time[employee_id] = max(time[employee_id], duration)
            else:
                time[employee_id] = duration
            
            # Update the previous end time to the current end time
            prev_time = leave_time
        
        # Find the maximum time worked
        max_time = max(time.values())
        
        # Find the smallest employee ID with the maximum time worked
        hardest_worker_id = min(emp_id for emp_id, t in time.items() if t == max_time)
        
        return hardest_worker_id
