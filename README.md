# Fitness Booking API

A simple REST API for a fictional fitness studio offering classes like Yoga, Zumba, and HIIT.

## Features

- List all upcoming classes with time zone support
- Book a class with validation of available slots
- View bookings by client email

## Tech Stack

- Python 3.8+
- FastAPI
- SQLite (via SQLAlchemy ORM)
- Pydantic for request validation
- Timezone handling using `pytz`

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd fitness-booking-api
2. Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate 

3. Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

4. Run the API:

bash
Copy
Edit
uvicorn fitness_booking_api:app --reload

5. The API will be available at: http://127.0.0.1:8000
