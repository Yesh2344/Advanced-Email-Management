# app.py

from flask import Flask, jsonify, request
import os
import imapclient
import email

app = Flask(__name__)

# Configuration: Set these as environment variables for security.
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'imap.example.com')
EMAIL_USER = os.environ.get('EMAIL_USER', 'user@example.com')
EMAIL_PASS = os.environ.get('EMAIL_PASS', 'yourpassword')
IMAP_PORT = 993  # Standard port for IMAP over SSL

def get_mail_client():
    """Initialize and login to the IMAP server."""
    try:
        client = imapclient.IMAPClient(EMAIL_HOST, ssl=True, port=IMAP_PORT)
        client.login(EMAIL_USER, EMAIL_PASS)
        return client
    except Exception as e:
        print("Failed to connect or login to email server:", e)
        return None

@app.route('/emails', methods=['GET'])
def fetch_emails():
    """
    Fetch a list of emails from the INBOX.
    This endpoint retrieves email IDs for now and can be extended to include subjects, senders, etc.
    """
    client = get_mail_client()
    if not client:
        return jsonify({'error': 'Failed to connect to email server'}), 500
    
    try:
        client.select_folder('INBOX', readonly=True)
        message_ids = client.search(['ALL'])
        email_list = []
        for msgid in message_ids:
            # Fetch a minimal set of data. Extend this to parse subject, sender, etc.
            fetched = client.fetch([msgid], ['BODY[]', 'FLAGS'])
            email_list.append({'id': msgid})
        client.logout()
        return jsonify(email_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
