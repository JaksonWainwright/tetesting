class Proc_Status:
    def __init__(self):
        self.null = None

    def get_proc_status(self):
        with open('proc_statuses.txt', 'r') as proc_status_file:
            return proc_status_file.read()

    def update_proc_statuses(self, update_values):
        with open('proc_statuses.txt', 'w+') as proc_status_file:
            proc_status_file.write(update_values)

    def parse_proc_status(self):
        current_proc_statuses = self.get_proc_status()
        buffer = []
        i = 1
        for item in current_proc_statuses:
            if item == '1':
                buffer.append(f'Database Cluster {i} Query Success')
            else:
                buffer.append(f'Database Cluster {i} Query Failure')
            i += 1
        return ' '.join(buffer)
