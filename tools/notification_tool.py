class NotificationTool:
    """
    NotificationTool simulates sending notifications to the employee.
    In a production system, this could connect to:
    - Email server
    - Slack / MS Teams API
    - SMS gateways

    For this project, we print the message to the console to represent
    a successful notification delivery.
    """

    def send(self, message: str):
        """
        Sends a notification message.

        Parameters:
            message (str): Notification text to be delivered.

        Returns:
            None
        """

        print(f"[NOTIFICATION SENT] {message}")
