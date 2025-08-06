import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_data(num_records=1000):
    np.random.seed(42)

    donor_ids = [f'DONOR_{i:04d}' for i in range(num_records)]
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    locations = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']

    data = {
        'donor_id': np.random.choice(donor_ids, num_records),
        'donation_date': [datetime.now() - timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_records)],
        'blood_type': np.random.choice(blood_types, num_records),
        'location': np.random.choice(locations, num_records),
        'donated_volume_ml': np.random.randint(250, 500, num_records),
        'last_donation_days_ago': np.random.randint(0, 365, num_records),
        'donations_in_last_year': np.random.randint(0, 4, num_records),
        'is_available_next_month': np.random.choice([0, 1], num_records, p=[0.3, 0.7]) # Target variable
    }

    df = pd.DataFrame(data)
    df = df.sort_values(by='donation_date').reset_index(drop=True)

    # Simulate recurring donors and their patterns
    for donor_id in df['donor_id'].unique():
        donor_df = df[df['donor_id'] == donor_id].copy()
        if len(donor_df) > 1:
            donor_df['last_donation_days_ago'] = (donor_df['donation_date'].max() - donor_df['donation_date']).dt.days
            df.loc[donor_df.index, 'last_donation_days_ago'] = donor_df['last_donation_days_ago']

    df.to_csv('blood_donation_system/data/synthetic_blood_data.csv', index=False)
    print('Synthetic data generated and saved to blood_donation_system/data/synthetic_blood_data.csv')

if __name__ == '__main__':
    generate_synthetic_data(num_records=5000)


