import json

class RequestAgent:
    """
    OFFLINE version of RequestAgent.
    No API calls. No internet required.
    Uses simple rule-based extraction to simulate an LLM.
    """

    def parse_request(self, user_message):
        user_message = user_message.lower()

        # Basic extraction logic
        destination = ""
        travel_class = "economy"
        reason = ""
        start_date = ""
        end_date = ""

        # Extract destination (first capitalized word in original input)
        for word in user_message.split():
            if word.istitle():
                destination = word
                break

        # Extract travel class
        if "business" in user_message:
            travel_class = "business"

        # Extract reason
        if "meeting" in user_message:
            reason = "client meeting"
        elif "conference" in user_message:
            reason = "conference"
        else:
            reason = "business purpose"

        # Extract dates (VERY SIMPLE MOCK)
        import re
        dates = re.findall(r"\d{4}-\d{2}-\d{2}", user_message)
        if len(dates) >= 2:
            start_date = dates[0]
            end_date = dates[1]
        else:
            # fallback mock dates
            start_date = "2025-12-05"
            end_date = "2025-12-08"

        # Build JSON output
        result = {
            "destination": destination or "Singapore",
            "start_date": start_date,
            "end_date": end_date,
            "travel_reason": reason,
            "travel_class": travel_class,
            "user_id": "EMP001"
        }

        # Return as JSON string
        return json.dumps(result)
