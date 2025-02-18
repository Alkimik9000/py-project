from person import Person
from utils import getNumberInRange
import os

class Employee(Person):
    def __init__(self, person: Person) -> None:
        self._user_id = person._user_id
        self._name = person._name
        self._age = person._age

        
        print("Select Field of Work:")
        field_of_work_options: list[str] = [
            "Software Engineering", "Healthcare", "Education",
            "Finance", "Construction", "Retail"
        ]
        for index, field in enumerate(field_of_work_options, start=1):
            print(str(index) + ". " + field)

        work_choice: int = getNumberInRange("Enter choice", "Field of Work", 1, len(field_of_work_options))
        self._field_of_work: str = field_of_work_options[work_choice - 1]

        self._salary: int = getNumberInRange("Salary", "Salary", 0, 1000000)

    def getType(self) -> str:
        return "Employee"

    def getFieldOfWork(self) -> str:
        return self._field_of_work
    
    def getSalary(self) -> int:
        return self._salary
    
    def toCsvRow(self) -> dict:
        data = super().toCsvRow()
        data.update({
            "field_of_work": self.getFieldOfWork(),
            "salary": int(self.getSalary())
        })
        return data
    
    def displayProfile(self, single_line: bool = False) -> None:
        super().displayProfile(single_line) 

        if single_line:
            print(" | Employee in " + self._field_of_work + " with a salary of $" + str(self._salary), end="") 
        else:
            print("He is an employee in the field of work of " + self.getFieldOfWork() + ".")
            print("His salary is $" + str(self.getSalary()) + ".")


if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))