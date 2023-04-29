import pandas as pd
df = pd.read_csv("data2.csv")
while True: 
    idx = int(input("ProfId: ").strip())
    for i in df[df["ProfId"] == idx].iterrows():
        print(i[1]["Review"])
        print("---")
