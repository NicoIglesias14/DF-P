path='/workspaces/DF-P/notebooks/10_Dataviz/data/gapminder.csv'

import pandas

df=pandas.read_csv(path)
print(df)

import streamlit

streamlit.write(df) 

paises=df['country'].unique()
pais=streamlit.selectbox(label='Seleccione país',options=paises)
mask=df['country']==pais
s=df[mask]

import plotly.express
fig=plotly.express.line(data_frame=s,x='year',y='lifeExp')

streamlit.plotly_chart(fig)