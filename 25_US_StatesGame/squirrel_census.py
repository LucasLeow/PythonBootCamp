import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(df.columns)

squirrel_color = list(df['Primary Fur Color'].dropna().unique())
squirrel_color_count = df.groupby(['Primary Fur Color'])['Unique Squirrel ID'].count()

frame = {
    'color': squirrel_color,
    'count': squirrel_color_count
}

new_df = pd.DataFrame(frame)
print(squirrel_color_count)