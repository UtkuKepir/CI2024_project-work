**Methodology**

I used only numpy library. Firstly, I defined a Node class. In this class, I implemented my tree structure to represent the data. I initialized my Node class, with value, left and right. left and right represent values(x[0], x[1]…., and 1,2,3 …) and value represents operator like sin. Left is required for single-value operators like sin(left). On the other hand, right and left are required for double value operators like ‘+’ i.e. left + right. I have evaluate() function for the representation of the mathematical formulas. I used '+', '-', '*', '/', '^', 'sin', 'cos', 'tan', 'sigmoid', 'exp', 'log', 'sqrt', 'inv' for mathematical calculations. I tried to handle inf, Nan, and very large values here properly. For example, in the below function, 1000 is used for not dealing with large fitness values for my algorithm. It is an optimization for my algorithm.    

elif self.value == 'exp':

              return np.exp(left) if np.all(left < 1000) else float('inf')
I used count_nodes() function for applying a penalty to the fitness function as a complexity. __str__ function is just for to see the tree as an string. 
My main algorithm is Genetic Programming which is an Evolutionary Algorithm variant. In addition to the Genetic Programming, I used Simulated Annealing for better exploration. I used 0.9 as a cooling rate for Simulated Annealing to train faster. Higher cooling rate means slower training. I prefer to continue with Modern Genetic Programming. I used tree structure for representation, recombination for exchange of elements, steady-state model as a population model, roulette wheel(fitness proportional) selection for parent selection, and function with the best fitness value(the lowest MSE) is used for deterministic survivor selection. Firstly, I used mutation with low probabilities, but I realized that it did not bring me any better result, so in the end I decided not to use mutation. Roulette wheel parent selection is used for decreasing selective pressure. Also, I added a penalty as a complexity(number of used node) to the MSE value while calculating fitness. For evolving, I am initializing my population with random tree. Firstly, I am taking care of using all rows of the x_train. Because I need x[0], x[1],.. at least once in my funciton as you can see below.

![image](https://github.com/user-attachments/assets/51197bf3-5b19-40b4-aba7-3ec56953c174)

 After generating these variables once, I’m generating these variables again or random constants as you can see below 

![image](https://github.com/user-attachments/assets/7392e1a9-3033-40fe-ac38-ca64d4610573)

Then, I am starting evolving generations for generation in range(self.num_gen). For each generation, I’m taking half of the population used for parent selection. Then, picking 20 parents over the population, then sorting them according to their fitness. Then, using roulette wheel, for decreasing selective pressure, I am picking 2 parents. Then parents go crossover to construct offspring. After that offspring's fitness values compete with the parents’ fitness values to select a survivor. This is a steady-state population model actually. If the offspring's fitness value is lower than the population’s best fitness value offspring is the survivor(best_individual). I am saving the best individual coming from parent or offspring to the population instead of the oldest individual for not losing the best individual with the best fitness value. Also, I’m adding 50 new individuals for each generation to increase diversity, and this method gave me better results than mutation. Finally, I wrote best_individuals with the best fitness values(lowest MSE) to the s328174.py.

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


