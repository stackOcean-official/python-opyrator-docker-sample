from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

def train():
    df = pd.read_csv('data/beach_chairs.csv')
    print(df.head)
    dependent_var = "beach_chairs"

    df['Date'] = pd.to_numeric(pd.to_datetime(df['Date'], format='%Y-%m-%d'))

    X = df.drop(dependent_var, axis="columns")
    y = df[dependent_var]

    linear_model = LinearRegression()
    linear_model.fit(X, y)

    pickle.dump(linear_model, open(f"./model/model.sav", 'wb'))


if(__name__ == "__main__"):
    train()
