import pandas as pd
bd=pd.read_csv("/Users/davidskaff/Downloads/python-challenge/PyBank/Resources/budget_data.csv")
print(bd)

bd['Date'] = pd.to_datetime(bd['Date'], format='%b-%y')
bd = bd.sort_values('Date')

# The total number of months included in the dataset
total_months = bd['Date'].nunique()

# The net total amount of Profit/Losses over the entire period
total_profit_losses = bd['Profit/Losses'].sum()

# The changes in Profit/Losses over the entire period
bd['Profit/Losses_Change'] = bd['Profit/Losses'].diff()

# The average of those changes
average_change = bd['Profit/Losses_Change'].mean()

# The greatest increase in profits over the entire period
greatest_increase = bd.loc[bd['Profit/Losses_Change'].idxmax()]

# The greatest decrease in profits over the entire period
greatest_decrease = bd.loc[bd['Profit/Losses_Change'].idxmin()]

print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase["Date"].strftime("%b-%y")} (${greatest_increase["Profit/Losses_Change"]})')
print(f'Greatest Decrease in Profits: {greatest_decrease["Date"].strftime("%b-%y")} (${greatest_decrease["Profit/Losses_Change"]})')

results = [
    f'Total Months: {total_months}',
    f'Total: ${total_profit_losses}',
    f'Average Change: ${average_change}',
    f'Greatest Increase in Profits: {greatest_increase["Date"].strftime("%b-%y")} (${greatest_increase["Profit/Losses_Change"]})',
    f'Greatest Decrease in Profits: {greatest_decrease["Date"].strftime("%b-%y")} (${greatest_decrease["Profit/Losses_Change"]})'
]

with open('analysis_results.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')