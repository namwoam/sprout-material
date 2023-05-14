from fastapi import FastAPI
import pandas as pd

import os

app = FastAPI()

population_df = pd.read_csv(os.path.join(
    os.path.dirname(__file__), "country_population.csv"))

population_df = population_df.fillna("")

country_names: list[str] = population_df["Country Name"].to_list()


@app.get("/year-population/{year}")
async def get_year_population(year: int):
    year_population: list[float] = population_df[year].to_list()
    output: dict[str, str] = {}
    for country_index, country_name in enumerate(country_names):
        output[country_name] = year_population[country_index]
    return output
