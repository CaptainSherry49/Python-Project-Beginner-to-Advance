import pandas as pd  # Importing Pandas For Reading CSV File
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle


def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))  # The given data will be shuffled (last value will be excluded)
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__ == '__main__':
    df = pd.read_csv('data.csv')  # Reading CSV
    train, test = data_split(df, 0.2)

    X_train = train[['fever', 'bodyPain', 'age', 'runnyNose',
                     'difficultyBreath']].to_numpy()  # Converting train data to numpy array

    X_test = test[['fever', 'bodyPain', 'age', 'runnyNose',
                  'difficultyBreath']].to_numpy()  # Converting test data to numpy array

    Y_train = train[['infectionProbability']].to_numpy().reshape(2060, )

    Y_test = test[['infectionProbability']].to_numpy().reshape(515, )

    clf = LogisticRegression()  # Initializing
    clf.fit(X_train, Y_train)

    # open a file where you want to store tha data
    file = open('model.pkl', 'wb')

    # dump info to the file
    pickle.dump(clf, file)

    # Close the file
    file.close()
