from person import Person
from utils import getNumberInRange
import os

class Student(Person):
    def __init__(self, person: Person) -> None:
        self._user_id = person._user_id
        self._name = person._name
        self._age = person._age
        
        print("Select Field of Study:")
        field_of_study_options: list[str] = [
            "Software Development", "Electrical Engineering", "Medicine",
            "Business Administration", "Mechanical Engineering", "Psychology"
        ]
        for index, field in enumerate(field_of_study_options, start=1):
            print(str(index) + ". " + field)
        field_choice: int = getNumberInRange("Enter choice", "Field of Study", 1, len(field_of_study_options))
        self._field_of_study: str = field_of_study_options[field_choice - 1]
        self._year_of_study: int = getNumberInRange("Year of Study", "Year", 1, 10)
        self._score_avg: int = getNumberInRange("Average Score (stored as an integer)", "Average Score", 0, 100)

    def getType(self) -> str:
        return "Student"

    def getFieldOfStudy(self) -> str:
        return self._field_of_study 
    
    def getYearOfStudy(self) -> int:
        return self._year_of_study
    
    def getScoreAvg(self) -> int:
        return self._score_avg
    
    def toCsvRow(self) -> dict:
        data = super().toCsvRow()
        data.update({
            "field_of_study": self.getFieldOfStudy(),
            "year_of_study": int(self.getYearOfStudy()),
            "avg_score": int(self.getScoreAvg())
        })
        return data

    def displayProfile(self, single_line: bool = False) -> None:
        super().displayProfile(single_line) 
        if single_line:
            print(" | Student in " + self._field_of_study + " (Year: " + str(self._year_of_study) + ", Avg Score: " + str(self._score_avg) + ")", end="")
        else:
            print("He is a student in the field of study of " + self.getFieldOfStudy() + ".")
            print("The year of study is " + str(self.getYearOfStudy()) + " and the average score is " + str(self.getScoreAvg()) + ".")

if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))
