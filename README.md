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

