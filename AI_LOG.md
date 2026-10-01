# AI Collaboration Log

## Week 3 — MVP Deployment and Web Version — October 1, 2026

**Tool(s) used:** ChatGPT, VS Code, Git, GitHub, Render

**What I asked for:**
I asked AI to help convert the existing Habit Builder CLI MVP
into a Flask web application and deploy it online.

**What I kept as-is:**
I kept the original Habit Builder MVP functionality:
- Add Habit
- View Habits
- Complete Habit
- Delete Habit
- JSON-based data storage

The original `main.py` MVP was preserved.

**What I changed or rejected, and why:**
I added a Flask web interface using `app.py`, HTML templates,
CSS styling, and `requirements.txt`.

I did not replace the original MVP because it represents the
initial working version of the project.

**Something the AI got wrong that I had to catch:**
During deployment, Render initially failed because
`requirements.txt` was not included in the deployed commit.

I checked the Git status and repository structure, moved
`requirements.txt` to the project root, committed the required
web files, and pushed them to GitHub.

After the correction, the application was successfully deployed
on Render.

**Milestone result:**
The Habit Builder MVP is now available as a live Flask web
application.