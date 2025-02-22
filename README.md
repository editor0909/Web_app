# Streamlit CRUD App with MySQL

This project is a simple CRUD (Create, Read, Update, Delete) application built using Streamlit and MySQL. It allows users to interact with a MySQL database via a Streamlit web interface.

## Features
- **Create**: Add new user records (name and email)
- **Read**: View all user records from the database
- **Update**: Modify an existing user record
- **Delete**: Remove a user record from the database

## Technologies Used
- **Python**
- **Streamlit**
- **MySQL**
- **MySQL Connector**

## Prerequisites
Before running this project, ensure you have the following installed:
- Python (>=3.7)
- MySQL Server
- Required Python libraries (install using the command below)

## Installation


1. Install the required dependencies:
   ```bash
   pip install streamlit mysql-connector-python
   ```

2. Set up the MySQL database:
   ```sql
   CREATE DATABASE crud_new1;
   USE crud_new1;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL
   );
   ```

4. Update database credentials in `app.py`:
   ```python
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_password",
       database="crud_new1"
   )
   ```

## Usage
Run the Streamlit app using:
```bash
streamlit run app.py
```

## Troubleshooting
- Ensure MySQL service is running.
- Verify database credentials in the script.
- Check if required Python dependencies are installed.

## License
This project is licensed under the MIT License.

