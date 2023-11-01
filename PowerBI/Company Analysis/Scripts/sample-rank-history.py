import csv
import random
from datetime import datetime, timedelta

# Load the list of companies from the CSV
companies = []
with open("companies.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        companies.append(row)

# List of possible ranks
ranks = ["High", "Medium", "Low"]

# Function to generate ranking history for a company
def generate_ranking_history_for_company(company_id):
    ranking_history = []
    current_rank = random.choice(ranks)
    current_year = 2022
    for year in range(2022, 2027):  # Generate ranking history for 2022 to 2026
        old_rank = current_rank
        rank_changes = random.randint(0, 3)  # Randomly generate 0 to 3 rank changes in a year
        for _ in range(rank_changes):
            new_rank = random.choice([rank for rank in ranks if rank != old_rank])
            # Determine whether the rank increased or decreased
            if ranks.index(new_rank) > ranks.index(old_rank):
                rank_change = "Increased"
            else:
                rank_change = "Decreased"
            
            # Generate a random date within the year when the rank changed
            rank_change_date = datetime(year, random.randint(1, 12), random.randint(1, 28))
            
            ranking_history.append({
                "CompanyID": company_id,
                "Year": year,
                "OldRank": old_rank,
                "NewRank": new_rank,
                "RankChange": rank_change,
                "RankChangeDate": rank_change_date.strftime("%Y-%m-%d")
            })
            old_rank = new_rank
        current_rank = old_rank
        current_year = year
    return ranking_history

# Initialize a list to store the ranking history
ranking_history = []

# Loop through each company and generate ranking history
for company in companies:
    company_id = company["ID"]
    ranking_history.extend(generate_ranking_history_for_company(company_id))

# Write the list of ranking history to a CSV file
with open("company_ranking_history.csv", mode="w", newline="") as csv_file:
    fieldnames = ["CompanyID", "Year", "OldRank", "NewRank", "RankChange", "RankChangeDate"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for ranking in ranking_history:
        writer.writerow(ranking)

print("CSV file 'company_ranking_history.csv' has been created.")
