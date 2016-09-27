import json

INPUT_FILE = 'pool.json'
OUTPUT_HTML = 'index.htm'
OUTPUT_CSS = 'style.css'

def header():
    return '<html><head></head><body>'
    
def footer():
    return '</body></html>'

def layout_data(data):
    output = '<div id="pool">'
    output = output + '<div id="pool_level" '
    if data['pool_level'] <= 0:
        output = output + 'class="pool_low">Low</div>'
    if data['pool_level'] >= 0:
        output = output + 'class="pool_normal">Normal</div>'
    return output
def load_data(source_json):
    pool_raw_data = json.load(source_json)
    pool_data = {}
    for feed in pool_raw_data['feeds']:
        # Pool sensor measured in resistance (higher number means more water)
        if feed['name'] == 'poolLevel':
            pool_data['pool_level']= feed['stream']['value']

        # Pool temperature
        elif feed['name'] == 'poolTemp':
            pool_data['pool_temp'] = feed['stream']['value']

        # Air temperature
        elif feed['name'] == 'airTemp':
            pool_data['air_temp'] = feed['stream']['value']

        # Air humidity
        elif feed['name'] == 'airRH':
            pool_data['air_humidity'] = feed['stream']['value']

        # Wifi sensor strength
        elif feed['name'] == 'poolRSSI':
            pool_data['station_signal_strength'] = feed['stream']['value']

        # Pool pump is running
        elif feed['name'] == 'poolPump':
            if feed['stream']['value'] == 1:
                pool_data['pool_pump'] = True
            elif feed['stream']['value'] == 0:
                pool_data['pool_pump'] = False
    return pool_data
    
def style():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
