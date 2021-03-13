import requests
import pickle

urls = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(urls)
text = response.text
data = text.splitlines()
data_for_pickling = [[i] for i in data if len(i) != 0]


# Pickling
with open('pickling iris.pkl', 'wb') as f:
    pickle.dump(data_for_pickling, f)


# Reading
with open('pickling iris.pkl', 'rb') as f:
    for_read = pickle.load(f)
print(for_read)
