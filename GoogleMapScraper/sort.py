# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("leads_sorted.csv")

# length before adding row
length1 = len(data)


# sorting by first name
data.sort_values("Institute Name", inplace=True)

# dropping duplicate values
data.drop_duplicates(keep=False, inplace=True)

# length after removing duplicates
length3 = len(data)

# printing all data frame lengths
print(length1,  length3)
data.to_csv('leads_final.csv', index=False, encoding='utf-8')
