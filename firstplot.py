#firstplot.py
#First practice plots pulling from data from another source, not a list

import numpy as np
import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
x_indexes = np.arange(len(months))
width = 0.25

money_per_month_2021 = [500, 550, 550, 550, 550, 550, 750, 750, 750, 750, 900, 1000]
plt.bar(x_indexes - width, money_per_month_2021, width=width, color='k', label='2021')


money_per_month_2022 = [900, 950, 950, 950, 950, 1910, 2870, 4150, 5000, 5000, 6500, 6900]
plt.bar(x_indexes, money_per_month_2022, width=width, color='b', label='2022')

hopeful_money_per_month_2023 = [7000, 7000, 7000, 7000, 8500, 10500, 13000, 15500, 15500, 15500, 15500, 15750]
plt.bar(x_indexes + width, hopeful_money_per_month_2023, width=width, color='r', label='2023')

plt.xlabel("Months of the Year")
plt.ylabel("Money made per month")
plt.title("Money Tracker")

plt.legend()
plt.xticks(ticks=x_indexes, labels=months)
plt.grid(True)
plt.tight_layout()
plt.show()