import pandas as pd
import numpy as np
import sqlite3


df=pd.read_csv("C:\Calyx-TrabajoPracticoFinal\data\dnrpa-transferencias-autos-202305.csv",encoding = "utf-8")

# set 1
df1 = df[(df["automotor_origen"] == "Nacional") & (df["registro_seccional_provincia"] == "Formosa") & (df["automotor_anio_modelo"] >= 2015 )]

# set 2
df2 = df[(df["registro_seccional_codigo"] == 1216) & (df["automotor_origen"] == "Importado")]

# join sets
df_concat = pd.concat([df1, df2], axis=0)

# create 'id' and 'code'
df_concat['id']=np.arange(len(df_concat))

# choose the necessary columns
df_final = df_concat[["id","registro_seccional_provincia","titular_domicilio_provincia_id","titular_pais_nacimiento_id"]]
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

# Save the data generated in the sub dataset in the database.

data = list(df_final.itertuples(index=False, name=None))
cursor.executemany("Insert Into Provinces Values (?, ?, ?, ?)", data)
conn.commit()
conn.close()