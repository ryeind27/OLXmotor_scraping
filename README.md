# Scraping Motor bekas di OLX menggunakan Scrapy

## Installation

Membuat virtual environment:

```bash
python3 -m venv .env
```
atau
```bash
python -m venv .env
```

Aktifkan virtual environment:

```bash
source .env/bin/activate
```
atau masuk ke directory scripts dan masukan activate pada command prompt

```bash
cd .env/scripts
```

Install Scrapy:

```bash
pip install scrapy
```

Membuat Scrapy project:

```bash
scrapy startproject olxmotor
```

## Creating the spider

```bash
cd olxmotor
```
```bash
scrapy genspider olxmotor_scraping https://www.olx.co.id/motor-bekas_c200
```

## Running spider crawling

```bash
scrapy crawl olxmotor_scraping
```

## Result

Hasil output dicetak dalam format .JSON dapat di lihat [disini](olxmotor/spiders/output.json)
