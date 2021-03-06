'''
Scenario: You are a data scientist working for a consulting firm. One of your colleagues from the Auditing department
has asked you to help them assess the financial statement of organization X.
You've been supplied with the two lists of data: monthly revenue and monthly expenses for financial year in question.
calculate the following metrics:

1. Profit for each month
2. Profit after tax for each month (tax rate is 30%)
3. Profit after margin for each month- equals to profit after tax divided by revenue.
4. Good months: profit after tax was greater than mean for the year
5. Bad months: profit after tax was less than mean for the year
6. The best months: profit after tax was max for the year
7. The worst months: profit after tax was min for the year

All results need to be presented as lists.
Results for $ need to be calculated with $0.01 precision but need to be presented in units of $1000(i.e. 1k)
with no decimal points.

Your colleague has warned you that it is okay for tax for any given month to be negative.

Data:
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
'''
import numpy as np
from numpy import array

rev = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97,
       15433.50]
exp = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37,
       3803.96]
revenue = np.array(rev)
expenses = np.array(exp)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
good_months = []
bad_months = []
best_months = []
worst_months = []
monthly_profit = []
monthly_profit_after_tax = []
profit_after_margin = []
for i in range(0, len(revenue)):
    monthly_profit.append(round((revenue[i] - expenses[i]), 2))
    monthly_profit_after_tax.append(round((revenue[i] - (expenses[i] + (0.3 * expenses[i]))), 2))

total_monthly_profit_after_tax = sum(monthly_profit_after_tax)
mean_profit = round((total_monthly_profit_after_tax / 12), 2)
max_profit = round((max(monthly_profit_after_tax)), 2)
min_profit = round((min(monthly_profit_after_tax)), 2)
for i in range(0, len(monthly_profit_after_tax)):
    profit_after_margin.append(months[i] + ": " + str(round((monthly_profit_after_tax[i] / revenue[i]), 2)))

for i in range(0, len(monthly_profit_after_tax)):
    if monthly_profit_after_tax[i] > mean_profit:
        good_months.append(months[i] + " ")
    else:
        bad_months.append(months[i] + " ")

for i in range(0, len(monthly_profit_after_tax)):
    if monthly_profit_after_tax[i] == max_profit:
        best_months.append(months[i] + " ")
    elif monthly_profit_after_tax[i] == min_profit:
        worst_months.append(months[i] + " ")

print(f"""Monthly Profit: {monthly_profit}
Monthly profit after tax: {monthly_profit_after_tax}
Mean profit after tax: {mean_profit}
Maximum Profit: {max_profit}
Minimum profit: {min_profit}
Good months: {good_months}
Bad months: {bad_months}
Best month(s): {best_months}
Worst month(s): {worst_months}
Profit after margin: {profit_after_margin}
""")
print("After converting calculations to units of $1000: ")
revenue_1000 = [round(i / 1000, 2) for i in revenue]
revenue_1000_fmtd = [("$" + str(revenue_1000[i]) + "K") for i in range(0, len(revenue_1000))]
expenses_1000 = [round(i / 1000, 2) for i in expenses]
expenses_1000_fmtd = [("$" + str(expenses_1000[i]) + "K") for i in range(0, len(expenses_1000))]
profit_1000 = [round(i / 1000, 2) for i in monthly_profit]
profit_1000_fmtd = [(months[i] + ": $" + str(profit_1000[i]) + "K") for i in range(0, len(profit_1000))]
profit_after_tax_1000 = [round(i / 1000, 2) for i in monthly_profit_after_tax]
profit_after_tax_1000_fmtd = [(months[i] + ": $" + str(profit_after_tax_1000[i]) + "K") for i in
                              range(0, len(profit_after_tax_1000))]
profit_after_margin_1000 = [round(i / 1000, 2) for i in range(0, len(profit_after_margin))]
profit_after_margin_1000_fmtd = [(months[i] + ": $" + str(profit_after_margin_1000[i]) + "K") for i in
                                 range(0, len(profit_after_margin_1000))]
mean_profit_1000 = "$" + str(round((mean_profit / 1000), 2)) + "K"
max_profit_1000 = "$" + str(round((max_profit / 1000), 2)) + "K"
min_profit_1000 = "$" + str(round((min_profit / 1000), 2)) + "K"

print(f"""Monthly expenses: {expenses_1000_fmtd}
Monthly revenue: {revenue_1000_fmtd}
Monthly profit: {profit_1000_fmtd}
Monthly profit after tax: {profit_after_tax_1000_fmtd}
Monthly profit after margin: {profit_after_margin_1000_fmtd}
Mean profit after tax: {mean_profit_1000}
Maximum Profit: {max_profit_1000}
Minimum profit: {min_profit_1000}
""")
