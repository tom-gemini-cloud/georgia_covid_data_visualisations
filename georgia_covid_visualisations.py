import matplotlib.pyplot as plt
import pandas as pd

# Data
dates = pd.date_range(start='2020-04-26', periods=14)
cobb = [35, 55, 75, 40, 50, 65, 30, 15, 35, 30, 40, 20, 5, 2]
dekalb = [45, 60, 90, 55, 60, 40, 40, 30, 45, 40, 50, 35, 15, 5]
fulton = [55, 85, 110, 70, 85, 50, 60, 40, 60, 50, 70, 95, 20, 5]
gwinnett = [50, 65, 105, 85, 70, 45, 55, 35, 50, 45, 65, 40, 15, 3]
hall = [60, 75, 170, 95, 90, 55, 70, 45, 65, 60, 80, 50, 25, 8]

# Create DataFrame
data = {
    'Date': dates,
    'Cobb': cobb,
    'DeKalb': dekalb,
    'Fulton': fulton,
    'Gwinnett': gwinnett,
    'Hall': hall
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Plot
ax = df.plot(kind='bar', stacked=False, figsize=(15, 8), colormap='tab20')
plt.title('Daily Confirmed COVID-19 Cases by County (26 Apr 2020 - 09 May 2020)')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend(title='County')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot 
plt.show()