"""
Group Members:
1. Leen  - 746007751
2. Trisha  - 753005593
3. Mohammed - 410001753

Manifesto:
- Mohammed: Implemnted Task 1 check_limit()
- Leen: Implemented Task 3 calculate_average_books() and Task 4 count_over_limit().
- Trisha: Implemented Task 2 process_borrowers().

"""
import csv


# Task 1 
def check_limit(borrowed):
    """
    Check the borrowing limit and returns the status message
    >>>check_limit(borrowed)
    Parameters:
        borrowed (int): Number of borrowed books

    """
    if borrowed <=3:  #books are 3 or less
        return "Within limit"
    elif borrowed >3 and borrowed <=6:  #books are between 4 and 6
        return "Over limit: Fine $5"
    elif borrowed > 6:  #books are more than 6
        return "Over limit: Fine $10"
    else: #the input shows error or invalid
        return "Error: Invalid number of books"
    


#Task 2
def process_borrowers(filename):
    """
    This function displays the status of the borrowers 
    >>>process_borrowers(filename)
    Parameters:
        filename (str) : Filename

    Ali: Within limit
    Sara: Over limit: Fine $5
    Error: Invalid number of books for John
    Error: Non-numeric value for Mary
    David: Over limit: Fine $10

    """
    
    with open(filename,"r") as f:
        reader=csv.reader(f) 
        next(reader) # omits the header for processing
        for i in reader: # iterating over lines in the file
            try:
                n=int(i[1]) # checkes for potential ValueError and acts as the parameter for check_limit function
                if n < 0:
                    print(f"Error: Invalid number of books for {i[0]}")
                    continue
                else:
                    status=check_limit(n)
                    print(f"{i[0]}: {status}") #displays the status
            except ValueError:
                print(f"Error: Non-numeric value for {i[0]}") # specifies the non-numeric value which caused the error

    





# Task 3 
def calculate_average_books(filename): 
    """
    This function calculates and displays the average number of books borrowed by students.
    >>> calculate_average_books(filename)
    Parameters:
        filename (str): The path to the CSV file containing student names and number of borrowed books

    Average number of books borrowed: 4.67
     
    """
    with open(filename, "r") as f:  
        csv_reader = csv.reader(f)    
        next(csv_reader)              # Skips the header row

        total_books = 0                 # Stores the total number of books borrowed
        valid_entries = 0               # Counts how many valid student entries are processed

        for line in csv_reader:         #Loops through each row in the CSV file
            if len(line) < 2:           # Skips rows with missing data
                continue

            books = line[1]            

            try:
                books = int(books)      # Converts the book count to an integer
                if books < 0:           # Skips negative numbers that include invalid data
                    continue            

                total_books = total_books + books 
                valid_entries = valid_entries + 1 
            except ValueError:                      # Handles string values in the second column 
              continue
            
        if valid_entries > 0:                       # Checks if there were any valid entries
            average = round(total_books / valid_entries, 2)   # Calculates the average number of books
            print(f"Average number of books borrowed: {average}") 
        else:
            print("No valid entries found.")         # Prints a message if no valid data exists


# Task 4 
def count_over_limit(filename):
    """
    Counts and prints how many students borrowed more than the allowed limit of books.
    >>> count_over_limit(filename)
    Parameters:
        filename (str): The path to the CSV file containing student names and number of borrowed books
      
    Number of students over the limit: 2
    """
    limit = 3                           # Sets the borrowing limit to 3 books
    over_limit_count = 0                # Counter for students who exceed the limit

    with open(filename, "r") as f:     
        csv_reader = csv.reader(f)       
        next(csv_reader)                   # Skips the header row

        for line in csv_reader:         # Loops through each row in the CSV file
            if len(line) < 2:            # Skips rows with missing columns
                continue

            books = line[1]              # Reads the number of borrowed books

            try:
                books = int(books)      # Converts the value to an integer
                if books < 0:           # skips negative values
                    continue
                if books > limit:       # Checks if the student borrowed more than the limit
                    over_limit_count = over_limit_count + 1
            except ValueError:                              # Skips rows where the book value isn't a number
                continue
              
    print(f"Number of students over the limit: {over_limit_count}")   
    
#Task 5
def main():
    """
    Checks if the file name is valid and calls all the functions of the book borrowing system
    >>>main()


    Enter the filename: new.csv
    File not found. Please try again.
    Enter the filename: borrowers.csv
    Ali: Within limit
    Sara: Over limit: Fine $5
    Error: Invalid number of books for John
    Error: Non-numeric value for Mary
    David: Over limit: Fine $10

    Average number of books borrowed: 4.67
    Number of students over the limit: 2

    """
    while True: # prompts the user to enter the filename until valid
        filename=input("Enter the filename: ") # Takes filename as the input from the user
        try:
            with open(filename, 'r') as file: # verifies the file exists
                break

        except FileNotFoundError: # raises an exception and displays the error message
            print("File not found. Please try again.")
        
        except Exception: # raises an exception on occurence of any other error
            print(f"An error occurred:Try again.")
    process_borrowers(filename)
    print()
    calculate_average_books(filename)
    count_over_limit(filename)
    

if __name__== "__main__":
    main()





