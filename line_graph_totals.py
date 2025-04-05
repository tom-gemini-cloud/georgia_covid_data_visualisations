import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.dates as mdates

# Set the style
plt.style.use('dark_background')

# Set background color for the entire figure
plt.rcParams['figure.facecolor'] = '#0F3051'
plt.rcParams['axes.facecolor'] = '#0F3051'

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

# Calculate total cases for each day
df['Total'] = df.sum(axis=1)

# Create a single figure and axis
fig, ax = plt.subplots(figsize=(15, 8))

# Create the gradient colormap from white to red
colors = ['white', '#FF9999', '#FF6666', '#FF3333', '#FF0000', '#CC0000']
cmap = mcolors.LinearSegmentedColormap.from_list('WhiteToRed', colors)

# Plot line for total cases
line, = ax.plot(df.index, df['Total'], color='white', linewidth=3)

# Create a gradient fill using fill_between with multiple segments
# Convert dates to numeric values for matplotlib
date_nums = mdates.date2num(df.index)

# Create a gradient fill by using multiple fill_between calls with different alphas
num_segments = 10
for i in range(num_segments):
    # Calculate the alpha for this segment (increasing from top to bottom)
    alpha = 0.1 + (i / num_segments) * 0.6
    
    # Calculate the y-value for this segment
    y_value = (i / num_segments) * df['Total'].max()
    
    # Fill the area up to this y-value
    ax.fill_between(df.index, y_value, df['Total'], 
                   color='red', alpha=alpha, zorder=1)

# Add a text label directly within the shaded area
midpoint_idx = len(df.index) // 2
midpoint_date = df.index[midpoint_idx]
midpoint_y = df['Total'].iloc[midpoint_idx] * 0.4  # Position at 40% of the height
ax.text(midpoint_date, midpoint_y, 'Total Covid-19 Cases in the Top 5 Most Infected Counties', 
        color='white', fontsize=14, fontweight='bold', alpha=0.8,
        ha='center', va='center')

# Customize the plot
plt.title('Total Daily Confirmed COVID-19 Cases in the Top 5 Most Infected Counties in Georgia', 
          pad=40, fontsize=14, fontweight='bold', color='white')
plt.xlabel('Date', fontsize=12, labelpad=10, color='white')
plt.ylabel('Total Number of Cases', fontsize=12, labelpad=10, color='white')

# Adjust the y-axis limit
ax.set_ylim(0, df['Total'].max() * 1.2)  # Add 20% padding for annotations

# Format x-axis dates
plt.xticks(dates, [d.strftime('Apr %d') if d.month == 4 else d.strftime('May %d') for d in dates], 
           rotation=45, ha='right', color='white')
plt.yticks(color='white')

# Remove top and right spines, style bottom and left
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')
plt.gca().spines['bottom'].set_alpha(0.3)
plt.gca().spines['left'].set_alpha(0.3)

# Add grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.2, color='white')

# Add legend
ax.legend(loc='upper right', facecolor='#0F3051', edgecolor='none')

# Create a custom colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, df['Total'].max()))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.01, orientation='vertical')
cbar.ax.set_ylabel('Case Count', color='white')
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax, 'yticklabels'), color='white')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()