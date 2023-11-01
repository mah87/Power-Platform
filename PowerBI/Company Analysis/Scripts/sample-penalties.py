import random
import csv
from datetime import datetime, timedelta

# Load the list of companies from the CSV
companies = []
with open("companies.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        companies.append(row)

# List of penalty descriptions
penalty_descriptions = [
    "Regulatory fine for non-compliance",
    "Late payment penalty",
    "Environmental violation fine",
    "Safety violation penalty",
    "Contractual penalty"
]

# Function to generate random penalties for a given year and company
def generate_penalties_for_company(year, company_id):
    num_penalties = random.randint(0, 1)  # Randomly generate 0 or 1 penalty per year
    penalties = []
    for _ in range(num_penalties):
        penalty_date = datetime(year, random.randint(1, 12), random.randint(1, 28))  # Random date in the given year
        penalty_amount = round(random.uniform(1000, 10000), 2)  # Random penalty amount
        description = random.choice(penalty_descriptions)
        penalties.append({
            "Year": year,
            "CompanyID": company_id,
            "Description": description,
            "PenaltyDate": penalty_date.strftime("%Y-%m-%d"),
            "PenaltyAmount": penalty_amount
        })
    return penalties

# Initialize a list to store the penalties
penalties = []

# Date range from 1/1/2022 to 12/31/2026
start_date = datetime(2022, 1, 1)
end_date = datetime(2026, 12, 31)

# Loop through each account and generate penalties
for company in companies:
    company_id = company["ID"]
    for year in range(2022, 2027):
        if start_date <= datetime(year, 12, 31) <= end_date:
            penalties.extend(generate_penalties_for_company(year, company_id))

# Write the list of penalties to a CSV file
with open("penalties.csv", mode="w", newline="") as csv_file:
    fieldnames = ["Year", "CompanyID", "Description", "PenaltyDate", "PenaltyAmount"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for penalty in penalties:
        writer.writerow(penalty)

print("CSV file 'penalties.csv' has been created.")
