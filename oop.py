class cricket:
    format="test"
    def __init__(self,country,time):
        self._country=country
        self.time=time
class subcricket(cricket):        
    def show(self):
        print(self._country)   
        
match=subcricket(*input().split(","))
print(match.format)
match.show()
print(match.time)