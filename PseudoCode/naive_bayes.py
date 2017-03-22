# Import Libraries
from sklearn.naive_bayes import GaussianNB

# Load Train and Test datasets
# This is where X (your predictor), Y (your target) and x_test comes from...

# Variables
x_train = input_training_values
y_train = target_training_values

x_test = input_testing_values

# Create Model
model = GaussianNB()

# Train Model
model.fit(x_train, y_train)

# Mean accuracy on the given test data and labels
model.score(x_train, y_train)

# Predict Output
predicted = model.predict(x_test)
