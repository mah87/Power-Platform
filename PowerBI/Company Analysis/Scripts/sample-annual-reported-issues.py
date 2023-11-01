import csv
from datetime import datetime, timedelta
import random

# Load the list of annual reports from the CSV
annual_reports = []
with open("annual_reports.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        annual_reports.append(row)

# List of issue names
issue_names = [
    "Financial Compliance",
    "Operational Efficiency",
    "Environmental Impact",
    "Safety Concerns",
    "Regulatory Compliance"
]

# Function to generate random issues for an annual report
def generate_issues_for_annual_report(annual_report_id):
    num_issues = random.randint(0, 5)  # Randomly generate 0 or 1 issue
    issues = []
    for _ in range(num_issues):
        issue_name = random.choice(issue_names)
        issues.append({
            "AnnualReportID": annual_report_id,
            "IssueName": issue_name
        })
    return issues

# Initialize a list to store the issues
issues = []

# Loop through each annual report and generate issues
for annual_report in annual_reports:
    annual_report_id = annual_report["AnnualReportID"]
    issues.extend(generate_issues_for_annual_report(annual_report_id))

# Write the list of issues to a CSV file
with open("annual_report_issues.csv", mode="w", newline="") as csv_file:
    fieldnames = ["AnnualReportID", "IssueName"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for issue in issues:
        writer.writerow(issue)

print("CSV file 'annual_report_issues.csv' has been created.")
