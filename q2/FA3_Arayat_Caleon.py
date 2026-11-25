from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading():
        pass

class PHSensor(Sensor):
    def __init__(self, name):
        self.name = name
    def get_reading(self):
        return "7.2 pH (Neutral)"
    
class TempSensor(Sensor):
    def __init__(self, name):
        self.name = name
    def get_reading(self):
        return "24.5°C"

sensor1 = PHSensor("pH")
sensor2 = TempSensor("Temperature")
iterator = [sensor1, sensor2]

print("--- Lab Inventory System ---")
for iteration in iterator:
    print(f"[{iteration.name} Sensor] Reading: {iteration.get_reading()}")

print("\n"+("-")*28)
#sensor3 = Sensor()
#sensor3.get_reading()