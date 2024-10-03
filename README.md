# Task-Management-Application

    Coding Temple - Module 9: Mini-Project

## Introduction:

Welcome to the Task Management Application, a user-friendly and efficient tool designed to help you manage tasks effectively. Built with Flask and Bootstrap, this application leverages modern web technologies to provide a responsive and interactive experience for users.


## Technologies Used:

1. Flask: The web framework powering the backend.
2. Marshmallow: For object serialization and deserialization.
3. SQLAlchemy: As the ORM for database interactions.
4. MySQL: For data storage and management.
5. Flask-Bcrypt: To securely hash and salt passwords.
6. Jinja2: For dynamic HTML rendering.
7. HTML/CSS/Bootstrap: To create a responsive and visually appealing front-end.
8. JavaScript: Enhancing interactivity across the application.


## Features

### Task Management:

1. **Home Page:**
    - A welcoming landing page featuring a Navbar, Jumbotron for the welcome message, and Cards to display key features of the application.

2. **Task Dashboard Page:**
    - An interactive dashboard utilizing Cards, Forms, and Buttons to manage tasks efficiently.

3. **Task Details Page:**
    - A detailed view for individual tasks, including Cards and Forms for easy editing.

4. **Task Creation Page:**
    - A Bootstrap Form layout for adding new tasks with input validation.

5. **Registration Page:**
    - Allows new users to sign up with a Bootstrap Form and built-in validation.

6. **Authentication Page:**
    - Users can log in using a secure form layout, complete with validation for credentials.


### User Experience Enhancements:

1. **Interactive Top Navigation:**
    - A dynamic navbar that adapts based on user authentication.

2. **Animated Progress Bars:**
    - Visual indicators of task completion, motivating users to finish their tasks.

3. **Intuitive Color Adjustments:**
    - Color-coded task priority and progress levels for easy identification.

4. **Embedded Collaboration Links:**
    - Convenient links to tools like Microsoft Teams, Slack, Discord, Dropbox, Google, and GitHub.

5. **Form Validation:**
    - Comprehensive validation steps for all forms ensure data integrity and a smooth user experience.


### Bootstrap Integration:

1. Utilizes Bootstrap's grid system for responsive layout design and consistent styling across all pages.

2. Applies Bootstrap typography, color palette, and utilities for a cohesive look.
Responsive Design

3. Ensures accessibility across various devices using Bootstrap's responsive grid and utilities.

4. Tested for responsiveness with Bootstrap's built-in breakpoint classes and media queries.


### Database Integration:

1. **User and UserAccount Management:**
    - Implemented endpoints for managing users and their associated accounts.
    - Capture essential user information, including name, email, phone number, and preferred contact methods.
    - Securely stores and manages user account details, including username and password.

2. **Database Management:**
    - Utilizes Flask-SQLAlchemy to integrate a MySQL database into the application.
    - Creates the necessary database models to represent users, user accounts, and tasks.
    - Established proper relationships between the database tables.


### Bonus Features:

1. **Accordion Component:**
    - Accordions for organizing tasks, providing a clean layout.



## Getting Started
To get a local copy up and running, follow these steps:

### Prerequisites
- Python 3.x
- MySQL Community Server
- MySQL Workbench
- Python dependencies:
  - Flask
  - Flask-SQLAlchemy
  - Flask-Marshmallow
  - Flask-Bcrypt
  - mysql-connector-python

## Installation:
*** **GitHub Repository** ***

[Task Management Application Module9-MiniProject Repository](https://github.com/Tmiseray/Task-Management-Application)

*** **Cloning Option** ***
* If you have Git Bash installed, you can clone the repository using the URL
1. Create a 'Clone' Folder
2. Within the folder, right-click for Git Bash
3. From the GitHub Repository, click on the '<> Code' button and copy the link provided
4. Paste the link into your Git Bash and click 'Enter'
* If you have GitHub Desktop, when you click on the '<> Code' button you will have an option to 'Open with GitHub Desktop'
* If you have Visual Studio Code, when you click on the '<> Code' button you will have an option to 'Open with Visual Studio'
* [HTTPS] (https://github.com/Tmiseray/Task-Management-Application.git)
* [SSH] (git@github.com:Tmiseray/Task-Management-Application.git)
* [GitHubCLI] (`gh repo clone Tmiseray/Task-Management-Application`)

*** **Download Option** ***
1. From the GitHub Repository, click on the '<> Code' button
2. Click on 'Download Zip'
3. Extract contents of Zip file

*** **Update File & Run App** ***
1. Update the database connection details in the `app.py` & `password.py` files:
   - Locate the line `app.config['SQLALCHEMY_DATABASE_URI']` and replace the placeholder values with your MySQL connection details.
   - Locate the `password.py` file and replace the placeholder with your password. You can also update the secret key too!
2. Start the Flask application:
   ```
   python app.py
   ```
   OR
   ```
   flask run
   ```


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.
