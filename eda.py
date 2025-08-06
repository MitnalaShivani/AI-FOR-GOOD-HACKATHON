import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(file_path):
    df = pd.read_csv(file_path)

    print("\n--- Dataset Info ---")
    df.info()

    print("\n--- First 5 Rows ---")
    print(df.head())

    print("\n--- Basic Statistics ---")
    print(df.describe())

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Visualizations
    plt.figure(figsize=(12, 6))
    sns.countplot(x='blood_type', data=df)
    plt.title('Distribution of Blood Types')
    plt.savefig('blood_donation_system/docs/blood_type_distribution.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.histplot(df['donated_volume_ml'], bins=20, kde=True)
    plt.title('Distribution of Donated Volume (ml)')
    plt.savefig('blood_donation_system/docs/donated_volume_distribution.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.countplot(x='is_available_next_month', data=df)
    plt.title('Distribution of Donor Availability (Next Month)')
    plt.savefig('blood_donation_system/docs/donor_availability_distribution.png')
    plt.close()

    print("EDA complete. Visualizations saved to blood_donation_system/docs/")

if __name__ == '__main__':
    perform_eda('blood_donation_system/data/synthetic_blood_data.csv')


