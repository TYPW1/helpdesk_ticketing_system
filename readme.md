
# Help Desk Ticketing System

## Overview

The **Help Desk Ticketing System** is a simple yet effective web application built using **Flask** and **SQLAlchemy**. This system allows users to submit tickets for technical support, track their status, and for support agents to manage and resolve issues. With an easy-to-use interface and integrated authentication, this tool can help teams stay organized and respond quickly to customer issues.

### Key Features

- **User Authentication**: Secure login for admins to manage tickets.
- **Ticket Submission**: Users can submit issues with descriptions and priority levels.
- **Ticket Management**: Admins can view, update the status of tickets, and mark them as resolved.
- **Simple Admin Dashboard**: Admin interface for managing all tickets and updating their status.
- **Database-Backed**: Data persistence with **SQLite** for storing ticket and user data.
- **Responsive UI**: A clean, user-friendly front-end built using HTML, CSS, and Flask templating.

## Technologies Used

- **Flask**: A lightweight Python web framework for building web applications.
- **SQLAlchemy**: An ORM (Object-Relational Mapper) to interact with the database.
- **Flask-Login**: For user authentication and session management.
- **SQLite**: A file-based database to store ticket and user data.
- **HTML/CSS**: For building the front-end and styling the web pages.
- **Werkzeug**: For password hashing and security.

## Installation

### Prerequisites

To run this project, you'll need to have **Python 3.6+** and **pip** installed. You also need to install the following Python dependencies:

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Login
```

### Steps to Set Up

1. **Clone the Repository**:
   
   Start by cloning the project to your local machine:
   ```bash
   git clone https://github.com/your-username/help-desk-ticketing-system.git
   cd help-desk-ticketing-system
   ```

2. **Create a Virtual Environment**:
   
   It's a good practice to use a virtual environment to isolate your project dependencies:
   ```bash
   python -m venv .venv
   .\.venv\Scriptsctivate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**:

   Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   
   Once everything is set up, you can run the Flask application:
   ```bash
   python app.py
   ```

   Your app will be accessible at `http://127.0.0.1:5000`.

## Usage

### 1. **Login and Authentication**:
   
   - By default, the system comes with a hardcoded admin user:
     - **Username**: `admin`
     - **Password**: `password`
   
   - Use this login to access the **Admin Dashboard**, where you can manage all tickets and their statuses.
   
### 2. **Submit a Ticket**:
   
   - Users can submit a ticket with a description and select a priority (Low, Medium, High).
   - Once submitted, the ticket will appear on the homepage and can be tracked by the user and support agents.

### 3. **Admin Dashboard**:
   
   - The **Admin Dashboard** allows support agents to view and update ticket statuses (Open, In Progress, Resolved).
   - Admins can manage tickets directly from this interface, including marking them as resolved or escalating issues.

### 4. **Ticket Status Management**:
   
   - Support agents can change the status of tickets from "Open" to "In Progress" and eventually "Resolved."
   - This system helps maintain clear communication between users and support agents.

## Features to Add

- **User Roles**: Different roles (e.g., Admin, Support Agent, User) to manage permissions and views.
- **Email Notifications**: Send email notifications when a ticket is updated or resolved.
- **User Registration**: Allow users to register and submit tickets without using hardcoded credentials.
- **Rich Text Editing**: Allow users to submit tickets with formatted text or file attachments.
- **Advanced Search & Filters**: Add the ability to search and filter tickets by status, priority, and date.
  
## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork it and create a pull request. You can help by:

- Reporting bugs or issues.
- Suggesting new features or improvements.
- Writing documentation or improving the current README.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Flask**: For making web development simple and fun.
- **SQLAlchemy**: For simplifying database management.
- **Flask-Login**: For seamless user authentication.
- **HTML/CSS**: For making the app look great.

---

Feel free to contact me if you have any questions or suggestions for improvement!
