import requests
import datetime

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

    fund_id = fund['id']

    url = f"https://fintual.cl/api/real_assets/{fund_id}/days?from_date={from_date}&to_date={to_date}"

    response = requests.get(url)
    responseData = response.json()

    # La llamada puede resultar en un objeto muy extenso, pero en este caso para calcular la rentabilidad, necesitamos solo el atributo "nav" o "net asset value" que representa el valor cuota de cada uno de los fondos. Con un ciclo "for" recorremos todas las dias consultados:
    nav_risky = [float(data['attributes']['net_asset_value'])
                 for data in responseData['data']]

    # PD: Se usa el metodo float para pasar la respuesta de formato string a numerico, para poder asi calcular el rendimiento la formula entregada. Se calcula el profit entre la primera y ultima posición obtenida en el array "nav_risk". De esta manera se puede calcular el profit en rangos de fechas mas amplios si se lo deseara:

    profit = ((nav_risky[-1] - nav_risky[0])/nav_risky[0])*100

    return profit


# Ahora, creo un bucle "for" en el que se itera en cada posición del array y realiza una llamada a la API de Fintual obtener la info para cada fondo:
for fund in funds:
    fund_name = fund['name']
    profit = get_profit(fund, from_date, to_date)

    # Finalmente, se imprime el resultado por consola para cada uno de los fondos:
    print(
        f'La rentabilidad 📈 de nuestro fondo {fund_name} el {to_date} fue de: {round(profit, 2)}%')


# Bonus: Obtenmos el rendimiento de los ultimos 3 años :)

def get_dates(year):
    set_date = datetime.date.today()
    end_date = set_date - datetime.timedelta(days=1)
    init_date = datetime.date(
        end_date.year - year, end_date.month, end_date.day)

    return init_date, end_date


for fund in funds:
    fund_name = fund['name']
    years = [1, 2, 3]
    print(f'\nLa rentabilidad del fondo 📅 {fund_name} fue:')
    for year in years:
        year_from_date, year_to_date = get_dates(year)
        profit = get_profit(fund, year_from_date, year_to_date)
        if profit > 0:
            print(
                f'{year} año/s es de: {round(profit, 2)}% 📈')
        else:
            print(
                f'{year} año/s es de: {round(profit, 2)}% 📉')
