import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set the style
plt.style.use('dark_background')
# The Georgia County Colour Palette [Cobb, DeKalb, Fulton, Gwinnett, Hall]
georgia_palette = ['#7874E9', '#3ED2DC', '#DEC367', '#DE7A4C', '#3E9AEB']

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
    'Date': dates.strftime('%b %d'),
    'Cobb': cobb,
    'DeKalb': dekalb,
    'Fulton': fulton,
    'Gwinnett': gwinnett,
    'Hall': hall
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Create a single figure and axis
fig, ax = plt.subplots(figsize=(15, 8))

# Plot on the specific axis
df.plot(kind='bar', stacked=False, width=0.8, color=georgia_palette, ax=ax)

# Customize the plot
plt.title('Daily Confirmed COVID-19 Cases by County for the period April 26 2020 to May 09 2020', 
          pad=40, fontsize=14, fontweight='bold', color='white')
plt.xlabel('Date', fontsize=12, labelpad=10, color='white')
plt.ylabel('Number of Cases', fontsize=12, labelpad=10, color='white')

# Ajust the y-axis limit
ax.set_ylim(0, 180)

# Customize legend
plt.legend(title='County', title_fontsize=12, fontsize=10,
          loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=5, columnspacing=1.5, handletextpad=0.5,
          facecolor='#0F3051', edgecolor='none')

# Format x-axis
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')

# Remove top and right spines, style bottom and left
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')
plt.gca().spines['bottom'].set_alpha(0.3)
plt.gca().spines['left'].set_alpha(0.3)

# Turn off grid
ax.grid(False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()