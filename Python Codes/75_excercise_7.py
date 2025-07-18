# clear the cluster

import os
files = os.listdir("75_clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"75_clutteredFolder/{file}", f"75_clutteredFolder/{i}.png")
        i = i + 1