Flask Vocabulary App
Overview
This Flask-based web application was developed to help School Psychology students, like my girlfriend, practice and remember important vocabulary terms through flashcards. The app allows users to create, update, delete, and view vocabulary words and their meanings.

The project has been dockerized and deployed on AWS using AWS AppRunner, with images pushed to AWS Elastic Container Registry (ECR).

Features
Flashcards for Psychology Vocabulary: Users can add, view, update, and delete vocabulary words.
Vocabulary Management: The app uses an in-memory dictionary for storing words and their meanings.
Simple API Integration: It provides APIs for basic CRUD (Create, Read, Update, Delete) operations on the vocabulary.
Web-based User Interface: A user-friendly interface to view and manage the vocabulary.
Dockerized Deployment: The application is containerized using Docker and deployed on AWS via AppRunner.
Tech Stack
Flask: A lightweight web framework for Python.
Flask-SQLAlchemy: For database interactions (if future enhancements are made to integrate with a persistent database).
Docker: To containerize the application.
AWS AppRunner: For seamless deployment of the application.
AWS ECR: To store Docker images used in deployment.
Installation
To run the application locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/vocabulary-app.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
export FLASK_APP=app.py
flask run
The app will be available at http://localhost:5000.

Docker Deployment
To run the application using Docker:

Build the Docker image:

bash
Copy code
docker build -t vocabulary-app .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 vocabulary-app
The app will be accessible at http://localhost:5000.

AWS Deployment
This app has been deployed to AWS AppRunner for scalable, managed container hosting.

Push the Docker image to AWS ECR:

Set up AWS AppRunner to deploy the application from ECR.

Future Enhancements
User Authentication: Add user login functionality to personalize the flashcards experience.
Enhanced User Interface: Improve the UI/UX to make it more interactive and visually appealing.

Contributing
Feel free to submit pull requests if you'd like to contribute!