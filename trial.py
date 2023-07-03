def makeClass():
    class Thermostat:
        def __init__(self, temp):
            self.temp = 5/9 * (temp - 32)

        def get_temperature(self):
            return self.temp

        def set_temperature(self, updated_temp):
            self.temp = updated_temp
        
    return Thermostat


Thermostat = makeClass()
thermos = Thermostat(76)
temp = thermos.get_temperature
thermos.temperature = 26
temp = thermos.temperature
print(temp)


