import numpy as np  
import matplotlib.pyplot as plt
#产生测试数据
x = weight
y = profit
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('数据散点图')
plt.xlabel('weight')
plt.ylabel('profit')
ax1.scatter(x,y,c = 'r',marker = 'o')
plt.legend('x1')  
#显示所画的图  
plt.show() 
