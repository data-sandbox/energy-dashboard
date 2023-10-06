import os
import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
# TODO from typing import List, Optional, Tuple, Union
from plotting import plot_monthly, plot_annual

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


def query_api(url, params):
    print("Querying API...")
    response = requests.get(url, params=params)
    return response.json()


def create_df(json, frequency):
    print("Creating dataframe...")
    data = json['response']['data']
    df = pd.DataFrame(data)
    if frequency == 'monthly':
        df['period'] = pd.to_datetime(df['period'])
    elif frequency == 'annual':
        df['period'] = pd.to_datetime(df['period'], format='%Y')
    else:
        raise TypeError("Supports only 'monthly' or 'annual")
    return df


def save_chart(chart, name):
    print("Saving chart...")
    chart.save(f'src/data/{name}.json')
    return


def create_chart(facets, frequency, axis_title, chart_name):
    print(f'Initializing {chart_name}_{frequency} chart...')
    if frequency == 'monthly':
        startDate = date.today() + relativedelta(years=-shortTerm)
        start_string = f"{startDate.year}-{startDate.strftime('%m')}"
    elif frequency == 'annual':
        startDate = date.today() + relativedelta(years=-longTerm)
        start_string = f"{startDate.year}-01"
    else:
        raise TypeError("Supports only 'monthly' or 'annual")

    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": start_string,
              "offset": 0,
              "length": 5000}

    response = query_api(url, params)
    df = create_df(response, frequency)
    if frequency == 'monthly':
        chart = plot_monthly(df, axis_title)
    elif frequency == 'annual':
        chart = plot_annual(df, axis_title)
    else:
        raise TypeError("Supports only 'monthly' or 'annual")

    save_chart(chart, f'{chart_name}_{frequency}')

    return


if __name__ == "__main__":

    token = os.getenv("API_KEY")
    url = 'https://api.eia.gov/v2/total-energy/data/'

    shortTerm = 3
    longTerm = 20

    # Consumption
    chart_name = 'consumption'
    facets = ["CLTCBUS", "NNTCBUS", "PMTCBUS", "NUETBUS", "RETCBUS"]
    axis_title = 'Energy Consumption (Trillion Btu)'
    create_chart(facets, frequency='monthly',
                 axis_title=axis_title,
                 chart_name=chart_name)

    create_chart(facets, frequency='annual',
                 axis_title=axis_title,
                 chart_name=chart_name)

    # Production
    chart_name = 'production'
    facets = ["REPRBUS", "BMPRBUS", "NUETBUS",
              "NLPRBUS", "PAPRBUS", "NGPRBUS", "CLPRBUS"]
    axis_title = 'Energy Production (Trillion Btu)'
    create_chart(facets, frequency='monthly',
                 axis_title=axis_title,
                 chart_name=chart_name)

    create_chart(facets, frequency='annual',
                 axis_title=axis_title,
                 chart_name=chart_name)

    # Energy Prices
    # Electricity
    chart_name = 'prices'
    facets = ["ESRCUUS", "ESCMUUS", "ESICUUS", "ESACUUS", "ESOTUUS"]
    axis_title = 'Cents per kWh (taxes included)'
    create_chart(facets, frequency='monthly',
                 axis_title=axis_title,
                 chart_name=chart_name)

    create_chart(facets, frequency='annual',
                 axis_title=axis_title,
                 chart_name=chart_name)

    # Gas
    chart_name = 'gas'
    facets = ["RUUCUUS", "PUUCUUS", "DFONUUS"]
    axis_title = 'Dollars per Gallon (taxes included)'
    create_chart(facets, frequency='monthly',
                 axis_title=axis_title,
                 chart_name=chart_name)

    create_chart(facets, frequency='annual',
                 axis_title=axis_title,
                 chart_name=chart_name)

    # Renewables
    chart_name = 'renewables'
    facets = ["HVTCBUS", "GETCBUS", "SOTCBUS", "WYTCBUS",
              "WDTCBUS", "WSTCBUS", "BFTCBUS", "BMTCBUS"]
    axis_title = 'Energy Consumption (Trillion Btu)'
    create_chart(facets, frequency='monthly',
                 axis_title=axis_title,
                 chart_name=chart_name)

    create_chart(facets, frequency='annual',
                 axis_title=axis_title,
                 chart_name=chart_name)
