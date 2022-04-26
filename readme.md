
# Autotrader Search Bot

This project is written in python, and uses the `bs4` and `requests` library to scrape
the autotrader website using specifications defined in the `config.ini` file.  


## Setup

Install autotrader-bot with `pip`

```bash
  cd autotrader-bot
  pip3 install -r requirements.txt
  python3 app.py
```
    
## Config Options

| Name | Example     | Description                |
| :-------- | :------- | :------------------------- |
| postcode | PH36 4LB | Your postcode |
| radius | national, 1-200 miles | Radius of search |
| make | Volkwagen | Car make |
| model | Polo | Car model |
| trim | GTI | Model variant |
| min-price | 15000 | Minimum price |
| max-price | 30000 | Maximum price |
| min-year | 2014 | Minimum year |
| max-year | 2019 | Maximum year |
| max-mileage | 100-200000 | Maximum miles |
| transmission | automatic, manual | Transmition |
| fuel-type | petrol, diesel, petrol hybrid | Fuel type |
| minimum-engine-size | 1.4 | Minimum engine size |
| maximum-engine-size | 2.0 | Maximum engine size |
| min-engine-power | 59 | Minimum engine power (BHP) |
| max-engine-power | 180 | Maximum engine power (BHP) |
| seller-type | private adverts, trade adverts | Type of seller |
| colour | white, black, blue | Vehicle colour |
| exclude-writeoff-categories | on | Ignore CAT Vehicles |

