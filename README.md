## Flask Application Design: Rent Tracking App

### HTML Files:
1. **login.html**: Designed for users to log in to the application with appropriate credentials. It includes fields for email and password along with a submit button.
2. **dashboard.html**: Serves as the main interface for users after successful login. It presents an overview of all shops, their rent status, electricity meter readings, and common area maintenance details.
3. **shop_details.html**: Provides detailed information for a specific shop. It displays rent history, electricity consumption data, and allows for entering meter readings or marking rent payments as paid/unpaid.
4. **reports.html**: Allows users to generate reports in various formats (PDF, CSV, JSON) for different aspects of the application data, such as shop rents, electricity consumption, or common area maintenance expenses.

### Routes:
1. **login**: Handles user login and redirects to the dashboard upon successful authentication.
2. **dashboard**: Displays the dashboard page with summarized information for all shops.
3. **shop_details/<shop_id>**: Shows detailed information for a specific shop, including rent history, electricity meter readings, and maintenance expenses.
4. **mark_rent_paid/<rent_id>**: Allows users to mark a specific rent payment as paid.
5. **mark_rent_unpaid/<rent_id>**: Allows users to mark a specific rent payment as unpaid.
6. **enter_meter_reading/<shop_id>**: Lets users enter the electricity meter reading for a specific shop.
7. **common_area_maintenance/<shop_id>**: Enables users to enter common area maintenance expenses for a specific shop.
8. **generate_report/<report_type>**: Generates reports in different formats based on the report type specified.

### Additional Notes:
- The database schema will contain tables for shops, rents, electricity meter readings, and common area maintenance expenses.
- The application should employ appropriate data validation techniques to ensure data integrity.
- The application should implement security measures such as password hashing and role-based access control to ensure data protection.