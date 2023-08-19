import requests

# Para calcular la rentabilidad del 12 de noviembre de 2021, tambien tambien tener una variable con la fecha del día anterior (11 de noviembte de 2021):
from_date = "2021-11-11"
to_date = "2021-11-12"

# Se crea un array con un objeto, donde cada uno contiene la info de los fondos:
funds = [
    {
        "name": "Very Conservative Streep",
        "id": "15077"
    },
    {
        "name": "Conservative Clooney",
        "id": "188"
    },
    {
        "name": "Moderate Pit",
        "id": "187"
    },
    {
        "name": "Risky Norris",
        "id": "186"
    }
]

# Ahora, creo un bucle "for" en el que se itera en cada posición del array y realiza una llamada a la API de Fintual obtener la info para cada fondo:
for fund in funds:

    fund_name = fund['name']
    fund_id = fund['id']

    url = f"https://fintual.cl/api/real_assets/{fund_id}/days?from_date={from_date}&to_date={to_date}"

    response = requests.get(url)
    responseData = response.json()

    # La llamada puede resultar en un objeto muy extenso, pero en este caso para calcular la rentabilidad, necesitamos solo el atributo "nav" o "net asset value" que representa el valor cuota de cada uno de los fondos:
    nav_riksy_11 = float(responseData['data']
                         [0]['attributes']['net_asset_value'])
    nav_riksy_12 = float(responseData['data']
                         [1]['attributes']['net_asset_value'])

    # PD: Se usa el metodo float para pasar la respuesta de formato string a numerico, para poder asi calcular el rendimiento la formula entregada:

    profit = (nav_riksy_12 - nav_riksy_11)/nav_riksy_11

    # Finalmente, se imprime el resultado por consola para cada uno de los fondos:
    print(
        f'La rentabilidad 📈 de nuestro fondo {fund_name} el {to_date} fue de: {round(profit, 4)}%')
