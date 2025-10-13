import csv
# borrowedbooks = int(input("Please enter number of books borrowed: ")) #asks for users input.
# def check_limit(borrowed):
#     if borrowed < 0:
#         return "Error: Invalid number of books"
#     elif borrowed <= 3:
#         return "within limit"
#     elif borrowed > 3 and borrowed <= 6:
#         return "Over limit: Fine $5"
#     else:
#         return "Over limit: Fine $10"

file_path = "borrowers.csv"

def calculate_average_and_overlimit(file_path):
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)

        total_books = 0
        valid_entries = 0
        over_limit_count = 0

        for line in csv_reader:
            # Skip incomplete or empty lines
            if len(line) < 2:
                continue

            name = line[0]
            books = line[1]

            try:
                books = int(books)

                # Check for invalid (negative) numbers
                if books < 0:
                    print(f"Error: Invalid number of books for {name}")
                    continue

                # Check if over the limit
                if books > 3:
                    fine = (books - 3) * 5
                    print(f"{name}: Over limit: Fine ${fine}")
                    over_limit_count += 1
                else:
                    print(f"{name}: Within limit")

                # Add to totals for average
                total_books += books
                valid_entries += 1

            except ValueError:
                # Handle non-numeric input
                print(f"Error: Non-numeric value for {name}")

        # Calculate average
        if valid_entries > 0:
            average = total_books / valid_entries
            print(f"Average number of books borrowed: {average:.2f}")
        else:
            print("No valid entries found.")

        print(f"Number of students over the limit: {over_limit_count}")

calculate_average_and_overlimit(file_path)
