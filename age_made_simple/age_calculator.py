from datetime import datetime

class AgeCalculator:
    """
    This program calculates a person's age based on their date of birth and return the day of the week they were born. 
    """
    def calculate_age(self, date_of_birth: str) -> int:
        """
        Calculate the age based on the provided date of birth.
        Returns:
            int: the calculated age.
        """
        # Validate the provided date
        formatted_date = date_format_validator(date_of_birth)
        
        # Get the current date
        current_date = datetime.now()
        
        # Calculate the age
        age = current_date.year - formatted_date.year - ((current_date.month, current_date.day) < (formatted_date.month, formatted_date.day))
        
        return age

    def day_of_week(self, date_of_birth: str) -> str:
        """
        Determine the day of the week the person was born based on the provided date of birth.
        Returns:
            str: the day of the week the person was born.
        """
        # Validate the provided date
        formatted_date = date_format_validator(date_of_birth)
        
        # Get the day of the week as an integer (0 = Monday, 6 = Sunday)
        day_index = formatted_date.weekday()

        # Define a list of days of the week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Get the day of the week as a string
        day_name = days_of_week[day_index]

        return day_name
    
    def get_birth_details(self, date_of_birth: str) -> None:
        """
        Display both the calculated age based on the provided date of birth and return the day of the week the person was born.
        """
        # Calculate age and day of the week
        age = self.calculate_age(date_of_birth)
        day_name = self.day_of_week(date_of_birth)

        print(f"\nYou are {age} years old and you were born on a {day_name}.\n\n")
        

def date_format_validator(date: str):
    """
    Args:
        date (str): use this format YYYY-MM-DD.
    """
    try:
        # Convert the input string to a datetime object
        return datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("\nInvalid date of birth format. Please use this format: 'YYYY-MM-DD'.\n")

if __name__ == "__main__":
    # Input date of birth in the format 'YYYY-MM-DD'
    date_of_birth_str = input("\nEnter your date of birth (YYYY-MM-DD): ")

    # Create an instance of the AgeCalculator class
    calculator = AgeCalculator()

    # Calculate age and day of the week
    age = calculator.calculate_age(date_of_birth_str)
    day_name = calculator.day_of_week(date_of_birth_str)

    print(f"\nYou are {age} years old.")
    print(f"You were born on a {day_name}.")
    
    # Display age and day of the week at once
    calculator.get_birth_details(date_of_birth_str)
