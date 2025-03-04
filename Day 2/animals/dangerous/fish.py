class Fish:
    def __init__(self):
        self.members = ["Salmon", "Tuna", "Shark"]

    def printMembers(self):
        print("Printing fish:")
        for member in self.members:
            print("\t" + member)
