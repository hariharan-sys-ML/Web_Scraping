import matplotlib.pyplot as plt
import Data_analysis as da

plt.bar(da.Rate.index,da.Rate.values)
plt.xticks(da.Rate.index)
plt.xlabel("Rating")
plt.ylabel("No.of Books")
plt.title("Rating vs No.of Books")
plt.show()

plt.hist(da.df["Price"], bins=100)
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.title("Distribution of Book Prices")
plt.show()

avg_price = da.df.groupby("Rating")["Price"].mean()
plt.plot(avg_price.index, avg_price.values)
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.title("Average Book Price by Rating")
plt.show()