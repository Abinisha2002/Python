'''Matplot'''
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.array([0,3,5])
# ypoints=np.array([0,150,45])
# plt.plot(xpoints,ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.array([1,2,6,8])
# ypoints=np.array([3,8,1,10])
# plt.plot(xpoints,ypoints)
# plt.title("title")
# plt.xlabel("number")
# plt.ylabel("mark")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,1,10,5,7])
# plt.plot(ypoints)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker="*")
# plt.show()





# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,'*:m')
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o',ms=50)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker="o",mec='r')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,10,1])
# plt.plot(ypoints,marker="o",mfc="r")
# plt.show()


# import matplotlib. pyplot as plt
# import numpy as np
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,color="r")
# plt.show()
# plt.plot(ypoints,c="hotpink")
# plt.show()
# plt.plot(ypoints,linewidth="20.5")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# y1=np.array([3,8,1,10])
# y2=np.array([6,2,7,11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x1=np.array([0,1,2,3])
# y1=np.array([3,4,1,10])
# x2=np.array([0,1,2,3])
# y2=np.array([6,2,7,11])
# plt.plot(x1,y1,x2,y2)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([80,85,90,95,100,105,110,115,120,125])
# y=np.array([240,250,260,270,280,290,300,310,320,330])
# plt.plot(x,y)
# plt.xlabel("Average pulse")
# plt.ylabel("Calorie burnage")
# plt.show()





# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([80,85,90,95,100,105,110,115,120,125])
# y=np.array([240,250,260,270,280,290,300,310,320,330])
# font1={"family":"serif","color":"blue","size":"20"}
# font2={"family":"serif","color":"darkred","size":15}
# plt.title("Sports watch Data",fontdict=font1)
# plt.xlabel("Average pulse",fontdict=font2)
# plt.ylabel("Calorie Burnage",fontdict=font2)
# plt.plot(x,y)
# plt.show()


import matplotlib .pyplot as plt
import numpy as np
from scipy.stats import linregress
np.random.seed(42)
x=np.random.rand(50)*10
y=2* x+1+np.random.random(50)*2 
slope,intercept,r_value,p_value,std_err=linregress(x,y)
y_pred=slope*x+intercept
plt.scatter(x,y,label="Data")
plt.plot(x,y_pred,color="red",label=f'Regression Line:y={slope:.2f}x+{intercept:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()