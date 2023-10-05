import os
import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
# TODO from typing import List, Optional, Tuple, Union
from plotting import (plot_monthly, plot_annual, plot_overview_monthly, plot_overview_annual,
                      plot_prices_monthly, plot_prices_annual)

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

    # Overview
    # Chart 1
    frequency = 'monthly'
    startDate = date.today() + relativedelta(years=-shortTerm)
    facets = ["CLTCBUS", "NNTCBUS", "PMTCBUS", "NUETBUS", "RETCBUS"]
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-{startDate.strftime('%m')}",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_overview_monthly(df)
    # save_chart(chart, 'overview_monthly')

    # Chart 2
    frequency = 'annual'
    startDate = date.today() + relativedelta(years=-longTerm)
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-01",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_overview_annual(df)
    # save_chart(chart, 'overview_annual')

    # Production
    facets = ["REPRBUS", "BMPRBUS", "NUETBUS",
              "NLPRBUS", "PAPRBUS", "NGPRBUS", "CLPRBUS"]
    axis_title = 'Energy Production (Trillion Btu)'
    chart_name = 'production'
    create_chart(facets, frequency='monthly',
                 axis_title=axis_title,
                 chart_name=chart_name)

    create_chart(facets, frequency='annual',
                 axis_title=axis_title,
                 chart_name=chart_name)

    # Energy Prices
    # Monthly, Electricity
    frequency = 'monthly'
    startDate = date.today() + relativedelta(years=-shortTerm)
    facets = ["ESRCUUS", "ESCMUUS", "ESICUUS", "ESACUUS", "ESOTUUS"]
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-{startDate.strftime('%m')}",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_prices_monthly(df)
    # save_chart(chart, 'prices_monthly')

    # Annual, Electricity
    frequency = 'annual'
    startDate = date.today() + relativedelta(years=-longTerm)
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-01",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_prices_annual(df)
    # save_chart(chart, 'prices_annual')

    # Monthly, Gas
    frequency = 'monthly'
    startDate = date.today() + relativedelta(years=-shortTerm)
    facets = ["RUUCUUS", "PUUCUUS", "DFONUUS"]
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-{startDate.strftime('%m')}",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_monthly(df, 'Dollars per Gallon (taxes included)')
    # save_chart(chart, 'gas_monthly')

    # Annual, Gas
    frequency = 'annual'
    startDate = date.today() + relativedelta(years=-longTerm)
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-01",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_annual(df, 'Dollars per Gallon (taxes included)')
    # save_chart(chart, 'gas_annual')

    # Renewables
    # Monthly
    frequency = 'monthly'
    startDate = date.today() + relativedelta(years=-shortTerm)
    facets = ["HVTCBUS", "GETCBUS", "SOTCBUS", "WYTCBUS",
              "WDTCBUS", "WSTCBUS", "BFTCBUS", "BMTCBUS"]
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-{startDate.strftime('%m')}",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_monthly(df, 'Energy Consumption (Trillion Btu)')
    # save_chart(chart, 'renewables_monthly')

    # Annual
    frequency = 'annual'
    startDate = date.today() + relativedelta(years=-longTerm)
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": facets,
              "start": f"{startDate.year}-01",
              "offset": 0,
              "length": 5000}

    # response = query_api(url, params)
    # df = create_df(response, frequency)
    # chart = plot_annual(df, 'Energy Consumption (Trillion Btu)')
    # save_chart(chart, 'renewables_annual')
