class Birds:
    def __init__(self):
        self.members = ['Eagle', 'Parrot', 'Sparrow']

    def printMembers(self):
        print('Birds:', ', '.join(self.members))
