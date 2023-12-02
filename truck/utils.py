import csv
import io
from datetime import datetime

from truck.models import Truck


def date_parser(date_string):
    """parse dat into db acceptable format"""
    if date_string:
        # Parse the date string
        parsed_date = datetime.strptime(date_string, "%m/%d/%Y %I:%M:%S %p")
        # Format the parsed date as "YYYY-MM-DD"
        return parsed_date.strftime("%Y-%m-%d")
    return None


def load_data_from_csv(csv_file):
    """Load data from csv file to Truck model"""
    with io.TextIOWrapper(csv_file, encoding="utf-8", newline='\n') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                Truck.objects.create(
                    location_id=row['locationid'],
                    applicant=row['Applicant'],
                    facility_type=row['FacilityType'],
                    cnn=row['cnn'],
                    location_description=row['LocationDescription'],
                    address=row['Address'],
                    block_lot=row['blocklot'],
                    block=row['block'],
                    lot=row['lot'],
                    permit=row['permit'],
                    status=row['Status'],
                    food_items=row['FoodItems'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    schedule=row['Schedule'],
                    days_hours=row['dayshours'],
                    noi_sent=row['NOISent'],
                    approved=date_parser(row['Approved']),
                    received=row['Received'],
                    prior_permit=row['PriorPermit'],
                    expiration_date=date_parser(row['ExpirationDate']),
                    location=row['Location'],
                    fire_prevention_districts=row['Fire Prevention Districts'] or None,
                    police_districts=row['Police Districts'] or None,
                    supervisor_districts=row['Supervisor Districts'] or None,
                    zip_codes=row['Zip Codes'],
                    neighborhoods_old=row['Neighborhoods (old)'] or None,
                )
            except:
                pass
