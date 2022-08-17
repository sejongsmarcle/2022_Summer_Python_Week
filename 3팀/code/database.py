import pandas as pd
import plotly
import plotly.graph_objs as go

def save(date, title, contents, feeling):
    idx = len(pd.read_csv("database.csv"))
    new_df = pd.DataFrame({"date":date,
                        "title":title,
                        "contents":contents,
                        "feeling":feeling}, 
                        index = [idx])
    new_df.to_csv("database.csv", mode = "a", header = False)
    return None

def load_list():
    diary_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        diary_list.append(df.iloc[i].tolist())
    return diary_list

def now_index():
    df = pd.read_csv("database.csv")
    return len(df)-1

def load_diary(idx):
    df = pd.read_csv("database.csv")
    diary_info = df.iloc[idx]
    return diary_info

def avg_emotion():
    df = pd.read_csv("database.csv")
    total = 0
    for i in range(len(df)):
            total += df.iloc[i][3]
    avg = total / len(df)
    return avg

if __name__ =="__main__":
    load_list()