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


# Task 2
# def process_borrowers (file_path):
#  with open(file_path,"r") as f:
#     for line in f:
#         line=line.strip()
#         Name,book =line.split(",")
#         try:
#             book=int(book)
#             status=check_limit(book)
#             print(Name,"-",status)
#         except ValueError:
#             print("Error: Non-numeric value for", Name)

# def check_limit(borrowed):
#     limit = 3
#     fine_per_book = 5
#     if borrowed <= limit:
#         return "Within limit"
#     else:
#         fine = (borrowed - limit) * fine_per_book
#         return f"Over limit: Fine ${fine}"
# def process_borrowers(file_path):
#     with open(file_path, "r") as f:
#         csv_reader = csv.reader(f)
#         next(csv_reader)  

#         for line in csv_reader:
           
#             if len(line) < 2:
#                 print(f"Error: Missing data for {line[0] if line else 'Unknown'}")
#                 continue

#             name = line[0]
#             books = line[1]

#             try:
#                 books = int(books)
#                 if books < 0:
#                     print(f"Error: Invalid number of books for {name}")
#                     continue
            
#                 status = check_limit(books)
#                 print(f"{name}: {status}")
#             except ValueError:
#                 print(f"Error: Non-numeric value for {name}")
#mohammed


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








print(check_limit(book))
#check_limit(file_path)
calculate_average_books(file_path)
count_over_limit(file_path)




