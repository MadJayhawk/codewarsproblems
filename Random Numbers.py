import random



# File path
file_path = r'F:\Codewars Problems\Affordable Vacation Random Numbers.txt'
def write_random_numbers(file_path, num_count, min_val, max_val):
    with open(file_path, 'w') as file:
        for _ in range(num_count):
            random_number = random.randint(min_val, max_val)
            file.write(f"{random_number}\n")
        file.close()    
    print(f"{num_count} random numbers have been written to {file_path}")

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        file.close()
    return numbers
# Number of random numbers to generate
num_count = 15_000_000
min_val = 1
max_val = 400

# Write random numbers to the file
write_random_numbers(file_path, num_count, min_val, max_val)

# Read numbers from the file into a list
numbers_list = read_numbers_from_file(file_path)

# Print the first 10 numbers to verify
print("First 10 numbers from the list:")
print(numbers_list[:20])

# Print the total count of numbers retrieved
print(f"Total numbers retrieved: {len(numbers_list)}")