# FoodTruck Explorer

Welcome to FoodTruck Explorer, a Django-based food discovery app that allows you to explore and discover food trucks in your area. This project utilizes Docker for easy deployment and management.

## Getting Started

To run the project, follow these simple steps:

1. **Install Docker:** Make sure you have Docker installed on your machine. You can download it from [https://www.docker.com/](https://www.docker.com/).

2. **Run Docker Compose:**
   ```bash
   docker-compose up
   ```
   This command will set up the necessary containers and start the project. The app will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. **Upload CSV File:**
   Navigate to the "Upload CSV" link in the header of the app. Upload a CSV file containing food truck data and submit the form. This will populate the database with the truck information.

4. **Query Data:**
   Once you have uploaded and submitted the CSV file, you can start querying data based on longitude and latitude to find nearby food trucks.

5. **Create Superuser:**
   Run the following command to create a superuser account:
   ```bash
   make createsuperuser
   ```
   This will prompt you to enter details for the superuser account, which can be used to access the admin panel.

6. **Login to Admin Panel:**
   Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with the superuser credentials you created. Here, you can manage and view the data stored in the app.

## Project Details

- **Project Name:** FoodTruck Explorer
- **Framework:** Django
- **Containerization:** Docker
___

### Note:
**The csv containing truck data in also included in the project under 'food-truck-data.csv'**