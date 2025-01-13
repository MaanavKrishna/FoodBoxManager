# FoodBoxManager
FoodBox Manager is a comprehensive Python-based application designed to simplify food inventory, sales, and report management. Built using Python and MySQL, this program is perfect for restaurants, food delivery services, catering businesses, or any small to medium-sized food enterprise. It offers an intuitive interface and robust functionality to keep your operations organized and efficient.

Features

1. Inventory Management
	•	Add new food items with details such as food number, name, type, price, and quantity.
	•	Modify existing records to keep the database up-to-date.
	•	Delete items that are no longer part of the menu or inventory.
	•	Search for food items using either food number or name.

2. Sales Management
	•	Record sales transactions, including date, food number, quantity sold, and price.
	•	Automatically update inventory to reflect changes in stock after each sale.
	•	Calculate total cost for each transaction.

3. Reports Generation
	•	Current Stock: View the complete inventory with all details.
	•	Profit Reports:
	•	Calculate net profit for the current day.
	•	Generate monthly profit summaries for business performance analysis.

4. Dynamic Table Creation
	•	Automatically checks and creates required database tables (inventory, sales) if they do not already exist.

5. Role-Based Menus
	•	Admin Menu: Full access to inventory, sales, and report features.
	•	User Menu: Limited access for recording sales and viewing reports.

Usage
	1.	Admin Operations:
	•	Manage inventory by adding, updating, deleting, or searching items.
	•	Record sales transactions.
	•	Generate detailed business performance reports.
	2.	User Operations:
	•	Log sales transactions.
	•	Update sales records as needed.
	3.	Reports:
	•	Track real-time inventory levels.
	•	View daily or monthly profit summaries for effective decision-making.

Technologies Used
	•	Backend: Python
	•	Database: MySQL
	•	Libraries:
	•	mysql.connector: To interact with the MySQL database.
	•	tabulate: For formatted table-like data display.

Setup Instructions
	1.	Install Python and MySQL on your system.
	2.	Install required Python libraries using:

pip install mysql-connector-python tabulate


	3.	Run the program:

python foodbox_manager.py


	4.	Ensure you have a MySQL server running and update database credentials (host, user, passwd) in the script as needed.

Future Enhancements
	•	Add role-based authentication for enhanced security.
	•	Introduce a web-based interface for easier accessibility.
	•	Enable exporting reports to CSV or Excel for external analysis.
	•	Enhance error handling and validation for smoother operation.

FoodBox Manager is designed to streamline your food business operations and help you focus on growth, not management headaches. Give it a try and see how it can make your work easier! 🎉
