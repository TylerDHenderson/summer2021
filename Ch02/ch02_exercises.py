import pandas as pd

df = pd.read_csv('data/parsed.csv')

df[
    (df.parsed_place == 'Japan') & (df.magType == 'mb')
].mag.quantile(0.95)


f"{df[df.parsed_place == 'Indonesia'].tsunami.value_counts(normalize=True).iloc[1,]:.2%}"

print(df)

df[df.parsed_place == 'Nevada'].describe()


df['ring_of_fire'] = df.parsed_place.str.contains(r'|'.join([
    'Alaska', 'Antarctic', 'Bolivia', 'California', 'Canada',
    'Chile', 'Costa Rica', 'Ecuador', 'Fiji', 'Guatemala',
    'Indonesia', 'Japan', 'Kermadec Islands', '^Mexico',
    'New Zealand', 'Peru', 'Philippines', 'Russia',
    'Taiwan', 'Tonga', 'Washington' 
]))


df.ring_of_fire.value_counts()

df.loc[df.ring_of_fire, 'tsunami'].sum()