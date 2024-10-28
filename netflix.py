import json 
import pandas as pd 

#Loading a TSV file into a DataFrame
file = 'netflix_titles.tsv'
df = pd.read_csv(file, sep='\t', encoding='utf-8')

#Select only certain columns and rename them
selected_columns = ['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']
filtered_df = df[selected_columns]

filtered_df = df[selected_columns].rename(columns={
    'PRIMARYTITLE': 'title',
    'DIRECTOR': 'directors',
    'CAST': 'cast',
    'GENRES': 'genres',
    'STARTYEAR': 'decade'
})

#Convert to lists for each column
filtered_df['directors'] = filtered_df['directors'].apply(lambda x: x.split(", ") if pd.notnull(x) else [])
filtered_df['cast'] = filtered_df['cast'].apply(lambda x: x.split(", ") if pd.notnull(x) else [])
filtered_df['genres'] = filtered_df['genres'].apply(lambda x: x.split(", ") if pd.notnull(x) else [])
filtered_df['decade'] = (df['STARTYEAR'] // 10) * 10



#Converting a DataFrame to a list of dictionaries
data_dict = filtered_df.to_dict(orient='records')


#Save to a JSON file
with open('hw02_output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

