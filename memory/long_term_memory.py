import json
import datetime


class LongTermMemory:
    """
    Long-term memory module for storing and retrieving
    historical corporate travel data.
    This helps the system personalize recommendations
    and demonstrate memory capabilities for the capstone.
    """

    def __init__(self):
        self.db_path = "data/past_trips.json"

    def load_trips(self):
        """Loads the list of past trips from the memory file."""
        try:
            with open(self.db_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def store_trip(self, trip):
        """
        Appends a new completed trip into past_trips.json.
        
        Parameters:
            trip (dict): Trip details to store.

        Example trip:
        {
            "destination": "Singapore",
            "travel_class": "economy",
            "price": 350
        }
        """

        trips = self.load_trips()

        trip["saved_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        trips.append(trip)

        with open(self.db_path, "w") as f:
            json.dump(trips, f, indent=4)

        print(f"[LongTermMemory] Trip stored successfully.")
