import os 
from utils import getNumberInRange

class Person:
    def __init__(self, user_id: int) -> None:
        self._user_id = user_id
        self._name = input("Name: ")
        self._age = getNumberInRange("Type the age", "Age", 0, 120)
    
    def getId(self) -> int:
        return self._user_id
    
    def getType(self) -> str:
        return "Person"

    def getName(self) -> str:
        return self._name

    def getAge(self) -> int:
        return self._age
    
    def toCsvRow(self) -> dict:
        data = {
            "user_id": self._user_id,
            "name": self._name,
            "age": self._age,
            "type": self.getType()
        }
        return data
    
    def displayProfile(self, single_line: bool = False) -> None:
        try:
            if single_line:
                print("ID: " + str(self._user_id) + " | Name: " + self._name + " | Age: " + str(self._age), end="") 
            else:
                print("ID: " + str(self._user_id))
                print("Name: " + self._name)
                print("Age: " + str(self._age))
        except TypeError as e:
            print("Error: Failed to display profile - Invalid data type:", str(e))
        except Exception as e:
            print("Error: Failed to display profile:", str(e))

if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))