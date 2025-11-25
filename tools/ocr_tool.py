class OCRTool:
    """
    OCRTool simulates Optical Character Recognition for extracting
    text or numeric values from receipt images or uploaded files.

    In a real system, this would use:
    - pytesseract
    - AWS Textract
    - Google Vision API
    - Azure OCR

    For this capstone project, we simulate extraction behavior.
    """

    def extract_amount(self, receipt_text: str):
        """
        Extracts a numeric amount from a given receipt text string.

        Parameters:
            receipt_text (str): OCR-extracted raw text from a receipt.

        Returns:
            float: Extracted amount value.
        """

        # Simulated behavior: search for something like "Total: 350"
        for token in receipt_text.split():
            token = token.replace("$", "")
            if token.isdigit():
                print(f"[OCRTool] Amount extracted from receipt: {token}")
                return float(token)

        print("[OCRTool] No valid amount found in receipt text.")
        return None
