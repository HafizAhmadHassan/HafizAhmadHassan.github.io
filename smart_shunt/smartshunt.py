class smartshunt:

    def __init__(self, name: str):
        self.name = name
    
    def examine(self, nam: str):
        print("Patient  : %s name: is %s" % (self.name,nam))