import json
from typing import List
from utils import toCSV
from models import Config, KoppelConfigPaginaSubpagina
import glob

config_path = "config/scan_dir.txt"
configRows: List[Config] = []
koppelConfigRows: List[KoppelConfigPaginaSubpagina] = []

try:
    f = open(config_path)
    scan_dir = f.read()
except:
    print(f"error reading {config_path}")

for path in glob.glob(f"{scan_dir}/**/*.json", recursive=True):
    try:
        with open(path, "r") as file:
            data = json.load(file)

            config = Config(
                config_id=data.get("identifier"),
                title=data.get("figure", {}).get("title"),
                subtitle=data.get("figure", {}).get("subtitle"),
                duiding=data.get("figure", {}).get("duiding"),
                credits_id=data.get("figure", {}).get("credits_id"),
                update_datum=data.get("figure", {}).get("update_datum"),
                group=data.get("figure", {}).get("group"),
                order=data.get("figure", {}).get("order"),
            )

            configRows.append(config)

            pagina_ids = data.get("figure", {}).get("pagina_id", [])
            subpagina_ids = data.get("figure", {}).get("subpagina_id", [])

            for pagina_id, subpagina_id in zip(pagina_ids, subpagina_ids):
                koppel_config = KoppelConfigPaginaSubpagina(
                    config_id=data.get("identifier"),
                    pagina_id=pagina_id,
                    subpagina_id=subpagina_id,
                )
                koppelConfigRows.append(koppel_config)

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")

toCSV("output/config.csv", Config, configRows)
toCSV(
    "output/koppel_config_pagina_subpagina.csv",
    KoppelConfigPaginaSubpagina,
    koppelConfigRows,
)
