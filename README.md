Task Manager

A task management web application built with Flask (backend) and React (frontend), integrated with MongoDB for storing tasks. It allows users to add, update, delete, and drag & drop tasks across different statuses (To-Do, In Progress, Completed).

Features

User-friendly task board with drag-and-drop functionality.

CRUD operations (Create, Read, Update, Delete) for tasks.

Flask API to handle task management.

MongoDB as a NoSQL database.

Predefined default tasks when a user logs in.

Tech Stack

Frontend: React, CSS

Backend: Flask, Flask-CORS

Database: MongoDB

State Management: React Hooks

Drag & Drop: @dnd-kit/core, @dnd-kit/sortable

Installation & Setup

Prerequisites

Ensure you have the following installed:

Node.js & npm (for React)

Python 3 & pip (for Flask)

MongoDB (running locally or using a cloud service like MongoDB Atlas)

Backend (Flask) Setup

Clone the repository:

Create and activate a virtual environment:

Install dependencies:
requitment.txt

Configure MongoDB connection in app.py:

Run the Flask server:

Frontend (React) Setup

Note: The React frontend needs to be imported from another GitHub repository.

Clone the React client repository:

Install dependencies:
"dependencies": {
        "@dnd-kit/core": "^6.3.1",
        "@dnd-kit/sortable": "^10.0.0",
        "@dnd-kit/utilities": "^3.2.2",
        "@testing-library/dom": "^10.4.0",
        "@testing-library/jest-dom": "^6.6.3",
        "@testing-library/react": "^16.2.0",
        "@testing-library/user-event": "^13.5.0",
        "axios": "^1.8.4",
        "react": "^19.0.0",
        "react-dom": "^19.0.0",
        "react-router-dom": "^7.3.0",
        "react-scripts": "5.0.1",
        "web-vitals": "^2.1.4"
      }

Start the React development server:

Library Installations

Python Libraries

Run the following command inside the backend folder:

React Libraries

Run the following command inside the frontend folder:

Usage

Sign Up: Create an account on the login page.

Login: Enter credentials to access the dashboard.

Create a Task: Click the + button to add a new task.

Drag & Drop Tasks: Move tasks between To-Do, In Progress, and Completed columns. (one colounm must contain a task , then only another task can be draged to that coloum (bug))

Edit/Delete Tasks: Click on a task to update or remove it.


Notes

Ensure MongoDB is running before starting the Flask backend.

The frontend communicates with the Flask backend via API calls.

Adjust MongoDB connection details as needed.

License

This project is open-source and available under the MIT License.

