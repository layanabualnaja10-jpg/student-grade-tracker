# Student Grade Tracker

A beginner-friendly Python command-line application for tracking student grades, managing student records, and calculating class statistics.

## Features

- Add a student and their numeric grade
- View all students and grades
- Calculate the class average
- Handle empty names, non-numeric grades, and invalid menu choices
- Validate grades to ensure they are between 0 and 100
- Automatically save student records in a JSON file (`students.json`) and load them when the app starts

## Requirements

- Python 3.8 or newer
- No external libraries are required

## How to run

1. Open this folder in Visual Studio Code.
2. Open the integrated terminal.
3. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use `py main.py` instead.

## Unit 3 improvement idea

The current version checks that a grade is numeric, but it does not yet check
that the grade is between 0 and 100. A useful improvement is to reject
out-of-range grades and ask the user to enter a valid grade.

## Project structure

- `main.py` - application code
- `README.md` - project description and run instructions
- `.gitignore` - files Git should ignore
