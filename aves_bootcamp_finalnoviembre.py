# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("DATOS-AVES-QUINDIO.CSV", sep='\t') 

print("=== EXPLORACIÓN INICIAL ===")
print(f"Dimensiones del dataset: {df.shape}")
print("\nInformación del dataset:")
print(df.info())
print("\nEstadísticas descriptivas:")
print(df.describe())
print("\nValores nulos por columna:")
print(df.isnull().sum())

df_reducido=df[['species','family','individualCount','year','month','locality','basisOfRecord','recordedBy','decimalLatitude','decimalLongitude']]
df_reducido

df_reducido.describe()
df_reducido.info()


df_final=df_reducido.dropna()
df_final.info()
df_final