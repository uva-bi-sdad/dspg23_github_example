import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uva-bi-sdad/national_address_database/main/data/fips_county.csv", dtype={'fips':object})
print(df)

df[df['fips'] == '01']

df['fips']

df[df['fips'] == '01000']

df['abbr'] == 'al'

df[df['fips'].str[:2] == '01']

df.to_csv('fips_country.csv', index=False)