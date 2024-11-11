import pandas as pd
import re


df = pd.read_csv("./part_wine_reviews.csv")
df_5 = df.head(5)
#index = [False, True, False, True, False]
#d#print(df_filtered)

keyword = "aromas"
ser_descriptions = df_5["description"]
index = []
for description in ser_descriptions:
    if re.search(keyword, description):
        index.append(True)
    else:
        index.append(False)
print(ser_descriptions)

