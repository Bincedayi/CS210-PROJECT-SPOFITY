
#2022 araliktan 2023 kasima kadar train ondan sonra 2023 aralik ayi test ediyor ve 2024un ilk ayi predict
#BASKA BIR FEATURE ISTIYORSAN ENERGY YAZAN YERLERI DEGISTIR
#VIDEO MAX 5DK
#TRAIN TEST PREDICTION DATA

import matplotlib.pyplot as plt
import json
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Load data
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Convert to DataFrame and preprocess
df = pd.DataFrame(songs_data)
df['endTime'] = pd.to_datetime(df['endTime'])
df.set_index('endTime', inplace=True)
monthly_data = df.resample('M').mean()

# Train-test split
train_data = monthly_data['2022-12-01':'2023-11-30']
test_data = monthly_data['2023-12-01':'2023-12-31']

# Model training for 'features'
model = RandomForestRegressor(n_estimators=100)
model.fit(train_data.index.month.values.reshape(-1, 1), train_data['danceability'])

# Predictions for test period and future months
predictions = model.predict(test_data.index.month.values.reshape(-1, 1))
test_error = mean_squared_error(test_data['danceability'], predictions)


future_months = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
future_predictions = model.predict(future_months)

print("Test Error:", test_error)
print("Predictions for the first six months of 2024:", future_predictions)


# Combine test and future predictions for plotting
all_predictions = np.concatenate((predictions, future_predictions))
all_dates = pd.date_range(start='2023-12-01', periods=len(all_predictions), freq='M')

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(all_dates, all_predictions, marker='o', color='green')
plt.xlabel('Month')
plt.ylabel('Predicted Danceability')
plt.title('Predicted Danceability from Dec 2023 to Jun 2024')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
