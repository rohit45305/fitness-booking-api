from fastapi.testclient import TestClient
from fitness_booking_api import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_booking_and_get_bookings():
    # First get classes to find a valid class_id
    classes_response = client.get("/classes")
    classes = classes_response.json()
    if not classes:
        return
    
    class_id = classes[0]['id']

    # Create a booking
    booking_data = {
        "class_id": class_id,
        "client_name": "Test User",
        "client_email": "testuser@example.com"
    }
    response = client.post("/book", json=booking_data)
    assert response.status_code == 200
    booking = response.json()
    assert booking['client_email'] == "testuser@example.com"
    assert booking['class_id'] == class_id

    # Get bookings for the email
    response = client.get(f"/bookings?client_email=testuser@example.com")
    assert response.status_code == 200
    bookings = response.json()
    assert any(b['client_email'] == "testuser@example.com" for b in bookings)
