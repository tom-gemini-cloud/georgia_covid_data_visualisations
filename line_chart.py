import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import numpy as np

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

# Find global min and max values
all_values = np.array([cobb, dekalb, fulton, gwinnett, hall])
min_value = np.min(all_values)
max_value = np.max(all_values)

# Find which county and date has max and min
max_county_idx = np.where(all_values == max_value)[0][0]
max_day_idx = np.where(all_values == max_value)[1][0]
min_county_idx = np.where(all_values == min_value)[0][0]
min_day_idx = np.where(all_values == min_value)[1][0]

max_county = counties = ['Cobb', 'DeKalb', 'Fulton', 'Gwinnett', 'Hall'][max_county_idx]
min_county = counties = ['Cobb', 'DeKalb', 'Fulton', 'Gwinnett', 'Hall'][min_county_idx]

# Create the plot
plt.figure(figsize=(15, 8))
ax = df.plot(kind='line', lw=3, marker='o', markersize=6, color=muted_palette)

# Customize the plot
plt.title('Daily Confirmed COVID-19 Cases by County\n26 Apr 2020 - 09 May 2020', 
          pad=20, fontsize=14, fontweight='bold', color='white')
plt.xlabel('Date', fontsize=12, labelpad=10, color='white')
plt.ylabel('Number of Cases', fontsize=12, labelpad=10, color='white')

# Customize legend
plt.legend(title='County', title_fontsize=12, fontsize=10, 
          bbox_to_anchor=(1.02, 1), loc='upper left',
          facecolor='#1f1f1f', edgecolor='white')

# Customize grid
plt.grid(True, linestyle='--', alpha=0.3, color='white')

# Format x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d\n%b'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.xticks(color='white')
plt.yticks(color='white')

# Set background color
ax.set_facecolor('#1f1f1f')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['top'].set_color('white') 
plt.gca().spines['left'].set_color('white')
plt.gca().spines['right'].set_color('white')

# Highlight max value with coral marker (from muted palette)
plt.plot(dates[max_day_idx], max_value, 'o', 
         markersize=12, markeredgewidth=2,
         markerfacecolor=muted_palette[2], markeredgecolor='white')

# Highlight min value with teal marker (from muted palette)
plt.plot(dates[min_day_idx], min_value, 'o', 
         markersize=12, markeredgewidth=2,
         markerfacecolor=muted_palette[0], markeredgecolor='white')

# Add annotations without values
plt.annotate('Highest', 
             xy=(dates[max_day_idx], max_value),
             xytext=(15, 10),
             textcoords='offset points',
             color=muted_palette[2],
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=muted_palette[2], alpha=0.7))

plt.annotate('Lowest', 
             xy=(dates[min_day_idx], min_value),
             xytext=(15, 10),
             textcoords='offset points',
             color=muted_palette[0],
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=muted_palette[0], alpha=0.7))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show() 