class TravelAPIMock:
    """
    TravelAPIMock simulates an external travel search API.
    It returns a predefined list of flight options for any destination.

    In real-world applications, this would be replaced by:
    - Amadeus API
    - Skyscanner API
    - Sabre API
    - Cleartrip / MakeMyTrip APIs

    For this capstone project, we use static mock data
    to demonstrate tool integration.
    """

    def get_flights(self, destination):
        """
        Returns a list of mock flight options for the given destination.

        Parameters:
            destination (str): The city the user wants to travel to.

        Returns:
            list of dicts: Each containing flight data.
        """

        print(f"[TravelAPIMock] Retrieving mock flights for {destination}...")

        # Simulated static sample flight database
        flights = [
            {
                "flight": "AI-101",
                "airline": "Air India",
                "destination": destination,
                "price": 350,
                "duration": "5h 40m"
            },
            {
                "flight": "EM-220",
                "airline": "Emirates",
                "destination": destination,
                "price": 450,
                "duration": "6h 10m"
            },
            {
                "flight": "SQ-019",
                "airline": "Singapore Airlines",
                "destination": destination,
                "price": 300,
                "duration": "5h 30m"
            }
        ]

        return flights
