from dataclasses import asdict, fields
from typing import List, Type
import csv


def toCSV(filename: str, type: Type, list: List):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [f.name for f in fields(type)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows([asdict(c) for c in list])
        print(f"exported list of {type.__name__} to {filename}")
