import requests

from_date = "2021-11-11"
to_date = "2021-11-12"

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

for fund in funds:

    fund_name = fund['name']
    fund_id = fund['id']

    url = f"https://fintual.cl/api/real_assets/{fund_id}/days?from_date={from_date}&to_date={to_date}"

    response = requests.get(url)
    responseData = response.json()

    nav_riksy_11 = float(responseData['data']
                         [0]['attributes']['net_asset_value'])
    nav_riksy_12 = float(responseData['data']
                         [1]['attributes']['net_asset_value'])

    profit = (nav_riksy_12 - nav_riksy_11)/nav_riksy_11

    print(
        f'La rentabilidad de nuestro fondo {fund_name} el {to_date} fue de: {round(profit, 4)}%')
