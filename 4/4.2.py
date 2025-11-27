from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

d = load_digits()
X = d.data
y = d.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
for i in range(10):
    if y_pred[i] == y_test[i]:
           print(f"Correct:   Predicted = {y_pred[i]}, Actual = {y_test[i]}")
    else:
          print(f"Wrong:     Predicted = {y_pred[i]}, Actual = {y_test[i]}")