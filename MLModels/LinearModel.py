import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
Y = lifesat[["Life satisfaction"]].values

# Visualize the data
lifesat.plot(kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
# model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)

# Train the model
model.fit(X=X, y=Y)

# Make a prediction for Cyprus
X_new = [[37_655.2]]
print(model.predict(X=X_new))