


from scipy.stats import ttest_ind

# Load your data


import json
import pandas as pd
from scipy.stats import f_oneway

# Load data
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    data = json.load(file)

df = pd.DataFrame(data)

# Convert endTime to datetime and extract the month
df['endTime'] = pd.to_datetime(df['endTime'])
df['month'] = df['endTime'].dt.month

# Define a function to determine the season based on the month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

# Apply the function to create a season column
df['season'] = df['month'].apply(get_season)

# Choose a feature for analysis, e.g., 'energy'
feature_to_analyze = 'energy'

# Group the data by season
grouped_data = df.groupby('season')[feature_to_analyze]

# Perform one-way ANOVA
f_stat, p_value = f_oneway(*[group for name, group in grouped_data])


# Print results
alpha = 0.05  # 95% confidence level
if p_value < alpha:
    print("Reject H0: Seasonal events change do affect taste in music.")
else:
    print("Fail to reject H0: Seasonal events change do not significantly affect taste in music.")


#H0=Seasonal changes do not significantly affect taste in music.
#H1=Seasonal changes do affect taste in music.


#BU SADECE ENERJI ICIN