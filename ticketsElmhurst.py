import csv


tickets = {}

f = open("0216_parking.csv")
reader = csv.DictReader(f)

for row in reader: 
    plate = row["Plate ID"]
    tickets[plate] = tickets.get(plate,0) + 1
    #print("Ticket", tickets[plate], "for", plate)
    
f.close()

worst = sorted(tickets, key = tickets.__getitem__, reverse=True)

for i in range(11):
    print("Plate", worst[i], "has", tickets[worst[i]], "tickets.")
