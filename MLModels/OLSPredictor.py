import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])  # Hours studied (independent variable)
y = np.array([2, 4, 5, 4, 5])            # Exam score (dependent variable)

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients
intercept = model.intercept_
slope = model.coef_[0]

print(f"Intercept (β0): {intercept}")
print(f"Slope (β1): {slope}")

# Predict scores
y_pred = model.predict(X)

print("\nPredicted values:", y_pred)

# Plot data and regression line
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, y_pred, color="red", linewidth=2, label="Regression line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.show()