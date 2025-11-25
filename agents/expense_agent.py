import uuid
import datetime


class ExpenseAgent:
    """
    The ExpenseAgent is responsible for generating an expense report draft
    based on the booking confirmation. This automates a common post-travel
    workflow inside corporate environments.
    """

    def create_expense_report(self, booking):
        """
        Generates an expense report draft using booking details.

        Parameters:
            booking (dict): The booking confirmation returned by BookingAgent.

        Returns:
            dict: Expense report draft.
        """

        expense_id = str(uuid.uuid4())[:8]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        flight_price = booking["flight_details"]["price"]

        report = {
            "expense_id": expense_id,
            "status": "DRAFT",
            "created_at": timestamp,
            "booking_id": booking["booking_id"],
            "amount": flight_price,
            "breakdown": {
                "flight_cost": flight_price,
                "tax": round(flight_price * 0.08, 2),  # simulated tax
                "total": round(flight_price * 1.08, 2)
            }
        }

        print(f"[ExpenseAgent] Expense draft created: {report['expense_id']}")
        return report
