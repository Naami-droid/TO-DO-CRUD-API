# To-Do List Application with Basic CRUD Operations

This project implements a simple To-Do list application using FastAPI, providing basic Create, Read, Update, and Delete (CRUD) operations. The tasks are managed in an in-memory database, meaning data will not persist across application restarts.

## Features

-   **Create Task**: Add new tasks to the list.
-   **Read Tasks**: Retrieve all tasks or a specific task by its ID.
-   **Update Task**: Modify an existing task.
-   **Delete Task**: Remove a task from the list.

## Technologies Used

-   FastAPI
-   Pydantic

## How to Run

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Install dependencies**:
    ```bash
    pip install "fastapi[all]" uvicorn
    ```
3.  **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

The API documentation (Swagger UI) will be available at `http://127.0.0.1:8000/docs`.

## API Endpoints

-   `GET /`: Root endpoint.
-   `GET /health`: Health check endpoint.
-   `GET /task/{id}`: Retrieve a specific task.
-   `POST /tasks`: Create a new task.
-   `PUT /tasks/{id}`: Update an existing task.
-   `DELETE /tasks/{id}`: Delete a task.
