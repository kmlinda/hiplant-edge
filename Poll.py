class Poll:
    def __init__ (self, temp, moist, cond, light, poller, plantName, pollDate):
        self.temp = temp
        self.moist = moist
        self.cond = cond
        self.light = light
        self.poller = poller
        self.plantName = plantName
        self.pollDate = pollDate
    
    
    def show(self):
        print("{self.plantName}: Temperature: {self.temp} C - Moisture: {self.moist} - Conductivity: {self.cond} - Light: {self.light}")
    

    def save(self):
        print("persisting to database for {self.plantName}: Temperature: {self.temp} C - Moisture: {self.moist} - Conductivity: {self.cond} - Light: {self.light}")



