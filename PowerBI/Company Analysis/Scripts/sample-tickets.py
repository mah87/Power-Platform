import csv
import random
from datetime import date, timedelta

# Define the date range
start_date = date(2022, 1, 1)
end_date = date(2025, 12, 31)

# Load the list of companies from the CSV
companies = []
with open("companies.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        companies.append(row)

# Define the average number of tickets per year
average_tickets_per_year = 3.5

# Create a list to store the generated tickets
tickets = []

# Generate tickets for each year in the date range
current_date = start_date
while current_date <= end_date:
    for company in companies:
        # Generate a random number of tickets for this year
        num_tickets = round(random.uniform(0.5 * average_tickets_per_year, 1.5 * average_tickets_per_year))
        
        # Create tickets for this company in this year
        for _ in range(num_tickets):
            ticket_date = current_date + timedelta(days=random.randint(0, 365))
            ticket = {
                'Company ID': company['ID'],
                'Company Name': company['Name'],
                'Ticket ID': len(tickets) + 1,
                'Ticket Date': ticket_date.strftime("%Y-%m-%d"),
                'Ticket Description': f"Ticket for {company['Name']} on {ticket_date}",
            }
            tickets.append(ticket)
    
    # Move to the next year
    current_date = date(current_date.year + 1, 1, 1)

# Write the generated tickets to a CSV file
with open('sample_tickets.csv', 'w', newline='') as csvfile:
    fieldnames = ['Company ID', 'Company Name', 'Ticket ID', 'Ticket Date', 'Ticket Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(tickets)

print(f'{len(tickets)} tickets have been generated and saved to sample_tickets.csv')
