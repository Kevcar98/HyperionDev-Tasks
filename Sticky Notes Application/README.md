# Sticky Notes Application

## Table of Contents
- [Project Name](#project-name)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

cis a web-based platform developed using Django that allows users to create, read, update, and delete notes. This project demonstrates the fundamental aspects of web development, including working with models, views, templates, and forms in Django. Additionally, it showcases how to implement basic user interactions and manage data persistence.

Learning to build this application is essential for understanding the core principles of the Django framework and how to structure a web application using the Model-View-Template (MVT) architecture.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sticky-notes-application.git
   cd sticky-notes-application

2. **Create and activate a virtual environment:**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

4. *Apply migrations:**:
   ```bash
   python manage.py migrate

5. **Run the development server:**:
   ```bash
   python manage.py runserver



## Usage
After installing the application, you can use it to manage your sticky notes.

1. **Access the application:**
Open your web browser and navigate to http://127.0.0.1:8000/.


3. **Create a new note:**

Click on "Create New Note".
Fill in the title and content fields.
Click "Save" to create the note.
3. **View a note:**

Click on the title of a note in the list to view its details.


4. **Edit a note:**

In the note detail view, click on the "Edit" button.
Update the title or content.
Click "Save" to update the note.


5. **Delete a note:**

In the note detail view, click on the "Delete" button.
Confirm the deletion in the confirmation dialog.


6. **Bulletin Board Posts:**

Access the bulletin board section by navigating to http://127.0.0.1:8000/bulletin/.
Follow similar steps to create, view, edit, and delete posts.

##Credits
Developed by Kevin Caraballo Rodrigues.
