from cv2 import accumulateProduct
import numpy as np
import pandas as pd
import plotly_express as px
import plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt

plotly.offline.init_notebook_mode(connected=True)

# iris=px.data.iris()
# iris_plot=px.scatter(iris, x='sepal_width', y='sepal_length', color='species', marginal_y='histogram', marginal_x='box',
#                      trendline='ols')
# plotly.offline.plot(iris_plot)

# c= {['red','blue'],['Rex','LuLu']}
# b=pd.DataFrame(data=c,index=[2,3],columns=['a','b'])
# print(b)

# wt=np.arange(15).reshape(3,5)
# print(wt)
# df = px.data.gapminder().query("year == 2007")
# fig = px.line_geo(df, locations="iso_alpha",
#                   color="continent", # "continent" is one of the columns of gapminder
#                   projection="orthographic")
# # fig.write_image('./images/px/19-map-2.png')
# fig.show()
# df = pd.DataFrame({'A': [1, 1, 2, 2],
#                     'B': [1, 2, 3, 4],
#                    'C': np.random.randn(4)})
# print(df.groupby('A').agg('min'))
# df = pd.DataFrame({
#     'Country': ['China', 'US', 'Japan', 'EU', 'UK/Australia', 'UK/Netherland'],
#     'Number': [100, 150, 120, 90, 30, 2],
#     'Value': [1, 2, 3, 4, 5, 6],
#     'label':
#     list('abcdef')
# })
# df.drop('Country', axis=1).join(df['Country'].str.split(
#     '/', expand=True).stack().reset_index(level=1, drop=True).rename('Country'))
# print(df)
labels='Frogs','Hogs','Dogs','Cats'
sizes=[14,15,15,55]
explode=(0,0.1,0,0)
fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%.2f%%',shadow=True, startangle=90)
plt.show()

