import pandas as pd

def basic_cleaning(data: list[dict]):
    keys = {"timestamp", "location_name", "country", "latitude", "longitude", "temperature", "wind_speed", "humidity"}

    for item in data:
        if item.keys() - keys:
            data.remove(item)

    if not data:
        raise ValueError('There is no data to process')
    
    df = pd.DataFrame(data)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df


def add_categiries(df):

    df['temperature_category'] = pd.cut(
        df['temperature'], 
        bins=[float('-inf'), 18, 25, float('inf')], 
        labels=['cold', 'moderate', 'hot']
        )

    df['wind_category'] = pd.cut(
        df['wind_speed'], 
        bins=[float('-inf'), 10, float('inf')], 
        labels=['calm', 'windy']
        )

    return df

