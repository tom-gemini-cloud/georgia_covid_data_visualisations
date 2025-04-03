import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import matplotlib as mpl

# Set the style to dark and configure figure size
sns.set_theme(style="dark")
plt.rcParams['figure.figsize'] = (15, 8)
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['axes.facecolor'] = 'black'

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

# Create figure with black background
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
ax = df.plot(kind='bar', stacked=True, width=0.8, color=muted_palette, ax=ax)

# Customize the plot
plt.title('Daily Confirmed COVID-19 Cases by County\n26 Apr 2020 - 09 May 2020', 
          pad=20, fontsize=14, fontweight='bold', color='white')
plt.xlabel('Date', fontsize=12, labelpad=10, color='white')
plt.ylabel('Number of Cases', fontsize=12, labelpad=10, color='white')

# Customize legend with properly specified title and text colors
legend = plt.legend(title='County', fontsize=10, 
          bbox_to_anchor=(1.02, 1), loc='upper left',
          facecolor='black', edgecolor='white')
legend.get_title().set_color('white')
legend.get_title().set_fontsize(12)
for text in legend.get_texts():
    text.set_color('white')

# Customize grid
plt.grid(axis='y', linestyle='--', alpha=0.3, color='white')

# Format x-axis
ax.set_xticklabels([d.strftime('%d\n%b') for d in dates])
plt.xticks(color='white', rotation=0)
plt.yticks(color='white')

# Set spines color
for spine in ax.spines.values():
    spine.set_color('white')

# Add thin horizontal lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.2, color='white')

# Adjust layout with more bottom space for dates
plt.tight_layout()

# Show the plot
plt.show()