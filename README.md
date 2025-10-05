# TypeArena
Project Name:
TypeFlow (Typing Speed Tester with Beginner, Intermediate, Advanced Levels)

Project Description:
TypeFlow is a web-based typing speed tester built using Flask, HTML, CSS, and JavaScript.
It allows users to practice typing at three difficulty levels: Beginner, Intermediate, and Advanced, with sentences of varying lengths.

Beginner – short sentences (~5–8 words)

Intermediate – medium sentences (~12–20 words)

Advanced – long sentences (~25–50 words)

The application calculates typing speed (WPM), accuracy (%), and elapsed time in real-time.

Features:
Multi-level typing practice (Beginner / Intermediate / Advanced)

Real-time WPM, accuracy, and timer

Randomized sentences (50 sentences per level)

Glassy, semi-transparent container with background image

Simple and responsive UI with tabs for difficulty levels

Alerts show time, speed, and accuracy when a sentence is completed

Technologies Used:
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Styling: Glass effect with backdrop-filter

Randomization: Python random.choice

Installation & Setup:
Clone or download the repository.

Make sure Python is installed (Python 3.x recommended).

Install Flask:
pip install flask


Run the application:
python app.py

Folder Structure
typing_speed_tester/app.py                 # Flask backend
typing_speed_tester/ templates/ index.html          # HTML UI
typing_speed_tester/static/style.css           # Styling
typing_speed_tester/static/script.js           # JavaScript logic
typing_speed_tester/static/bg.jpg              # Background image

Usage:
Select a difficulty level by clicking on the Beginner / Intermediate / Advanced tab.

Click the Start button.

Start typing the sentence displayed in the container.

Monitor time, WPM, and accuracy in real-time.

Upon completing the sentence, an alert shows your performance.

Click Reset to try another sentence or restart the test.

Customization:
Background Image: Replace /static/bg.jpg with any image of your choice.

Sentences: Add or modify sentences in app.py for each level.

Styling: Modify style.css for colors, fonts, or container transparency.
