import csv
from datetime import datetime, timedelta
import random

# Load the list of companies from the CSV
companies = []
with open("./PowerBI/Company Analysis/Data/companies.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        companies.append(row)

# Function to generate random integer weights between 0 and 5
def generate_random_weights():
    return [random.randint(0, 5) for _ in range(5)]

# Function to generate annual reports for a company within a specific year
def generate_annual_reports_for_company(year, company_id):
    annual_reports = []
    month = random.randint(2,5)  
    reporting_year = year-1  
    if month == 2:
        submission_date = datetime(year, month, random.randint(1, 28))  # Random day in February
    elif month == 4:
        submission_date = datetime(year, month, random.randint(1, 30))  # Random day in April
    else:
        submission_date = datetime(year, month, random.randint(1, 31))  # Random day in March
    annual_report_id = f"AR-{reporting_year}-{company_id}"
    annual_reports.append({
        "CompanyID": company_id,
        "AnnualReportID": annual_report_id,
        "ReportingYear": reporting_year,
        "Criteria_1": generate_random_weights()[0],
        "Criteria_2": generate_random_weights()[0],
        "Criteria_3": generate_random_weights()[0],
        "Criteria_4": generate_random_weights()[0],
        "Criteria_5": generate_random_weights()[0],
        "SubmissionDate": submission_date.strftime("%Y-%m-%d")
    })
    return annual_reports

# Initialize a list to store the annual reports
annual_reports = []

# Date range from 2022 to 2027
start_year = 2022
end_year = 2027

# Loop through each company and generate annual reports
for company in companies:
    company_id = company["ID"]
    for year in range(start_year, end_year + 1):
        annual_reports.extend(generate_annual_reports_for_company(year, company_id))

# Write the list of annual reports to a CSV file
with open("./PowerBI/Company Analysis/Data/annual_reports.csv", mode="w", newline="") as csv_file:
    fieldnames = ["CompanyID", "AnnualReportID", "ReportingYear", "Criteria_1", "Criteria_2", "Criteria_3", "Criteria_4", "Criteria_5", "SubmissionDate"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for annual_report in annual_reports:
        writer.writerow(annual_report)

print("CSV file 'annual_reports.csv' has been created.")
