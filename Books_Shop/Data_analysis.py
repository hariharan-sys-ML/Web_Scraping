import pandas as pd

df = pd.read_csv("books.csv")

df = pd.read_csv("books.csv", encoding="utf-8")

df["Price"] = (df["Price"].str.replace("Â£", "").str.replace("£", "").astype(float))

print("Cheapest = " , df["Price"].min())
print("Mean Price = " ,round(df["Price"].mean(),2))
print("Maximum Price = ",df["Price"].max())

Rate = df["Rating"].value_counts()
print("\nMost common Rating  = " ,Rate.idxmax())

for i in Rate.index:
    if i == "Five":
        percent = Rate[i]/10
        print("The Percentage of Books with Five-Star Rating = " ,percent, "%")
    else:
        continue
new_df = df[(df["Rating"]=="Five") & (df["Price"] < 30)]
