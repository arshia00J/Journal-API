# FastAPI Journal API

This is a simple Journal API built with [FastAPI](https://fastapi.tiangolo.com/). The API allows you to manage journal entries with basic CRUD operations, including creating, retrieving, updating, and deleting journal entries.

## Features

- **GET /entries**: Retrieve all journal entries with their corresponding IDs.
- **POST /entries**: Create a new journal entry with a title, content, and the current date.
- **PUT /entries/{id}**: Update an existing journal entry by its ID.
- **DELETE /entries/{id}**: Delete a journal entry by its ID.

## Installation

### Prerequisites

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/) framework
- [Uvicorn](https://www.uvicorn.org/) ASGI server

### Setup

1. Clone this repository:

```bash
git clone https://github.com/your-username/fastapi-journal-api.git
cd fastapi-journal-api
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install fastapi uvicorn
```

### Running the Application

To run the FastAPI app, use the Uvicorn ASGI server:

```bash
uvicorn main:app --reload
```

- The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### GET /entries

Retrieve all journal entries along with their IDs.

**Response Example:**

```json
[
  {
    "id": 0,
    "entry": {
      "title": "My First Entry",
      "content": "This is the content of my first journal entry.",
      "nowdate": "2024-09-25"
    }
  }
]
```

#### POST /entries

Create a new journal entry.

**Request Body Example:**

```json
{
  "title": "My New Entry",
  "content": "This is my journal entry.",
  "nowdate": "2024-09-25"
}
```

#### PUT /entries/{id}

Update an existing journal entry by its ID.

**Request Body Example:**

```json
{
  "title": "Updated Entry",
  "content": "This is the updated content.",
  "nowdate": "2024-09-25"
}
```

#### DELETE /entries/{id}

Delete a journal entry by its ID.

**Response Example:**

```json
{
  "message": "Entry deleted"
}
```

### Contributing

Feel free to submit issues, pull requests, or suggest improvements!
