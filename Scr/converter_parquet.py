import pandas as pd
import pyarrow


df_convert = pd.read_csv(r'C:\Users\igors\OneDrive\Documents\Estudo_python\Jornada_cientista_de_dados\Projeto_1\dados\MICRODADOS_ENEM_2019.csv',sep=';', encoding='latin1')
df_convert.to_parquet(r'C:\Users\igors\OneDrive\Documents\Estudo_python\Jornada_cientista_de_dados\Projeto_1\dados\MICRODADOS_ENEM_2019.parquet')