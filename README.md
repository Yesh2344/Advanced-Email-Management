# Advanced Email Management Application

A comprehensive email client designed to simplify email management with advanced features such as intelligent categorization, summarization, and prioritization. This project uses a Flask backend for email processing and a simple HTML/JavaScript frontend for user interactions.

## Project Overview

The Advanced Email Management Application:
- **Fetches Emails:** Connects to an IMAP server to retrieve email data.
- **Summarizes Emails:** Uses state-of-the-art NLP models (via Hugging Face Transformers) to generate concise email summaries.
- **Categorizes Emails:** Classifies emails into categories (e.g., Work, Promotional, Finance, General) based on content.
- **Prioritizes Emails:** Determines email priority based on sender information using basic heuristics.
- **Provides a Frontend:** A simple HTML interface to interact with the backend endpoints.

## Features Implemented

### Day 1
- **Basic Flask API Setup:**
  - Created a Flask application with a foundational structure.
- **Email Integration:**
  - Implemented an `/emails` endpoint to connect to an IMAP server and fetch email IDs from the INBOX.

### Day 2
- **Summarization Endpoint (`/summarize`):**
  - Uses a Hugging Face summarization pipeline to generate summaries for provided email content.
- **Categorization Endpoint (`/categorize`):**
  - Analyzes email content using rule-based logic to assign categories.
- **Prioritization Endpoint (`/prioritize`):**
  - Determines the priority of an email based on sender information.

### Day 3
- **Frontend Integration:**
  - Developed an `index.html` file that provides a user interface to:
    - Fetch emails.
    - Summarize email content.
    - Categorize email content.
    - Prioritize emails based on the sender.
  - The frontend uses JavaScript to interact with the Flask API endpoints.
  - Addresses potential CORS issues by recommending the use of `flask-cors` on the backend.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **Virtual Environment (recommended)**
- **Gmail Account (or another email service):**
  - Ensure IMAP is enabled.
  - Use an app-specific password if using Gmail with 2FA enabled.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/advanced-email-management.git
   cd advanced-email-management
   ```

2. **Create and Activate a Virtual Environment:**

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   
   Ensure your `requirements.txt` includes:
   - flask
   - imapclient
   - transformers
   - flask-cors (if you plan to handle CORS issues)
   - python-dotenv (optional, for .env file handling)

   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   
   You can either set these manually in your command line:
   ```bash
   set EMAIL_HOST=imap.gmail.com
   set EMAIL_USER=youremail@gmail.com
   set EMAIL_PASS=your_app_specific_password
   ```

   Or create a `.env` file in your project directory with:
   ```
   EMAIL_HOST=imap.gmail.com
   EMAIL_USER=youremail@gmail.com
   EMAIL_PASS=your_app_specific_password
   ```

   And load these variables in your `app.py` using python-dotenv:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

## Running the Application

1. **Start the Flask Backend:**
   ```bash
   python app.py
   ```
   The server will run on `http://127.0.0.1:5000`.

2. **Serve the Frontend:**
   
   You can either open the `index.html` file directly in your browser or serve it using a simple HTTP server:
   ```bash
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser.

## API Endpoints

### GET `/`
Returns a welcome message.

### GET `/emails`
Fetches a list of email IDs from the INBOX.

**Response Example:**
```json
[
  { "id": 123 },
  { "id": 124 },
  { "id": 125 }
]
```

### POST `/summarize`
Generates a summary for the provided email content.

**Request Body:**
```json
{
  "email_content": "Your long email content here..."
}
```

**Response Example:**
```json
{
  "summary": "Concise summary text..."
}
```

### POST `/categorize`
Categorizes the email content using simple rule-based logic.

**Request Body:**
```json
{
  "email_content": "Let's schedule a meeting next week."
}
```

**Response Example:**
```json
{
  "category": "Work"
}
```

### POST `/prioritize`
Determines the email's priority based on the sender.

**Request Body:**
```json
{
  "sender": "boss@example.com"
}
```

**Response Example:**
```json
{
  "priority": "High"
}
```

## Testing Endpoints (Command Line)

### Summarization:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"email_content\": \"Your long email content here...\"}" http://127.0.0.1:5000/summarize
```
### Prioritization:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"sender\": \"boss@example.com\"}" http://127.0.0.1:5000/prioritize
```

## Frontend (index.html)

The provided `index.html` file offers a simple user interface to interact with the backend endpoints:

- **Fetch Emails:** Displays a list of email IDs.
- **Summarize Email:** Sends email content to generate a summary.
- **Categorize Email:** Analyzes the email content to assign a category.
- **Prioritize Email:** Evaluates sender information to determine priority.

**Note:** When serving `index.html` from a different port (e.g., 8000) than your Flask app (port 5000), you may encounter CORS issues. To resolve this, install `flask-cors` and enable CORS in your Flask app:

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

## Future Enhancements

- Expand email parsing to extract additional details (subject, sender, timestamp).
- Improve the categorization and prioritization logic with advanced ML techniques.
- Develop a more sophisticated frontend using modern JavaScript frameworks like React or Vue.js.
- Add authentication and user management.
- Implement email sending capabilities.
- Create email thread visualization.

## Troubleshooting

- **IMAP Connection Issues:** Ensure your email provider allows IMAP access and that your credentials are correct.
- **Dependency Issues:** Make sure all required packages are installed and compatible.
- **CORS Errors:** Enable CORS in your Flask application as described above.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Copyrights

@YeswanthSoma All Copyrights Reserved

## Contact

