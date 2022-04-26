from configparser import ConfigParser
import configparser
import requests, os

def main():
    url = 'https://www.autotrader.co.uk/car-search?'
    
    config = ConfigParser()
    config.read('config.ini')
    
    try:
        postcode = config.get('DETAILS', 'postcode')
        make = config.get('DETAILS', 'make')
        model = config.get('DETAILS', 'model')
        radius = config.get('DETAILS', 'radius')
        if radius == 'national' : radius = '1500'
    except(configparser.NoOptionError):
        print('[!] Missing Required Fields\n\n- Postcode\n- Make\n- Model\n- Radius')
        return
    
    url = url + f'postcode={postcode}&radius={radius}&make={make}&model={model}&'
    
    if config.has_option('DETAILS', 'trim') : url += f"trim={config.get('DETAILS', 'aggregatedTrim')}&"
    if config.has_option('DETAILS', 'min-price') : url += f"price-from={config.get('DETAILS', 'min-price')}&"
    if config.has_option('DETAILS', 'max-price') : url += f"price-to={config.get('DETAILS', 'max-price')}&"
    if config.has_option('DETAILS', 'min-year') : url += f"year-from={config.get('DETAILS', 'min-year')}&"
    if config.has_option('DETAILS', 'max-year') : url += f"year-to={config.get('DETAILS', 'max-year')}&"
    if config.has_option('DETAILS', 'max-milaege') : url += f"max-mileage={config.get('DETAILS', 'max-mileage')}&"
    if config.has_option('DETAILS', 'transmission') : url += "transmission={config.get('DETAILS', 'transmission')}&"
    if config.has_option('DETAILS', 'fuel-type') : url += f"fuel-type={config.get('DETAILS', 'fuel-type')}&"
    if config.has_option('DETAILS', 'minimum-engine-size') : url += f"minimum-badge-engine-size={config.get('DETAILS', 'minimum-engine-size')}&"
    if config.has_option('DETAILS', 'maximum-engine-size') : url += f"maximum-badge-engine-size={config.get('DETAILS', 'maximum-engine-size')}&"
    if config.has_option('DETAILS', 'min-engine-power') : url += f"min-engine-power={config.get('DETAILS', 'min-engine-power')}&"
    if config.has_option('DETAILS', 'max-engine-power') : url += f"max-engine-power={config.get('DETAILS', 'max-engine-power')}&"
    if config.has_option('DETAILS', 'seller-type') : url += f"seller-type={config.get('DETAILS', 'seller-type')}&"
    if config.has_option('DETAILS', 'colour') : url += f"colour={config.get('DETAILS', 'colour')}&"
    if config.has_option('DETAILS', 'exclude-writeoff-categories') : url+= f"exclude-writeoff-categories={config.get('DETAILS', 'exclude-writeoff-categories')}&"

    if url.endswith('&') : url = url[:-1]
    
    print(url)
    

if os.path.isfile(f'{os.getcwd()}/config.ini') != True:
    print('[i] Please follow the readme.')
else:
    main()