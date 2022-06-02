"""
Filling in the database from csv file.
"""
import sqlite3
import pandas as pd
import os
from ..session import db_path

def populate():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'posts.csv'))
    con = sqlite3.connect(db_path)
    df.to_sql("posts", con, if_exists='append', index=False)
    con.close()
