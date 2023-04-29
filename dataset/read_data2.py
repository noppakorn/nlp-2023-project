import pandas as pd
df = pd.read_csv("data2.csv")
while True:
    idx = int(input("ProfId: ").strip())
    out = ""
    for i in df[df["ProfId"] == idx].iterrows():
        out += i[1]["Review"]
        out += "\n"

    print(out.encode("unicode_escape"))
    print()
