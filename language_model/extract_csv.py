fr = open("clozeAbstracts.csv", "r")
csv_reader = csv.reader(fr, delimiter=',')
for row in csv_reader:
      #row[0] is the abstract
      #row[1] would be topic
