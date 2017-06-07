from sklearn.datasets import make_moons

db = dataset.connect('sqlite:///make_moons.db')

make_moons()
