<div align="center">
  <a href="https://github.com/dennisfrijlink-rivm/regiobeeld-json-naar-csv">
    <img style="border-radius: 100%;" src="public/logo.jpeg" alt="Logo" width="120" height="120">
  </a>
  <h1 align="center">Regiobeeld configs to .csv</h1>
</div>

## Over het project

Simpel python script om de regiobeeld `.json` config bestanden te exporteren naar `.csv` in het formaat van de nieuwe database.

## Hoe te gebruiken

### configuratie

In de `/config` directory staat het `scan_dir.example.txt` bestand met daarin een voorbeeld pad naar de `.json` configuraties. Hernoem dit bestand naar `scan_dir.txt` en vervang het pad naar de juiste directory **(let op dit moet een absoluut pad zijn)**:

```txt
C:\Users\superheld\Documents\de-regiobeeld-json-configs
```

### script starten

Run het script via de windows terminal:

```sh
$ python src/main.py
exported list of Config to output/config.csv
exported list of KoppelConfigPaginaSubpagina to output/koppel_config_pagina_subpagina.csv
```

Nu heeft het script de `.json` de configuraties in het opgegeven pad geconverteerd naar de `config.csv` en de `koppel_config_pagina_subpagina.csv` en geplaatst in de `output/` folder
