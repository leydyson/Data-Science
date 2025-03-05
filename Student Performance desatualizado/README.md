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
Time_Spent_on_Social_Media (hours/week) – Weekly hours spent on social media (0-30 hours)
Sleep_Hours_per_Night – Average sleep duration (4-10 hours)
Final_Grade – Assigned grade based on exam score (A, B, C, D, F)


## Project Organization

```
├── README.md
│   └── Main documentation file for the project. Contains a project description, installation instructions, usage guidelines, and an overview of the results.
├── LICENSE
│   └── License file for the project. Defines the terms under which the code can be used, modified, and distributed.
├── data/
│   ├── raw/
│   │   └── Raw data directly from the sources, without any processing.
│   ├── processed/
│   │   └── Data that has been processed and cleaned, ready for analysis or modeling.
│   ├── external/
│       └── External data from third parties used in the project.
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   │   └── Jupyter notebook for exploratory data analysis (EDA). Includes charts, tables, and descriptive statistics to understand the distribution, outliers, correlations, and patterns in the data.
│   ├── model_training.ipynb
│       └── Jupyter notebook for training and evaluating machine learning models. Includes steps such as data preparation, model selection and training, performance evaluation, and hyperparameter tuning.
├── src/
│   ├── data/
│   │   └── data_preprocessing.py
│   │       └── Script for data preprocessing. Includes tasks such as cleaning, normalization, transformation, and splitting the data into training and testing sets.
│   ├── models/
│   │   └── model_training.py
│   │       └── Script for defining, training, and evaluating machine learning models. Contains functions for training the models, evaluating performance, and saving the trained models.
│   └── visualization/
│       └── create_charts.py
│           └── Script for generating charts and visualizations from the data. Includes functions to create line charts, bar charts, scatter plots, histograms, and more, using visualization libraries like Matplotlib, Seaborn, or Plotly.
├── reports/
│   ├── figures/
│   │   └── Stores figures and charts generated during the project.
│   └── final_report.pdf
│       └── Final project report, including methodology, results, and conclusions.
├── requirements.txt
│   └── File listing all the dependencies needed to run the project. Includes all the Python libraries you used.
└── .gitignore
    └── File that specifies which files and folders should be ignored by Git. This typically includes raw data, sensitive configuration files, and other temporary files that don't need to be versioned.
```

--------

