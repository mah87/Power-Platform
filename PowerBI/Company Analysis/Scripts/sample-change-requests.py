import random
import csv
from datetime import datetime, timedelta

# Load the list of companies from the CSV
companies = []
with open("companies.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        companies.append(row)

# Function to generate random change requests for a given year and company
def generate_change_requests_for_company(year, company_id):
    num_requests = random.randint(0, 2)  # Randomly generate 0 to 2 change requests per year
    change_requests = []
    for _ in range(num_requests):
        submission_date = datetime(year, random.randint(1, 12), random.randint(1, 28))  # Random date in the given year
        name = random.choice(change_request_names)
        change_requests.append({
            "Year": year,
            "CompanyID": company_id,
            "Name": name,
            "SubmissionDate": submission_date.strftime("%Y-%m-%d")
        })
    return change_requests

# Initialize a list to store the change requests
change_requests = []

# List of change request names
change_request_names = ["Upgrade Software", "Implement New Process", "Infrastructure Maintenance", "Security Enhancement", "Database Optimization"]




# Date range from 1/1/2022 to 12/31/2025
start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 12, 31)

# Loop through each account and generate change requests
for company in companies:
    company_id = company["ID"]
    for year in range(2022, 2026):
        if start_date <= datetime(year, 12, 31) <= end_date:
            change_requests.extend(generate_change_requests_for_company(year, company_id))

# Write the list of change requests to a CSV file
with open("change_requests.csv", mode="w", newline="") as csv_file:
    fieldnames = ["Year", "CompanyID", "Name", "SubmissionDate"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for request in change_requests:
        writer.writerow(request)

print("CSV file 'change_requests.csv' has been created.")
