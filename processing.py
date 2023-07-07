import pandas as pd
import sqlite3


df=pd.read_csv("C:\Calyx-TrabajoPracticoFinal\data\dnrpa-transferencias-autos-202305.csv",encoding = "utf-8")

# set 1
df1 = df[(df["automotor_origen"] == "Nacional") & (df["registro_seccional_provincia"] == "Formosa") & (df["automotor_anio_modelo"] >= 2015 )]

# set 2
df2 = df[(df["registro_seccional_codigo"] == 1216) & (df["automotor_origen"] == "Importado")]

# join sets
df_concat = pd.concat([df1, df2], axis=0)

# create 'id' and 'code_number' (code_number uses the index of each row)
df_concat.insert(0, 'id', range(len(df_concat)))
df_concat.insert(0, 'code_number', range(1, len(df_concat) + 1))

# choose the necessary columns
df_final_province = df_concat[["id","registro_seccional_provincia","titular_domicilio_provincia_id","titular_pais_nacimiento_id"]]
df_final_country = df_concat[["id","titular_pais_nacimiento_id","titular_pais_nacimiento"]]
df_final_procedure = df_concat[["id","code_number","tramite_tipo", "titular_domicilio_provincia_id"]]
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

# Save the data generated in the sub dataset in the database.
table_province = list(df_final_province.itertuples(index=False, name=None))
table_country = list(df_final_country.itertuples(index=False, name=None))
table_procedure = list(df_final_procedure.itertuples(index=False, name=None))

cursor.executemany("Insert Into Provinces Values (?, ?, ?, ?)", table_province)
cursor.executemany("Insert Into Countries Values (?, ?, ?)", table_country)
cursor.executemany("Insert Into Procedures Values (?, ?, ?, ?)", table_procedure)

conn.commit()
conn.close()