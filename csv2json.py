import pandas as pd
import json

df = pd.read_csv('black-body-table-byte-1024.csv')

new_json = {
    'N': 1024,
    'r': list(map(int, df["RGB_r"])),
    'g': list(map(int, df["RGB_g"])),
    'b': list(map(int, df["RGB_b"]))
}

f = open("./black-body-1024.json", "w")
json.dump(new_json, f)
f.close()
