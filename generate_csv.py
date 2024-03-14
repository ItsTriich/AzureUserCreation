import csv
import random
import string

# Function to generate random string
def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Function to generate random email-like string
def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    return generate_random_string(random.randint(5, 10)) + "@" + random.choice(domains)

# Function to generate somewhat realistic names
def generate_realistic_name():
    prefixes = ['Mr.', 'Ms.', 'Dr.', 'Prof.']
    first_names = ['John', 'Alice', 'Michael', 'Emily', 'David', 'Emma', 'Sarah', 'James']
    last_names = ['Smith', 'Johnson', 'Brown', 'Lee', 'Wilson', 'Taylor', 'Anderson']
    prefix = random.choice(prefixes)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{prefix} {first_name} {last_name}"

# Generate CSV file with random realistic-like data
csv_file = "realistic_users.csv"
num_users = 10  # Change this to the desired number of users

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['DisplayName', 'UserPrincipalName', 'GivenName', 'Surname', 'Password'])
    for _ in range(num_users):
        display_name = generate_realistic_name()
        user_principal_name = generate_random_email()
        given_name = display_name.split()[1]  # Use the first name from the display name
        surname = display_name.split()[-1]    # Use the last name from the display name
        password = generate_random_string(8) + "123@"  # Adding some special characters to the password
        writer.writerow([display_name, user_principal_name, given_name, surname, password])

print(f"CSV file '{csv_file}' created successfully with {num_users} realistic-like users.")

