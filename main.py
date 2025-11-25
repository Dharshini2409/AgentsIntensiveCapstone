from dotenv import load_dotenv
load_dotenv()

import json

from agents.request_agent import RequestAgent
from agents.policy_agent import PolicyAgent
from agents.search_agent import SearchAgent
from agents.booking_agent import BookingAgent
from agents.expense_agent import ExpenseAgent

from memory.session_manager import SessionManager
from memory.long_term_memory import LongTermMemory

from tools.notification_tool import NotificationTool


# Initialize system components
request_agent = RequestAgent()
policy_agent = PolicyAgent()
search_agent = SearchAgent()
booking_agent = BookingAgent()
expense_agent = ExpenseAgent()

session = SessionManager()
lt_memory = LongTermMemory()
notify = NotificationTool()


def run_travel_concierge(user_message):
    print("\n========== CORPORATE TRAVEL CONCIERGE AGENT ==========")

    # Step 1 → Parse travel request
    print("\n[1] Parsing Travel Request...")
    parsed_request = json.loads(request_agent.parse_request(user_message))
    print("Parsed Request:", parsed_request)

    session.save("current_request", parsed_request)

    # Step 2 → Validate using policy agent
    print("\n[2] Checking Policy Compliance...")
    policy_result = policy_agent.validate(parsed_request)
    print("Policy Result:", policy_result)

    if policy_result["approved"] is not True:
        print("\n❌ Travel request rejected due to policy violation.")
        return {"error": "Policy Violation", "details": policy_result}

    # Step 3 → Search for best travel options
    print("\n[3] Searching For Best Matching Flights...")
    options = search_agent.search(parsed_request, policy_result["policy_limit"])
    print("Flight Options:", options)

    if len(options) == 0:
        print("\n❌ No flights found within policy limits.")
        return {"error": "No Flight Options"}

    best_option = options[0]

    # Step 4 → Book the best option
    print("\n[4] Booking Selected Flight...")
    booking_confirmation = booking_agent.book(best_option)
    print("Booking Confirmation:", booking_confirmation)

    # Step 5 → Generate expense report draft
    print("\n[5] Creating Expense Draft...")
    expense_draft = expense_agent.create_expense_report(booking_confirmation)
    print("Expense Draft:", expense_draft)

    # Step 6 → Notify user
    print("\n[6] Sending Notification...")
    notify.send(f"Your trip to {parsed_request['destination']} is booked! Booking ID: {booking_confirmation['booking_id']}")

    # Step 7 → Store trip in long-term memory
    print("\n[7] Storing Trip in Long-Term Memory...")
    lt_memory.store_trip({
        "destination": parsed_request["destination"],
        "travel_class": parsed_request["travel_class"],
        "price": best_option["price"]
    })

    print("\n✅ Workflow Completed Successfully!")

    # Return final output
    return {
        "request": parsed_request,
        "policy_check": policy_result,
        "flight_options": options,
        "booking": booking_confirmation,
        "expense_draft": expense_draft,
        "status": "success"
    }


# Example run for testing
if __name__ == "__main__":
    print("\nRunning Demo Travel Request...\n")

    user_input = "I need to travel to Singapore from December 5 to December 8 for a client meeting. Please book economy class."
    result = run_travel_concierge(user_input)

    print("\n\n========== FINAL OUTPUT ==========\n")
    print(json.dumps(result, indent=4))
