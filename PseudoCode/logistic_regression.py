# Import Libraries
from sklearn.linear_model import LogisticRegression

# Load Train and Test datasets
# This is where X (your predictor), Y (your target) and x_test comes from...

# Variables
x_train = input_training_values
y_train = target_training_values

x_test = input_testing_values

# Create Model
model = LogisticRegression()

# Train Model
model.fit(x_train, y_train)

# Mean accuracy on the given test data and labels
model.score(x_test, y_test)

# Linear Coeff. of features in decision function and Intercept added to decision function
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

# Predict Output
predicted = model.predict(x_test)
