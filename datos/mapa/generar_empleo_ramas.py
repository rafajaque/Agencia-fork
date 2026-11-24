"""Ocupados por región y rama de actividad, desde el microdato de la ENE (INE).

Entrada: datos/crudos/ine/ene-2026-08-jas.csv (microdato Jul-Sep 2026, fuera del repositorio).
Solo se suman factores de expansión: ninguna fila de personas sale del script.
Un ocupado es quien tiene categoria_ocupacion distinta de 0 o vacía.

Salida: datos/mapa/ene_ramas_region.json, y para cada área SIES, la proporción de
ocupados de la región que trabaja en las ramas asociadas (elaboración propia).

Uso: python datos/mapa/generar_empleo_ramas.py
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ENTRADA = RAIZ / "datos" / "crudos" / "ine" / "ene-2026-08-jas.csv"
SALIDA = RAIZ / "datos" / "mapa" / "ene_ramas_region.json"

# Secciones CAE rev. 4 (códigos del microdato, r_p_rev4cl_caenes), elaboración propia.
RAMAS = {
    "1": "Agricultura, ganadería, silvicultura y pesca",
    "2": "Explotación de minas y canteras",
    "3": "Industrias manufactureras",
    "4": "Electricidad, gas y agua (energía)",
    "5": "Suministro de agua y saneamiento",
    "6": "Construcción",
    "7": "Comercio",
    "8": "Transporte y almacenamiento",
    "9": "Alojamiento y comidas",
    "10": "Información y comunicaciones",
    "11": "Actividades financieras y de seguros",
    "12": "Actividades inmobiliarias",
    "13": "Actividades profesionales, científicas y técnicas",
    "14": "Actividades administrativas y de apoyo",
    "15": "Administración pública y defensa",
    "16": "Enseñanza",
    "17": "Salud humana y servicios sociales",
    "18": "Artes, entretenimiento y recreación",
    "19": "Otros servicios",
    "20": "Hogares como empleadores",
    "21": "Organizaciones extraterritoriales",
}

# Áreas SIES -> ramas asociadas. Es un supuesto de trabajo: revisar con el equipo.
AREA_RAMAS = {
    "Salud": ["17"],
    "Educación": ["16"],
    "Derecho": ["15", "13"],
    "Administración y Comercio": ["7", "11", "14"],
    "Tecnología": ["10", "3", "4", "6"],
    "Ciencias Sociales": ["13", "15", "19"],
    "Ciencias Básicas": ["13", "2"],
    "Agropecuaria": ["1"],
    "Humanidades": ["16", "18"],
    "Arte y Arquitectura": ["18", "13", "6"],
}

def main():
    ocupados = defaultdict(float)  # (región, rama) -> personas expandidas
    total = 0.0
    with open(ENTRADA, encoding="latin-1", newline="") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            if fila["categoria_ocupacion"].strip() in ("", "0"):
                continue
            w = float(fila["fact_cal"].replace(",", ".") or 0)
            region = fila["region"].zfill(2)
            rama = fila["r_p_rev4cl_caenes"].strip()
            total += w
            if rama in RAMAS:
                ocupados[(region, rama)] += w
            else:
                ocupados[(region, "999")] += w

    regiones = sorted({r for r, _ in ocupados})
    por_region = {}
    for r in regiones:
        tot_r = sum(v for (rr, _), v in ocupados.items() if rr == r)
        por_region[r] = {
            "ocupados": round(tot_r),
            "ramas": {k: round(ocupados.get((r, k), 0)) for k in RAMAS},
        }

    areas = {}
    for area, ramas in AREA_RAMAS.items():
        areas[area] = {}
        for r in regiones:
            tot_r = por_region[r]["ocupados"]
            en_area = sum(ocupados.get((r, k), 0) for k in ramas)
            areas[area][r] = round(100 * en_area / tot_r, 1) if tot_r else None

    salida = {
        "fuente": "INE, Encuesta Nacional de Empleo, microdato trimestre móvil Jul-Sep 2026 (mes central agosto). Cálculo propio con factor fact_cal.",
        "nota": "Ocupados por región y rama de actividad (CAE rev. 4). No es empleo por grupo ocupacional: la rama es una aproximación al tipo de trabajo.",
        "ocupados_total": round(total),
        "ramas": RAMAS,
        "areas_ramas": AREA_RAMAS,
        "regiones": por_region,
        "porcentaje_ocupados_en_area_por_region": areas,
    }
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"total ocupados {round(total)}; regiones {len(regiones)}; salida {SALIDA}")

if __name__ == "__main__":
    main()
