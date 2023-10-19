# ATM-management-system-GUI-
GitHub Repository Description: ATM Management System

This GitHub repository contains the source code for an ATM (Automated Teller Machine) Management System implemented in Python using the Tkinter library for the graphical user interface. The system is designed to simulate basic ATM functionalities, including deposit, withdrawal, balance checking, fund transfers, and transaction history.

Features:

1. User Authentication:
   - The system requires users to log in with a predefined username and password (`admin`/`admin123` in this case).
   - Invalid login attempts are handled with error messages.

2. Main Functionality:
   - Deposit:
     - Users can deposit money into their account.
   - The deposited amount is added to the account balance.

   - Withdraw:
     - Users can withdraw money from their account.
     - Withdrawal is processed only if the account has sufficient funds.

   - Transfer:
     - Users can transfer money to another account.
     - Transfer is allowed only if the recipient's account exists and has sufficient funds.

   - Balance Check:
     - Users can check their account balance.

   - Transaction History:
     - Users can view a list of transactions, including deposits, withdrawals, and transfers.
     - The transaction history can be saved to a PDF file.

3. Graphical User Interface (GUI):
   - The Tkinter library is used to create a user-friendly GUI.
   - The interface includes frames, labels, entry fields, buttons, and pop-up message boxes.

4. Dark Theme:
   - The GUI is designed with a dark theme for a modern and visually appealing appearance.
   - The `customtkinter` module is utilized to enhance the GUI aesthetics.

5. PDF Report Generation:
   - The system generates a PDF report of the transaction history.
   - The report includes details such as transaction type, amount, date, and time.

6. Code Organization:
   - The code is organized into classes and functions for better modularity and readability.
   - Each major functionality (deposit, withdrawal, transfer, etc.) is encapsulated in methods within the `ATM` class.

 How to Use:
1. Clone or download the repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the main script (`atm_system.py`).
4. Enter the provided username and password to log in.
5. Explore and use the ATM functionalities through the graphical interface.

Feel free to fork and modify the code according to your requirements or contribute to its enhancement. If you encounter any issues or have suggestions, please create an issue in the repository. Happy coding!
