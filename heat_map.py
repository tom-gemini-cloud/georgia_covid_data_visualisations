import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.colors as mcolors

# Set the style
plt.style.use('dark_background')

# Use the specified muted palette
muted_palette = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3', '#fdb462']

# Data
dates = pd.date_range(start='2020-04-26', periods=14)
date_labels = [date.strftime('%d %b') for date in dates]
counties = ['Cobb', 'DeKalb', 'Fulton', 'Gwinnett', 'Hall']

cobb = [35, 55, 75, 40, 50, 65, 30, 15, 35, 30, 40, 20, 5, 2]
dekalb = [45, 60, 90, 55, 60, 40, 40, 30, 45, 40, 50, 35, 15, 5]
fulton = [55, 85, 110, 70, 85, 50, 60, 40, 60, 50, 70, 95, 20, 5]
gwinnett = [50, 65, 105, 85, 70, 45, 55, 35, 50, 45, 65, 40, 15, 3]
hall = [60, 75, 170, 95, 90, 55, 70, 45, 65, 60, 80, 50, 25, 8]

# Create data matrix for heatmap
data_matrix = np.array([cobb, dekalb, fulton, gwinnett, hall])

# Create the plot
plt.figure(figsize=(15, 8))

# Create a custom colormap from the muted palette
# Use the teal (#8dd3c7) for low values and coral (#fb8072) for high values
colors = [muted_palette[0], '#ffffff', muted_palette[2]]
custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_muted_cmap', colors)

# Find min and max values for annotation styling
min_value = np.min(data_matrix)
max_value = np.max(data_matrix)

# Create heatmap
ax = sns.heatmap(data_matrix, 
                annot=False,  # No annotations
                cmap=custom_cmap,
                cbar_kws={"shrink": 0.75, "label": "Number of Cases"},
                linewidths=0.3,
                linecolor='#333333',
                xticklabels=date_labels,
                yticklabels=counties)

# Customize the plot
plt.title('Daily Confirmed COVID-19 Cases by County\n26 Apr 2020 - 09 May 2020', 
          pad=20, fontsize=14, fontweight='bold', color='white')
plt.xlabel('Date', fontsize=12, labelpad=10, color='white')
plt.ylabel('County', fontsize=12, labelpad=10, color='white')

# Set background color
ax.set_facecolor('#1f1f1f')

# Format x-axis labels
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')

# Adjust colorbar
cbar = ax.collections[0].colorbar
cbar.ax.yaxis.label.set_color('white')
cbar.ax.tick_params(colors='white')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show() 