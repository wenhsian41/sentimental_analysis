import os
import json
import pandas as pd
root = os.getcwd()+ '//'

def append_row(df, item):
    new_row = {'reviewText': item['reviewText'], 'overall': item['overall'], }
    df = df.append(new_row, ignore_index=True)
    return df

def transform_json():
    if os.path.exists(root + 'reviews_kindle.xlsx') == False:
        columns = ['reviewText', 'overall']
        df = pd.DataFrame(columns=columns)
        file_name = 'reviews_kindle.json'
        with open(file_name) as f:
            for line in f:
                item = json.loads(line)
                df = append_row(df, item)
        df.to_excel('reviews_kindle.xlsx', index=False)
    else:
        df = pd.read_excel('reviews_kindle.xlsx').head(5)

if __name__ == '__main__':
    # use dataframe to hold the data
    transform_json()
