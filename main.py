import requests
from bs4 import BeautifulSoup
import pandas as pd

def limpiar_datos(texto):

    texto_limpio = texto.replace(",","").replace(";","").replace(".","").replace(" ","").strip()

    return int(texto_limpio) if texto_limpio.isdigit() else 0

url = "https://www.scrapethissite.com/pages/simple/"
respuesta = requests.get(url)
sopa = BeautifulSoup(respuesta.text,"html.parser")
contenedores = sopa.find_all("div",class_="country")

datos_crudos = []

for con in contenedores:

    nombre_el = con.find("h3",class_="country-name")
    capital_el = con.find("span",class_="country-capital")
    poblacion_el = con.find("span",class_="country-population")
    area_el = con.find("span",class_="country-area")

    datos_crudos.append({
        "nombre": nombre_el.text.strip() if nombre_el else "No encontrado",
        "capital": capital_el.text.strip() if capital_el else "No tiene capital",
        "poblacion": limpiar_datos(poblacion_el.text) if poblacion_el else 0,
        "area": limpiar_datos(area_el.text) if area_el else 0
    })
    
df = pd.DataFrame(datos_crudos)

df_filtrado = df[df["poblacion"] > 10000000].copy()

df_final = df_filtrado.sort_values(by="poblacion", ascending=False)

df_final.to_csv("paises_pandas.csv", index = False, sep=";", encoding="utf-8-sig")

print(f"Pipeline terminado. Se guardaron {len(df_final)} países.")
print(df_final.head())

