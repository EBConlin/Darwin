class Dashboard:
    def __init__(self):
        self.logs = []

    def update(self, data):
        self.logs.append(data)
        print(f'Dashboard updated: {data}')