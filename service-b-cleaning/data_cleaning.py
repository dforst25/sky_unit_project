import pandas as pd

def basic_cleaning(data: list[dict]):
    keys = {"timestamp", "location_name", "country", "latitude", "longitude", "temperature", "wind_speed", "humidity"}

    for item in data:
        if item.keys() - keys:
            data.remove(item)


    if not data:
        raise ValueError('There is no data to process')


    df = pd.DataFrame(data)

    try: df['timestamp'] = pd.to_datetime(df['timestamp'])
    except Exception as e: raise ValueError({'Error Unprocessable Data': str(e)})
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df


def add_categiries(df):

    df['category_temperature'] = pd.cut(
        df['temperature'], 
        bins=[float('-inf'), 18, 25, float('inf')], 
        labels=['cold', 'moderate', 'hot']
        )

    df['status_wind'] = pd.cut(
        df['wind_speed'], 
        bins=[float('-inf'), 10, float('inf')], 
        labels=['calm', 'windy']
        )

    return df

