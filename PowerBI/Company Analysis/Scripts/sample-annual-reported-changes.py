import csv
from datetime import datetime, timedelta
import random

# List of issue names
change_descriptions = [
    "Address Change",
    "New Affiliation",
    "Tombstone Info Update",
    "New Capabilities"
]
# Load the list of annual reports from the CSV
annual_reports = []
with open("annual_reports.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        annual_reports.append(row)

# Function to generate random reported changes for an annual report
def generate_reported_changes_for_annual_report(annual_report_id):
    num_changes = random.randint(0, 1)  # Randomly generate 0 or 1 reported change
    changes = []
    for _ in range(num_changes):
        change_description = random.choice(change_descriptions)
        changes.append({
            "AnnualReportID": annual_report_id,
            "ChangeDescription": change_description
        })
    return changes

# Initialize a list to store the reported changes
reported_changes = []

# Loop through each annual report and generate reported changes
for annual_report in annual_reports:
    annual_report_id = annual_report["AnnualReportID"]
    reported_changes.extend(generate_reported_changes_for_annual_report(annual_report_id))

# Write the list of reported changes to a CSV file
with open("annual_report_reported_changes.csv", mode="w", newline="") as csv_file:
    fieldnames = ["AnnualReportID", "ChangeDescription"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for change in reported_changes:
        writer.writerow(change)

print("CSV file 'annual_report_reported_changes.csv' has been created.")
