import glob
import pandas as pd

df = pd.DataFrame()

for i in glob.glob("*.csv"):
    df_current = pd.read_csv(i).set_index("id")
    df = df.append(df_current)

df = df.sort_index()

print(df)
df.to_csv("combined.csv")
