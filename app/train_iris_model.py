from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target
species_map = {i: name for i, name in enumerate(iris.target_names)}

# 2. Split data into train and test (optional but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 4. Save the model to disk
joblib.dump(clf, 'model.pkl')

# 5. Save the species map
joblib.dump(species_map, 'species_map.pkl')

print("Model and species map saved!")
