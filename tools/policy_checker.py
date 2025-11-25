class PolicyChecker:
    """
    PolicyChecker provides additional helper functions to evaluate
    corporate travel policy rules. This tool allows the PolicyAgent
    to stay clean and modular by delegating rule logic here.

    This simulates a real-world enterprise policy engine.
    """

    def check_budget_limit(self, price, limit):
        """
        Validate if the flight price meets the allowed policy limit.
        """
        if price <= limit:
            print(f"[PolicyChecker] Price {price} is within limit {limit}.")
            return True
        else:
            print(f"[PolicyChecker] Price {price} exceeds limit {limit}.")
            return False

    def check_destination_allowed(self, destination, allowed_list, disallowed_list):
        """
        Check if a destination is allowed under corporate policy.
        """
        if destination in disallowed_list:
            print(f"[PolicyChecker] Destination '{destination}' is RESTRICTED.")
            return False
        
        if destination in allowed_list:
            print(f"[PolicyChecker] Destination '{destination}' is allowed.")
            return True

        print(f"[PolicyChecker] Destination '{destination}' is not in policy lists — allowed by default.")
        return True  # default permissive rule

    def check_trip_duration(self, start_date, end_date, max_days):
        """
        Validate trip duration based on policy.

        Example:
            max_days = 10
            duration <= 10 → OK
        """
        try:
            from datetime import datetime
            
            s = datetime.fromisoformat(start_date)
            e = datetime.fromisoformat(end_date)
            duration = (e - s).days

            if duration <= max_days:
                print(f"[PolicyChecker] Trip duration {duration} days is within allowed {max_days}.")
                return True
            else:
                print(f"[PolicyChecker] Trip duration {duration} exceeds max allowed {max_days}.")
                return False

        except Exception as e:
            print(f"[PolicyChecker] Date parsing error: {e}")
            return False
