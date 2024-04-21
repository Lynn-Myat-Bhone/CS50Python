class Vault:
    def __init__ (self, gallons=0,sickles=0,knuts=0):
        self.gallons = gallons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.gallons} Gallons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self,other): # operator overloading
        gallons = self.gallons + other.gallons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(gallons,sickles,knuts)
    

potter = Vault(100,20,30)
print(potter)

weasly = Vault(130,30,24)
print(weasly)

# totGal = potter.gallons + weasly.gallons
# totsick = potter.sickles + weasly.sickles
# totKnuts = potter.knuts + weasly.knuts

# total = Vault(totGal,totsick,totKnuts)
# print(total)

total = potter + weasly
print (total)