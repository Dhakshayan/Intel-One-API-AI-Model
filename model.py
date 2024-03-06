from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
from faker import Faker
df = pd.read_csv('your_data.csv')
X = df.drop(['user_id', 'subscription_start', 'subscription_end'], axis=1)
y = df[['netflix_watch_time', 'hulu_watch_time', 'prime_watch_time', 'disney_watch_time', 'spotify_watch_time', 'appleMusic_watch_time']].idxmin(axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))