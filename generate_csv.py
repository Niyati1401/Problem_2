import csv
import os
from faker import Faker
import random
from datetime import datetime, timedelta

faker = Faker()

def generate_csv(file_path, num_records):
    # Create directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'first_name': faker.first_name(),
                'last_name': faker.last_name(),
                'address': faker.address(),
                'date_of_birth': (datetime.now() - timedelta(days=random.randint(5000, 30000))).strftime('%Y-%m-%d')
            })

if __name__ == '__main__':
    file_path = 'data/sample_data.csv'
    num_records = 10000  # Adjust based on your needs
    generate_csv(file_path, num_records)
