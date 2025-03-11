class Fish:
    def __init__(self):
        self.members = ['Salmon', 'Goldfish', 'Shark']

    def printMembers(self):
        print('Fish:', ', '.join(self.members))
