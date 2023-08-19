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


def get_profit(fund, from_date, to_date):

    fund_name = fund['name']
    fund_id = fund['id']

    url = f"https://fintual.cl/api/real_assets/{fund_id}/days?from_date={from_date}&to_date={to_date}"

    response = requests.get(url)
    responseData = response.json()

    # La llamada puede resultar en un objeto muy extenso, pero en este caso para calcular la rentabilidad, necesitamos solo el atributo "nav" o "net asset value" que representa el valor cuota de cada uno de los fondos. Con un ciclo "for" recorremos todas las dias consultados:
    nav_risky = [float(data['attributes']['net_asset_value'])
                 for data in responseData['data']]

    # PD: Se usa el metodo float para pasar la respuesta de formato string a numerico, para poder asi calcular el rendimiento la formula entregada. Se calcula el profit entre la primera y ultima posición obtenida en el array "nav_risk". De esta manera se puede calcular el profit en rangos de fechas mas amplios si se lo deseara:

    profit = (nav_risky[-1] - nav_risky[0])/nav_risky[0]

    # Finalmente, se imprime el resultado por consola para cada uno de los fondos:
    print(
        f'La rentabilidad 📈 de nuestro fondo {fund_name} el {to_date} fue de: {round(profit, 4)}%')


# Ahora, creo un bucle "for" en el que se itera en cada posición del array y realiza una llamada a la API de Fintual obtener la info para cada fondo:
for fund in funds:
    get_profit(fund, from_date, to_date)
