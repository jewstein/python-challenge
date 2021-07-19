import csv
import statistics

with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimeter = ",")
    header = next(csvreader)

    tot_votes = []

    candidates = {}
    candidates = dict()
    candidates_list = [
    "Tom Cruise",
    "Angelina Jolie",
    "Kristen Stewart",
    "Denzel Washington"]
    print(candidates_list)