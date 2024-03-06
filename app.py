import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
np.random.seed(42)
fake = Faker()
num_users = 1000

data = {
    'user_id': range(1, num_users + 1),
    'age': np.random.randint(18, 65, size=num_users),
    'gender': np.random.choice(['M', 'F'], size=num_users),
    'subscription_plan': np.random.choice(['Basic', 'Standard', 'Premium'], size=num_users),
    'subscription_start': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_users)],
    'subscription_end': [fake.date_between(start_date='today', end_date='+1y') for _ in range(num_users)],
    'total_watch_time': np.random.randint(50, 500, size=num_users),
    'netflix_watch_time': np.random.randint(20, 200, size=num_users),
    'hulu_watch_time': np.random.randint(10, 100, size=num_users),
    'prime_watch_time': np.random.randint(10, 100, size=num_users),
    'disney_watch_time': np.random.randint(10, 100, size=num_users),
    'spotify_watch_time': np.random.randint(10, 100, size=num_users),
    'appleMusic_watch_time': np.random.randint(10, 100, size=num_users),
    'preferred_genre': np.random.choice(['Action', 'Drama', 'Comedy', 'Documentary','Sci-Fi','Horror','Romance',], size=num_users),
    #'churn_label': np.random.choice([0, 1], size=num_users)
}

df = pd.DataFrame(data)
df.to_csv('your_data.csv', index=False)
