# birds.py
class Birds:
    def __init__(self):
        """Constructor"""
        self.members = ["Sparrow", "Robin", "Duck"]

    def printMembers(self):
        print("Printing birds:")
        for member in self.members:
            print("\t" + member)
