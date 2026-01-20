import pandas as pd

def basic_cleaning(data: list[dict]):
    for item in data:
        if 'timestemp' not in item:
            data.remove(item)        
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df



def add_categiries(df):
    
    df['category_temperature'] = pd.cut(df[''], bins=[float('-inf'), 18, 25, float('inf')], labels=['cold', 'moderate', 'hot'])

    df['status_wind'] = pd.cut(df['wind'], bins=[float('-inf'), 10, float('inf')], labels=['calm', 'windy'])

    return df

