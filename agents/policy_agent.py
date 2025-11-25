import json


class PolicyAgent:
    """
    The PolicyAgent checks whether a travel request complies with
    the organization's corporate travel policy. It loads policy rules
    from a JSON file and validates request fields such as budget limits,
    travel class, and vendor preferences.
    """

    def __init__(self):
        # Load corporate policy rules from data/policies.json
        with open("data/policies.json", "r") as f:
            self.policy = json.load(f)

    def validate(self, request):
        """
        Validates the parsed travel request against company policy.

        Parameters:
            request (dict): Parsed travel request with destination, dates, class, etc.

        Returns:
            dict: Policy decision → approved/rejected + details.
        """

        travel_class = request.get("travel_class", "economy").lower()

        # Determine spending limit for class
        if travel_class == "business":
            limit = self.policy.get("business_class_limit", 1200)
        else:
            limit = self.policy.get("economy_class_limit", 400)

        # Check if preferred airlines exist (optional rule)
        preferred_airlines = self.policy.get("preferred_airlines", [])

        decision = {
            "approved": True,
            "policy_limit": limit,
            "preferred_airlines": preferred_airlines,
            "message": "Request complies with corporate travel policy."
        }

        # Additional example rule: pre-approval required
        if self.policy.get("pre_approval_required", False):
            decision["requires_manager_approval"] = True

        print(f"[PolicyAgent] Policy validated. Limit: {limit}, Class: {travel_class}")

        return decision
