# Corvit Student Feedback System

A Flask-based web application where students of Corvit Institute of Information Technology can submit course and institute feedback, and admins can manage questions, review submissions and view an AI-powered feedback report.

## Features

### Student Portal
- Student login with name, registration number and course selection
- Feedback form divided into sections (instructor, course content, labs, administration, career support, overall satisfaction, open-ended)
- Rating (1-5), Yes/No and text-answer questions
- Thank-you page after submission

### Admin Portal
- Secure admin login (hashed passwords)
- Dashboard with total feedbacks, average rating, positive and negative feedback counts
- Course-wise and section-wise performance tables
- Recent submissions list
- Student submissions page with search and course filter
- Detailed view of each submission, with delete option
- Manage questions: add, edit and delete questions and sections
- AI Report page with:
  - Overall sentiment and sentiment breakdown (positive / negative / neutral)
  - Priority level
  - Most mentioned and detected topics
  - Topic-wise and course-wise insights
  - Top strengths and complaints
  - Improvement suggestions
  - Student comments

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Sentiment Analysis:** TextBlob
- **Frontend:** HTML, CSS, Jinja2 templates
- **Security:** Werkzeug password hashing

## Project Structure

```
├── app.py
├── database.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── home.html
    ├── student_login.html
    ├── feedback_form.html
    ├── thank_you.html
    ├── admin_login.html
    ├── admin_dashboard.html
    ├── student_submissions.html
    ├── submission_detail.html
    ├── manage_questions.html
    └── ai_report.html
```

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create the database and add default data:
   ```
   python database.py
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

## Default Admin Login

```
Username: admin
Password: admin123
```

> **Important:** Change the default password and the `secret_key` in `app.py` before using this project in a real environment.

## Database Tables

- `admins` - admin accounts
- `courses` - list of courses
- `questions` - feedback questions (section, text, type, active status)
- `submissions` - student submissions with average rating and sentiment
- `answers` - answers for each submission

## Author

**Rida Shahzadi**
BS Computer Science, Arid Agriculture University Rawalpindi
