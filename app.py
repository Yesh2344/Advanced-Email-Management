# app.py

from flask import Flask, jsonify, request
import os
import imapclient
from transformers import pipeline

app = Flask(__name__)

# Email server configuration (use environment variables for real deployments)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'imap.example.com')
EMAIL_USER = os.environ.get('EMAIL_USER', 'user@example.com')
EMAIL_PASS = os.environ.get('EMAIL_PASS', 'yourpassword')
IMAP_PORT = 993  # Standard IMAP over SSL port

# Load the summarization pipeline (this may take a moment on first run)
summarizer = pipeline("summarization")

def get_mail_client():
    """Initialize and login to the IMAP server."""
    try:
        client = imapclient.IMAPClient(EMAIL_HOST, ssl=True, port=IMAP_PORT)
        client.login(EMAIL_USER, EMAIL_PASS)
        return client
    except Exception as e:
        print("Failed to connect or login to email server:", e)
        return None

@app.route('/')
def index():
    return "Welcome to the Advanced Email Management Application API!"

@app.route('/emails', methods=['GET'])
def fetch_emails():
    """
    Fetch a list of emails from the INBOX.
    Currently returns minimal information (email IDs).
    """
    client = get_mail_client()
    if not client:
        return jsonify({'error': 'Failed to connect to email server'}), 500
    
    try:
        client.select_folder('INBOX', readonly=True)
        message_ids = client.search(['ALL'])
        email_list = []
        for msgid in message_ids:
            # For simplicity, only returning the email ID.
            email_list.append({'id': msgid})
        client.logout()
        return jsonify(email_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summarize', methods=['POST'])
def summarize():
    """
    Generate a summary for the provided email content.
    Expects JSON: { "email_content": "long email text" }
    """
    data = request.get_json()
    email_content = data.get("email_content", "")
    if not email_content:
        return jsonify({"error": "No email content provided"}), 400
    try:
        summary_result = summarizer(email_content, max_length=130, min_length=30, do_sample=False)
        # The summarizer returns a list of dicts; return the summary text of the first item.
        return jsonify({"summary": summary_result[0]['summary_text']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/categorize', methods=['POST'])
def categorize():
    """
    Categorize the email based on its content.
    Expects JSON: { "email_content": "email text" }
    """
    data = request.get_json()
    email_content = data.get("email_content", "").lower()
    if not email_content:
        return jsonify({"error": "No email content provided"}), 400
    
    # Simple rule-based categorization:
    if "meeting" in email_content or "schedule" in email_content:
        category = "Work"
    elif "discount" in email_content or "offer" in email_content:
        category = "Promotional"
    elif "invoice" in email_content or "receipt" in email_content:
        category = "Finance"
    else:
        category = "General"
    
    return jsonify({"category": category})

@app.route('/prioritize', methods=['POST'])
def prioritize():
    """
    Determine the priority of an email based on sender details.
    Expects JSON: { "sender": "email@example.com" }
    """
    data = request.get_json()
    sender = data.get("sender", "").lower()
    if not sender:
        return jsonify({"error": "No sender provided"}), 400
    
    # Example: Emails from these contacts are high priority.
    important_contacts = ["boss@example.com", "ceo@example.com"]
    priority = "High" if sender in important_contacts else "Normal"
    
    return jsonify({"priority": priority})

if __name__ == '__main__':
    app.run(debug=True)
