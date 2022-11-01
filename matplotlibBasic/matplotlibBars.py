import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Fenerbahçe","Galatasaray","Beşiktaş","Sivasspor","Trabzonspor"])
y = np.array([28,23,19,0,6])

plt.bar(x,y,color = "magenta")
plt.show()
