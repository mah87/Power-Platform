import random
import csv

# List of company names
company_names = ["ABC Industries", "XYZ Tech Solutions", "Green Energy Corp", "Innovative Innovations", "Blue Sky Ventures", "QuickServe Delivery", "Solaris Systems", "EcoGreen Solutions", "Red Rocket Media", "Apex Analytics"]

# Shuffle the list of company names to make sure they are unique
random.shuffle(company_names)

# Initialize an empty list to store the generated companies
companies = []

# Number of companies you want to generate
num_companies = 100

# Probability of a company being registered (e.g., 70%)
registered_probability = 0.7

for i in range(1, num_companies + 1):
    company_name = company_names[i % len(company_names)]  # Use names in a circular manner
    company_id = f"COMP{str(i).zfill(3)}"  # Generating a company ID
    is_registered = random.random() < registered_probability  # Bias towards registered status

    status = "Registered" if is_registered else "Unregistered"

    companies.append({"ID": company_id, "Name": company_name, "Status": status})

# Write the list of companies to a CSV file
with open("companies.csv", mode="w", newline="") as csv_file:
    fieldnames = ["ID", "Name", "Status"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for company in companies:
        writer.writerow(company)

print("CSV file 'companies.csv' has been created.")

