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
book=int(input("Enter the number of borrowed books:")) #asking user how many books are entered
def check_limit(borrowed):
    """
    Check the borrowing limit and returns the status message
    >>>check_limit(borrowed)
    Parameters:
        borrowed (int): Number of borrowed books

    Enter the number of borrowed books:3

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

    Enter the number of borrowed books:3
    Ali: Within limit
    Sara: Over limit: Fine $5
    John: Within limit
    Error: Non-numeric value for Mary
    David: Over limit: Fine $10

    """
    try:
        with open(filename,"r") as f:
            reader=csv.reader(f) 
            next(reader) # omits the header for processing
            for i in reader: # iterating over lines in the file
                try:
                    n=int(i[1]) # checkes for potential ValueError and the parameter for check_limit function
                    status=check_limit(n)
                    print(f"{i[0]}: {status}") #displays the status
                except ValueError:
                    print(f"Error: Non-numeric value for {i[0]}") # specifies the non-numeric value which caused the error

    except FileNotFoundError:
        print("File not found")





# Task 3 
def calculate_average_books(file_path):
    """
    """
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)

        total_books = 0      
        valid_entries = 0   

        for line in csv_reader:
            
            if len(line) < 2:
                continue

            
            books = line[1]

            try:
                books = int(books)
                if books < 0:
                    continue
                total_books = total_books + books
                valid_entries = valid_entries + 1
            except ValueError:
              continue
        if valid_entries > 0:
            average = total_books / valid_entries
            print(f"Average number of books borrowed: {average:.2f}")
        else:
            print("No valid entries found.")


# Task 4 
def count_over_limit(file_path):
    """
    """
    limit = 3 
    over_limit_count = 0

    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)

        for line in csv_reader:
            if len(line) < 2: 
                continue

            
            books = line[1]

            try:
                books = int(books)
                if books < 0:
                    continue
                if books > limit:
                    over_limit_count = over_limit_count + 1
            except ValueError:
                continue
              
    print(f"Number of students over the limit: {over_limit_count}")

#Task 5
def main():
    """
    Checks if the file name is valid and calls the all the functions of the book borrowing system
    >>>main()

    Enter the number of borrowed books:3
    Enter the filename: new.csv
    File not found. Please try again.
    Enter the filename: borrowers.csv
    Ali: Within limit
    Sara: Over limit: Fine $5
    John: Within limit
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





