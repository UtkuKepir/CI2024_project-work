**Methodology**

Steady state model is used for population management model instead of generational model
**Results**


| **Data**      | **Fitness**      | **Expression**                                                     | **Expression using Numpy**                                             | **MSE using symreg.ipynb**|
|---------------|------------------|--------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------|
| problem_1.npz | 0.1              | sin(x[0])                                                          | np.sin(x[0])                                                           | 7.12594e-32               |
| problem_2.npz | 29575308429996.04| inv(sigmoid((x[0] + (x[1] + x[2]))))                               | 1 + np.exp(-(x[0] + x[1] + x[2]))                                      | 2.9617e+15                |
| problem_3.npz | 1323.05          | cos(tan(x[0])) + (inv(sigmoid(x[1])) + x[2])                       | np.cos(np.tan(x[0])) + (1 + np.exp(-x[1])) + x[2]                      | 132285                    |
| problem_4.npz | 21.58            | exp(cos((x[0] * x[1])))                                            | np.exp(np.cos(x[0] * x[1]))                                            | 2138.15                   |
| problem_5.npz | 0.15             | (cos(x[0]) / (x[1] / 0.02871653301747079))                         | np.cos(x[0]) * 0.02871653301747079 / x[1]                              | 30.98                     |
| problem_6.npz | 5.86             | cos(exp(sigmoid(x[0]))) + x[1]                                     | np.cos(np.exp(1 / (1 + np.exp(-x[0])))) + x[1]                         | 561.83                    |
| problem_7.npz | 626.07           | exp(x[0] * x[1])                                                   | np.exp(x[0] * x[1])                                                    | 62592.7                   |
| problem_8.npz | 21321683.32      | ((exp(x[5]) * (exp(x[0]) + x[3])) - (tan(inv(x[1])) + x[2])) + x[4]| ((np.exp(x[5]) * (np.exp(x[0]) + x[3])) - (np.tan(1 / x[1]) + x[2])) + x[4]| 2.13217e+09           |


