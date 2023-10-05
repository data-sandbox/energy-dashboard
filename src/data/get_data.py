import os
import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
# TODO from typing import List, Optional, Tuple, Union
from plotting import plot_overview_monthly, plot_overview_annual

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


if __name__ == "__main__":

    token = os.getenv("API_KEY")
    url = 'https://api.eia.gov/v2/total-energy/data/'

    # Chart 1
    frequency = 'monthly'
    startDate = date.today() + relativedelta(years=-3)
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": ["CLTCBUS", "NNTCBUS", "PMTCBUS", "NUETBUS", "RETCBUS"],
              "start": f"{startDate.year}-{startDate.strftime('%m')}",
              "offset": 0,
              "length": 5000}

    response = query_api(url, params)
    df = create_df(response, frequency)
    chart = plot_overview_monthly(df)
    save_chart(chart, 'overview_monthly')

    # Chart 2
    frequency = 'annual'
    startDate = date.today() + relativedelta(years=-20)
    params = {'api_key': token,
              'frequency': frequency,
              "data[0]": ["value"],
              "facets[msn][]": ["CLTCBUS", "NNTCBUS", "PMTCBUS", "NUETBUS", "RETCBUS"],
              "start": f"{startDate.year}-01",
              "offset": 0,
              "length": 5000}

    response = query_api(url, params)
    df = create_df(response, frequency)
    chart = plot_overview_annual(df)
    save_chart(chart, 'overview_annual')
