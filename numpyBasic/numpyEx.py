import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])

print(array.shape)

a = array.reshape(5,2) # 5'e 2lik bir matris oluşturduk
print("Kaça kaçlık bir array : ",a.shape)
print("Dimension : ",a.ndim)
print("Data type : ",a.dtype)
print("size : ",a.size)
print("Type : ", type(a))

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(array1.shape)


print(np.zeros((3,4))) # 3'e 4'lük matris oluşturur hepsi sıfırdır.
print(np.arange(10,50,5)) # 10'dan 50'ye kadar 50 dahil değil beşer beşer artırıp yazdırıyor.