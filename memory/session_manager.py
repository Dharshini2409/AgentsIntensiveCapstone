class SessionManager:
    """
    SessionManager handles short-term memory for the active workflow.
    It stores temporary session data such as:
    - parsed travel request
    - selected flight option
    - policy result
    - current workflow step

    This ensures the agent maintains context across multi-step operations.
    """

    def __init__(self):
        # Store session data using a simple dictionary
        self.session_data = {}

    def save(self, key, value):
        """
        Saves a key-value pair into session memory.

        Example:
            save("current_request", {...})
        """
        self.session_data[key] = value
        print(f"[SessionManager] Saved '{key}'")

    def load(self, key):
        """
        Retrieves value from session memory.
        Returns None if not found.
        """
        value = self.session_data.get(key)
        print(f"[SessionManager] Loaded '{key}': {value}")
        return value

    def clear(self):
        """
        Clears all temporary workflow data.
        Use this after the travel request completes.
        """
        self.session_data = {}
        print("[SessionManager] Cleared all session data")
