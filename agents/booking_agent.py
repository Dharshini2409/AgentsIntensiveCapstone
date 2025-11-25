import uuid
import datetime


class BookingAgent:
    """
    The BookingAgent is responsible for taking a selected flight option,
    creating a booking confirmation, and returning a structured response.
    This simulates a real booking workflow inside the multi-agent system.
    """

    def book(self, flight_option):
        """
        Accepts the selected flight option and generates a booking confirmation.

        Parameters:
            flight_option (dict): A flight option selected by the SearchAgent.

        Returns:
            dict: Booking confirmation details.
        """

        booking_id = str(uuid.uuid4())[:8]  # short unique ID
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        confirmation = {
            "booking_id": booking_id,
            "status": "CONFIRMED",
            "booked_at": timestamp,
            "flight_details": {
                "flight_number": flight_option.get("flight"),
                "destination": flight_option.get("destination"),
                "price": flight_option.get("price"),
                "airline": flight_option.get("airline", "N/A")
            }
        }

        print(f"[BookingAgent] Booking generated successfully: {confirmation['booking_id']}")
        return confirmation
