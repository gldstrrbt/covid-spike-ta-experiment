# Historical experimental archive; preserved with minimal cleanup.
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.offline as py
# py.init_notebook_mode()
# %matplotlib inline


df = pd.read_csv("^GSPC.csv", index_col="Date", parse_dates=True)
df.head()

df = df.reset_index()
df.head()

df=df.rename(columns={'Date':'ds', 'Close':'y'})
df.head()

df.set_index('ds').y.plot()

df['y'] = np.log(df['y'])
df.tail()
df.set_index('ds').y.plot().get_figure()

model = Prophet()
model.fit(df)

# future = model.make_future_dataframe(periods=24, freq = 'm')
future = model.make_future_dataframe(periods=780)
future.tail()

forecast = model.predict(future)
forecast.tail()

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = model.plot(forecast)

fig1 = model.plot_components(forecast)

print(forecast)
plt.show()

# print(df.head(2))
# print(df.info())
# print(df.describe(include='O'))