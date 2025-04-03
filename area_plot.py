import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates

# Set the style
plt.style.use('dark_background')
# Use the specified muted palette
muted_palette = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3', '#fdb462']

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

# Create the plot
plt.figure(figsize=(15, 8))
ax = df.plot(kind='area', stacked=True, alpha=0.8, color=muted_palette)

# Customise the plot
plt.title('Daily Confirmed COVID-19 Cases by County\n26 Apr 2020 - 09 May 2020', 
          pad=20, fontsize=14, fontweight='bold', color='white')
plt.xlabel('Date', fontsize=12, labelpad=10, color='white')
plt.ylabel('Number of Cases', fontsize=12, labelpad=10, color='white')

# Customise legend
plt.legend(title='County', title_fontsize=12, fontsize=10, 
          bbox_to_anchor=(1.02, 1), loc='upper left', 
          facecolor='#1f1f1f', edgecolor='white')

# Customise grid
plt.grid(axis='y', linestyle='--', alpha=0.3, color='white')

# Format x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d\n%b'))  # Date and month on separate lines
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(color='white')
plt.yticks(color='white')

# Set background color
ax.set_facecolor('#1f1f1f')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['top'].set_color('white')
plt.gca().spines['left'].set_color('white')
plt.gca().spines['right'].set_color('white')

# Add thin horizontal lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.2, color='white')

# Adjust layout with more bottom space for dates
plt.tight_layout()

# Show the plot
plt.show()
