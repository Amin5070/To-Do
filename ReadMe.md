# To-Do List API with Flask and MongoDB

This is a simple RESTful API for managing a To-Do list using Flask and MongoDB. It provides basic endpoints for adding, retrieving, updating, and deleting tasks.

## Getting Started

These instructions will help you set up and run the API on local machine.

### Prerequisites

- Python 3.x
- Flask
- Flask-PyMongo
- MongoDB

### Installation

1. Install the required Python packages using pip:

   ```bash
   pip install Flask Flask-PyMongo
   ```

3. Make sure you have MongoDB running on your machine. You can install it from [MongoDB's official website](https://www.mongodb.com/try/download/community).

4. Configure MongoDB:
   - The MongoDB URI is set in `app.config["MONGO_URI"]` within the Flask application. Modify it as needed to match your MongoDB setup.

### Running the Application

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. The API should be accessible at `http://localhost:2100`.

## API Endpoints

- `GET /tasks`: Retrieve a list of tasks.
- `POST /tasks`: Add a new task.
- `PUT /tasks/<task_id>`: Update a specific task by its ID.
- `DELETE /tasks/<task_id>`: Delete a specific task by its ID.

## Testing the API

You can test the API using tools like Postman. 
