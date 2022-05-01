import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

del df["Starname"]
del df["dist"]
del df["star_mass"]
del df["star_radius"]
print(df.shape)

print(list(df))

df = df.rename({
    "Star_name": "host_name",
    "Distance":"star_distance",
    "Mass":"star_mass",
    "Radius": "star_radius",
    "Luminosity": "star_luminosity"
},axis = "columns")

df.to_csv("stars.csv")