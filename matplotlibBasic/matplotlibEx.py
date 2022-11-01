import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dictionary = {"İsim": ["Burhan","Buse","Ayşenur","Yenes","Raşo"],
              "Yaş":[21,21,10,31,69],
              "Maaş":[250,100,0,50,200]}


dataFrame = pd.DataFrame(dictionary)
print(dataFrame)
print("\n")


# plot 1
plt.subplot(1,2,1)
plt.plot(dataFrame.Maaş,'o:b',label = "Çalışan-Maaş")
plt.grid(color = 'red',linestyle = "--")
plt.xlabel("çalışan")
plt.ylabel("maaş")

# plot 2
plt.subplot(1,2,2)
plt.plot(dataFrame.İsim,'o:y')
plt.grid(color = 'red',linestyle = "--")

plt.legend()
plt.show()

