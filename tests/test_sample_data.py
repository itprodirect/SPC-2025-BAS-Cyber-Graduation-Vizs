import pandas as pd
from pathlib import Path


def test_gpa_over_time_columns():
    df = pd.read_csv(Path('sample_data/gpa_over_time_sample.csv'))
    assert list(df.columns) == ['Term', 'Term GPA', 'Cumulative GPA']


def test_course_grades_distribution_columns():
    df = pd.read_csv(Path('sample_data/course_grades_distribution_sample.csv'))
    assert list(df.columns) == ['Course', 'Grade']


def test_credits_attempted_vs_gpa_columns():
    df = pd.read_csv(Path('sample_data/credits_attempted_vs_gpa_sample.csv'))
    assert list(df.columns) == ['Term', 'Credits Attempted', 'Cumulative GPA']


def test_milestones_columns():
    df = pd.read_csv(Path('sample_data/milestones_sample.csv'))
    assert list(df.columns) == ['Date', 'Milestone']
