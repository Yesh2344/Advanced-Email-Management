# Advanced Email Management Application

A comprehensive email client that focuses on improving email management with features such as intelligent email categorization, summarization, and prioritization. This project is built using Flask and leverages NLP models for processing email content.

## Project Overview

The Advanced Email Management Application is designed to:
- **Fetch Emails:** Retrieve email data from an IMAP server.
- **Summarize Emails:** Generate concise summaries of long emails using state-of-the-art NLP models.
- **Categorize Emails:** Automatically classify emails (e.g., Work, Promotional, Finance, General) using simple rule-based logic.
- **Prioritize Emails:** Determine email priority based on sender information using basic heuristics.

## Features Implemented

### Day 1
- **Basic Flask API Setup:** 
  - Initialized a Flask application with a simple structure.
- **Email Integration:** 
  - Implemented an endpoint (`/emails`) to fetch email IDs from the INBOX via an IMAP connection.
  
### Day 2
- **Summarization Endpoint (`/summarize`):**
  - Uses a Hugging Face transformer model to generate summaries for provided email content.
- **Categorization Endpoint (`/categorize`):**
  - Analyzes email content to assign a category using simple keyword-based rules.
- **Prioritization Endpoint (`/prioritize`):**
  - Determines email priority based on the sender's address using predefined rules.

