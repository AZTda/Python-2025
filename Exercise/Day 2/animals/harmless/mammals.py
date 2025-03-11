class Mammals:
    def __init__(self):
        self.members = ['Elephant', 'Tiger', 'Bear']

    def printMembers(self):
        print('Mammals:', ', '.join(self.members))
