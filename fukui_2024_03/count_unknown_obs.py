import pandas as pd
import numpy as np

df = pd.read_csv("./csv/data_by_pref/延べ宿泊者数および重心（福井県）.csv", encoding="utf-8")

def count_obs(index):
    wi=df.loc[index, '北海道':'沖縄県'].values.flatten().tolist()
    wi=np.array(wi)
    o = np.ones(len(wi))
    result = np.sum(wi*o)
    return result

known = []
for i in df.index:
    inc = count_obs(i)
    known.append(inc)

df["known"] = pd.DataFrame(known) 
df["unknown"] = df["総計"]-df["known"] 

df.to_csv("./fukui_2024_03/延べ宿泊者数および重心（福井県）.csv", encoding="utf-8")

print(53.0+69.0+2214.0+1530.0+7067.0+4317.0+147.0+224.0+151.0+57.0)
    