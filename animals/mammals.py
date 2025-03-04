# mammals.py
class Mammals:
    def __init__(self):
        """Constructor"""
        self.members = ["Tiger", "Elephant", "Wild Cat"]

    def printMembers(self):
        print("Printing mammals:")
        for member in self.members:
            print("\t" + member)
