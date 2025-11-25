from tools.travel_api_mock import TravelAPIMock


class SearchAgent:
    """
    The SearchAgent is responsible for querying available flight options
    and filtering them according to corporate travel policy limits.
    It interacts with the TravelAPIMock tool to simulate real API calls.
    """

    def __init__(self):
        self.api = TravelAPIMock()

    def search(self, request, policy_limit):
        """
        Retrieves and filters flight options based on the policy limit.

        Parameters:
            request (dict): Structured travel request.
            policy_limit (float): Max allowed price for this travel class.

        Returns:
            list: A list of flights that fit within the policy limit.
        """

        destination = request.get("destination")

        print(f"[SearchAgent] Searching flights for {destination}...")

        # Get ALL flights for that destination
        options = self.api.get_flights(destination)

        # Filter options based on corporate budget policy
        filtered = [o for o in options if o["price"] <= policy_limit]

        # Sort by price (cheapest first)
        filtered = sorted(filtered, key=lambda x: x["price"])

        print(f"[SearchAgent] Found {len(filtered)} valid flight options.")

        return filtered
