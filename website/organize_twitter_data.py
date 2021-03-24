import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import sqlite3 as sql
import io
import base64


def graph():
    img = io.BytesIO()
    conn = sql.connect('db.sqlite')
    df = pd.read_sql('SELECT name,volume FROM twitter_trends ORDER BY volume DESC', conn)
    if df.empty:
        return None
    else:
        df = df.dropna()
        df = df.head(10)
        plt.figure(figsize=(12, 12))
        sb.barplot(x="name", y="volume", data=df)
        plt.xticks(rotation=45)
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.clf()
        plt.close()
        return plot_url
