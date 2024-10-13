# Step 1: Installation and Setup
# No code needed - Install Python from https://www.python.org/ and use pip to install libraries

# Step 2: Variables and Data Types
age = 25
height = 5.8
name = "John"
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3)
my_dict = {"key": "value"}

# Step 3: Basic Operations
result = 10 + 5
comparison = age > 18

# Step 4: Control Structures
if age >= 21:
    print("You can have a drink!")
elif 18 <= age < 21:
    print("You're almost there!")
else:
    print("You're too young!")

for item in my_list:
    print(item)

# Step 5: Functions
def greet_person(name):
    return f"Hello, {name}!"

greeting = greet_person("Alice")
print(greeting)

# Step 6: Lists and Dictionaries
my_list.append(5)
print(my_list)

my_dict["new_key"] = "new_value"
print(my_dict)

# Step 7: NumPy and Arrays
import numpy as np

array = np.array([1, 2, 3, 4])
print(array)

# Step 8: Pandas and DataFrames
import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 22]}
df = pd.DataFrame(data)
print(df)

# Step 9: Visualizing Data
import matplotlib.pyplot as plt
import seaborn as sns

# (Assuming you have data loaded into a DataFrame df)
sns.scatterplot(x='Name', y='Age', data=df)
plt.show()

# Step 10: Machine Learning Libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
