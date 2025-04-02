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

