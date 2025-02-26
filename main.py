import os
import pandas as pd 
from main_menu import MainMenu
from person import Person
from student import Student
from employee import Employee
from utils import getNumberInRange

def createAndSaveEntry(target_database: dict[int, Person], target_list: list[int]) -> int:
    try:
        if (user_id := getId(target_database)) == -1: return 0
        base_person = Person(user_id)
        person_types = [Student, Employee, Person]
        for index, person_type in enumerate(person_types, start=1):
            print(str(index) + ". " + person_type.__name__)    
        user_choice = getNumberInRange("Select type of person:\nEnter choice", "Choice", 1, len(person_types))
        final_person = base_person if person_types[user_choice - 1] == Person else person_types[user_choice - 1](base_person)
        target_database[user_id] = final_person
        target_list.append(user_id)
        print("ID [" + str(user_id) + "] saved successfully")
        return final_person.getAge()
    except Exception as e:
        print("Error while saving entry:", str(e))
        return 0
    
def getId(target_database) -> int:
    user_typed_id = getNumberInRange(what_is_fetched="Add new ID to the database", error_to_display="ID")
    if user_typed_id in target_database:
        print("Error: ID already exists " + str(target_database[user_typed_id]))
        return -1
    return user_typed_id
 
def searchById(source_dict: dict[int, Person]) -> None:
    user_id = getNumberInRange("Type the ID you would like to search", "ID")
    if user_id not in source_dict:
        print("Error: ID " + str(user_id) + " is not saved")
        return
    source_dict[user_id].displayProfile(single_line=False)
        
    
def displayUserDetailsById(person_id: int, source_dict: dict[int, Person]) -> None:
    if person_id not in source_dict:
        print("Error: ID " + str(person_id) + " is not found")
        return
    person: Person = source_dict[person_id]
    person.displayProfile(single_line=False)


def displayAllNames(source_dict) -> None:
    for index, person_id in enumerate(source_dict):
        person: Person = source_dict[person_id]
        print(str(index) + ". " + person.getName())


def displayAllIds(source_list) -> None:
    for i, user_id in enumerate(source_list):
        print(str(i) + ". " +str(user_id)) 


def displayAllEntries(source_dict: dict[int, Person], source_list: list[int]) -> None:
    for user_id in source_list:
        source_dict[user_id].displayProfile(single_line=True)
        print("\n", end="")


def getYesImSure() -> bool:
    while True:
        y_or_n = input("Are you sure? (y/n)")
        if y_or_n == "y":
            return True
        elif y_or_n == "n":
            return False
        

def requestToExit() -> bool:
    if getYesImSure() is True:
        print("Goodbye!")
        return True
    else:
        return False


def displayAgesAverage(sum_of_ages: int, list_of_ids: list[int]) -> None:
    try:
        average_age = sum_of_ages / len(list_of_ids)
        print("Average age: " + str(average_age))
    except ZeroDivisionError:
        print("Cannot calculate average: No entries in database")


def checkDatabaseExists(source_dict) -> bool:
    if not source_dict: 
        print("Error: Can't perform operation - Database is empty")
        return False 
    return True 


def displayEntryByIndex(source_list: list[int], source_dict: dict[int, Person], print_as_list: bool = False) -> None:
    try:
        max_index: int = len(source_list) - 1
        print("Valid index range: 0 to " + str(max_index))
        typed_index = getNumberInRange("Which index would you like to display", "Index")
        if not (0 <= typed_index < len(source_list)):
            raise IndexError("Index " + str(typed_index) + " is out of range (valid range: 0-" + str(max_index) + ")")
        
        person_id = source_list[typed_index]
        person: Person = source_dict[person_id]

        if print_as_list:
            print(str(typed_index) + ". " + str(person_id))
        else:
            person.displayProfile(single_line=False)
    except IndexError as e:
        print("Error:", str(e))


def getFileName(current_path: str) -> str:
    file_name = input("Type a name for the CSV file: ")
    
    if not file_name.endswith(".csv"):
        if file_name.endswith((".", ".c", ".cs")):
            file_name = file_name[:file_name.rfind(".")]
        file_name += ".csv"

    if fileExists(current_path, file_name):
        print(file_name + " already exists. If you proceed all previous data will be permanently lost.")
        if getYesImSure() is True:
            return file_name
        else:
            return getFileName(current_path) 
    return file_name


def writeToFile(user_database: dict[int, Person], current_path: str) -> bool:
    try:
        file_name: str = getFileName(current_path)
        data: list = []
        for person in user_database.values():
            data.append(person.toCsvRow())

        df = pd.DataFrame(data)
        
        output_path: str = os.path.join(current_path, file_name)
        
        directory: str = os.path.dirname(output_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(output_path, index=False)
        print("File saved successfully to " + output_path)
        return True
    except PermissionError as e:
        print("PermissionError: " + str(e))
        print("Please check your permissions for the directory: " + directory)
        return False
    except Exception as e:
        print("Couldn't write data to csv file: " + str(e))
        return False


def fileExists(current_path: str, file_name: str) -> bool:
    full_path = os.path.join(current_path, file_name)
    return os.path.exists(full_path)

    
def selectFromMenu() -> MainMenu:   
    for item in MainMenu:
        print(str(item.value) + ". " + str(item.name).replace("_", " ").title())
    
    return MainMenu(getNumberInRange("Please enter your choice", "Choice", 1, len(MainMenu)))

def main() -> None:
    try:
        user_database: dict[int, Person] = {}
        list_of_ids: list[int] = []
        sum_of_ages: int = 0 
        current_path: str = os.path.join(os.getcwd(), "")

        while True:
            choice = selectFromMenu()
            if choice == MainMenu.SAVE_NEW_ENTRY:
                sum_of_ages = sum_of_ages + createAndSaveEntry(user_database, list_of_ids)
            elif choice == MainMenu.SEARCH_BY_ID:
                if checkDatabaseExists(user_database) == True:
                    searchById(user_database)
            elif choice == MainMenu.PRINT_AGES_AVERAGE:
                if checkDatabaseExists(user_database) == True:
                    displayAgesAverage(sum_of_ages, list_of_ids)
            elif choice == MainMenu.PRINT_ALL_NAMES:
                if checkDatabaseExists(user_database) == True:
                    displayAllNames(user_database)
            elif choice == MainMenu.PRINT_ALL_IDS:
                if checkDatabaseExists(user_database) == True:
                    displayAllIds(list_of_ids)
            elif choice == MainMenu.PRINT_ALL_ENTRIES:
                if checkDatabaseExists(user_database) == True:
                    displayAllEntries(user_database, list_of_ids)   
            elif choice == MainMenu.PRINT_ENTRY_BY_INDEX:
                if checkDatabaseExists(user_database) == True:
                    displayEntryByIndex(list_of_ids, user_database, print_as_list=False)
            elif choice == MainMenu.SAVE_ALL_DATA:
                if not writeToFile(user_database, current_path):
                    print("Operation ended without writing to file")
            elif choice == MainMenu.EXIT:
                if requestToExit() == True:
                    break
            input("Press Enter to continue ")
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt. Exiting...")
        exit()
    except Exception as e:
        print("An unexpected error occurred:" + str(e))


if __name__ == "__main__":
    main()

