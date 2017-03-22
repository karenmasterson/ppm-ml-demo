# Import Libraries
from sklearn import linear_model

# Load Train and Test datasets
# This is where x_train, y_train and x_test comes from...

# Variables
x_train = input_training_values
y_train = target_training_values

x_test = input_testing_values
y_test = derp

# Create Model
model = linear_model.LinearRegression()

# Train Model
model.fit(x_train, y_train)
model.score(x_test, y_test)

# Linear Coeff. estimates of shape (n_targets, n_features) and Intercept (independent term in linear model)
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

# Predict Output

predicted = model.predict(x_test)
