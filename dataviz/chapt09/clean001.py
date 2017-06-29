import pandas as pd

df = pd.read_json(open(nobel_winners_dirty.json))

def mongo_to_dataframe(db_name, collection, query={}, host='localhost', port=27017, username=none, password=none, no_id=true):
    db = get_mongo_database(db_name, host, port, username, password)
    cursor = db[collection].find(query)
    df = pd.dataframe(list(cursor))

    if no_id:
        del df['_id']

    return df

df = mongo_to_dataframe('nobel_prize', 'winners')
print(df)
