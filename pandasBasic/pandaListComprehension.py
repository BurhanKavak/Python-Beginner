import pandas as pd

dictionary = {"İsim":["Burhan","Buse","Ayşenur","Yenes","Raşo"],
              "Yaş":[21,21,10,31,69],
              "Maaş":[250,100,0,50,200]}

dataFrame = pd.DataFrame(dictionary)
print(dataFrame)
print("\n")

average = dataFrame.Maaş.mean()
print("Maaş ortalaması : ",average)

dataFrame["Maaş_Seviyesi"] = ["yüksek" if average < each else "düşük" for each in dataFrame.Maaş]
print(dataFrame)