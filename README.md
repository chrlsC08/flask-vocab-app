🎓 Flask Vocabulary App - Psychology Flashcards
Overview
Ever wondered how psychology students keep up with all the specialized vocabulary they need to master? I built this Flask-based web app for my girlfriend, a School Psychology grad student, to help her—and others like her—memorize crucial terms through interactive flashcards. With this app, users can easily create, update, delete, and view vocabulary words and definitions, all within a clean, simple interface.

Not only is this a fun and useful tool for students, but it's also fully dockerized and deployed on AWS using AppRunner, with images hosted in Elastic Container Registry (ECR)—a project made to scale and serve more than just my girlfriend's flashcard needs!

✨ Features
Flashcards for Psychology Vocabulary: Users can add, view, update, and delete vocabulary words for seamless studying.
Vocabulary Management: Powered by an in-memory dictionary for lightning-fast lookups.
Simple API Integration: Complete CRUD (Create, Read, Update, Delete) API support for managing vocabulary terms.
Web-based User Interface: A user-friendly interface to manage words and meanings effortlessly.
Dockerized Deployment: Runs as a fully containerized app, ensuring consistency across environments.
Deployed on AWS: Hosted with AWS AppRunner for scalable and managed container hosting.

🛠️ Tech Stack
Flask: The app is built with Flask, a lightweight Python web framework.
Flask-SQLAlchemy: Though the current app uses an in-memory dictionary, it's future-ready for persistent databases with SQLAlchemy.
Docker: For easy containerization and deployment.
AWS AppRunner: Deploys the app with zero hassle, ensuring scalability and high availability.
AWS ECR: Used for storing Docker images.

🚀 Getting Started
Local Installation
Want to try it out on your machine? Follow these steps:

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
Your app will now be running at http://localhost:5000 🎉.

Docker Deployment
Prefer running things in a container? Here's how:

Build the Docker image:

bash
Copy code
docker build -t vocabulary-app .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 vocabulary-app
Open http://localhost:5000 in your browser and you're good to go!

AWS Deployment
AWS Deployment This app has been deployed to AWS AppRunner for scalable, managed container hosting.

Push the Docker image to AWS ECR:

Set up AWS AppRunner: Use AWS AppRunner to deploy the application directly from ECR.

🌟 Future Enhancements
User Authentication: Allow users to log in and track their personal vocab lists.
Persistent Database: Integrate with PostgreSQL or MySQL to make vocabulary data permanent.
UI Improvements: Enhance the UI with flashier designs and a better user experience.

🤝 Contributing
Got ideas for improvement? Found a bug? Feel free to fork this repo and submit a pull request. All contributions are welcome!