import matplotlib
import numpy
import pandas
import sklearn
import scipy
import torch
import matplotlib.pyplot as plt

print("matplotlib   ", matplotlib.__version__)
print("numpy        ", numpy.__version__)
print("pandas       ", pandas.__version__)
print("scikit-learn ", sklearn.__version__)
print("scipy        ", scipy.__version__)
print("torch        ", torch.__version__)

plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig("test_figure.png")