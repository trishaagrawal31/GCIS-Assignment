"""
Group Members:
1. Leen  - 746007751
2. Trisha  - 753005593
3. Mohammed - 410001753

Manifesto:
- Mohammed: Implemnted Task 1 check_limit()
- Leen: Implemented Task 3 calculate_average_books() and Task 4 count_over_limit().
- Trisha: Implemented Task 2 process_borrowed().

"""
import csv
file_path = "borrowers.csv"

# Task 1 
book=int(input("enter the number of borrowed books:")) #asking user how many books are entered
def check_limit(borrowed):
    if borrowed <=3:  #books are 3 or less
        return "within limit"
    elif borrowed >3 and borrowed <=6:  #books are between 4 and 6
        return "Over limit: Fine $5"
    elif borrowed > 6:  #books are more than 6
        return "Over limit: Fine $10"
    else: #the input shows error or invalid
        return "Error: Invalid number of books"
print(check_limit(book)) #calling the function given


def process_borrowers(filename):
    """
    This function displays the status of the borrowers 
    >>>process_borrowers(filename)


    """
    try:
        with open(filename,"r") as f:
            reader=csv.reader(f)
            head=next(reader)
            for i in reader:
                try:
                    int(i[1])
                    status=check_limit(int(i[1]))
                    print(f"{i[0]} : {status}")
                except ValueError:
                    print(f"Error: Non-numeric value for {i[0]}")

    except FileNotFoundError:
        print("file not found")




# Task 3 
def calculate_average_books(file_path):
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)

        total_books = 0      
        valid_entries = 0   

        for line in csv_reader:
            
            if len(line) < 2:
                continue

            #name = line[0] #not lighting up check why?
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
    limit = 3 
    over_limit_count = 0

    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)

        for line in csv_reader:
            if len(line) < 2: 
                continue

            #name = line[0] not lighting up check why?
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
    while True:
        filename=input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                
                break
        except FileNotFoundError:
            print("File not found. Please try again.")
        
        except Exception:
            print(f"An error occurred:Try again.")
    process_borrowers(filename)
    count_over_limit(filename)
    calculate_average_books(filename)
    






if __name__== "__main__":
    main()
# print(check_limit(book))
# #check_limit(file_path)
# calculate_average_books(file_path)
# count_over_limit(file_path)




