# Student Performance & Learning Style

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This project seeks to apply machine learning and data science techniques to a database that relates study techniques that students used with their performance.

About Dataset
Student Performance & Learning Style Dataset
About the Dataset
This dataset provides insights into how different study habits, learning styles, and external factors influence student performance. It includes 10,000 records, covering details about students' study hours, online learning participation, exam scores, and other factors impacting academic success.

Dataset Features
Student_ID – Unique identifier for each student 
Age – Student's age (18-30 years)
Gender – Male, Female, or Other
Study_Hours_per_Week – Hours spent studying per week (5-50 hours)
Preferred_Learning_Style – Visual, Auditory, Reading/Writing, Kinesthetic
Online_Courses_Completed – Number of online courses completed (0-20)
Participation_in_Discussions – Whether the student actively participates in discussions (Yes/No)
Assignment_Completion_Rate (%) – Percentage of assignments completed (50%-100%)
Exam_Score (%) – Student’s final exam score (40%-100%)
Attendance_Rate (%) – Percentage of classes attended (50%-100%)
Use_of_Educational_Tech – Whether the student uses educational technology (Yes/No)
Self_Reported_Stress_Level – Student’s stress level (Low, Medium, High)
Time_Spent_on_Social_Media (hours/week) – Weekly hours spent on social media (0-30 hours)\**
Sleep_Hours_per_Night – Average sleep duration (4-10 hours)
Final_Grade – Assigned grade based on exam score (A, B, C, D, F)


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         ds_analysis_tool and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── ds_analysis_tool   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes ds_analysis_tool a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── imports.py              <- Useful imports 
    |
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

