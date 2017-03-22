# Import Libraries
from sklearn import tree

# Load Train and Test datasets
# This is where X (your predictor), Y (your target) and x_test comes from...

# Variables
x_train = input_training_values
y_train = target_training_values

x_test = input_testing_values

# Create Model (gini or entropy, gini is default)
model = tree.DecisionTreeClassifier(criterion='gini')

# model = tree.DecisionTreeRegressor() for regression also an option

# Train Model
model.fit(x_train, y_train)

# Mean accuracy on the given test data and labels
model.score(x_train, y_train)

# Predict Output
predicted = model.predict(x_test)
