import matplotlib.pyplot as plt
from IT19tb_WIN7_S1_Aufg2 import IT19tb_WIN7_S1_Aufg2

input_xmin = -10
input_xmax = 10
input_a = [1,2,3]

x_values, p_values, dp_values, pint_values = IT19tb_WIN7_S1_Aufg2(input_a, input_xmin, input_xmax)

plt.plot(x_values,p_values)
plt.plot(x_values,dp_values)
plt.plot(x_values,pint_values)
plt.grid()
plt.show()