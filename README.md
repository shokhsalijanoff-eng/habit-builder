# Habit Builder

Habit Builder is a simple web-based productivity application designed to help users create, manage, and track personal habits.

The project started as a simple MVP and was gradually improved using software engineering practices such as GitHub Issues, feature branches, pull requests, user personas, and user stories.

## Features

### 1. Add Habit

Users can create a new habit by entering a habit name.

The application also prevents users from adding empty or whitespace-only habit names.

### 2. View Habits

Users can view all of their existing habits from the main dashboard.

Each habit shows its current completion status.

### 3. Complete Habit

Users can mark an incomplete habit as completed.

Completed habits are visually distinguished from incomplete habits.

### 4. Delete Habit

Users can delete habits that they no longer want to track.

### 5. Habit Data Persistence

Habit data is stored in a JSON file (`habits.json`).

The application loads the saved habits when the application starts and updates the file when habits are added, completed, or deleted.

### 6. Progress Statistics

The dashboard displays:

- Total number of habits
- Number of completed habits
- Number of remaining habits
- Overall completion percentage

### 7. Progress Bar

A visual progress bar represents the user's overall habit completion percentage.

### 8. Dashboard Interface

The application provides a single dashboard where users can:

- Add habits
- View habits
- Complete habits
- Delete habits
- Check overall progress

The interface uses a dark theme with a fire-orange visual style.

### 9. Responsive Design

The interface is designed to work on both desktop and smaller mobile screens.

## Technology Stack

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **JSON**
- **Git / GitHub**
- **Render**

## Project Structure

```text
habit-builder/
│
├── app.py
├── main.py
├── habits.json
├── requirements.txt
├── PRODUCT_VISION.md
├── AI_LOG.md
├── PERSONAS.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
