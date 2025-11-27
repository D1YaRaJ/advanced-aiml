from surprise import SVD, Dataset
from surprise.model_selection import train_test_split
from surprise import accuracy
import pandas as pd

data = Dataset.load_builtin('ml-100k')
df= pd.DataFrame(data.raw_ratings, columns=['user_id', 'item_id', 'rating', 'timestamp'])

print(df.head(5))
print("User–Item Rating Matrix:") 
print(df.pivot(index='user', columns='item', values='rating')) 
trainset, testset = train_test_split(data, test_size=0.2)

model = SVD()
model.fit(trainset)

predictions = model.test(testset)
rmse = accuracy.rmse(predictions, verbose=False)

print(f"\nRMSE: {round(rmse, 4)}")
print("\nFirst 10 Predictions (user, movie, true rating, predicted rating):\n")
print("user    , movie     , true rating     , predicted rating")

for pred in predictions[:5]:
    print(
        f"User {pred.uid} | Movie {pred.iid} | "
        f"Actual = {pred.r_ui} | Predicted = {round(pred.est, 3)}"
    )
