import numpy as np
import matplotlib.pyplot as plt

def process_and_map(x, n):
	minimum_rand, maximum_rand = min(x), max(x)
	return list(map(lambda num:int( (n - 1) / (maximum_rand - minimum_rand) * (num - minimum_rand)) + 1, x))

def generate_random(n = 3, number_of_samples, distribution = "normal"):
    plt.title(distribution)
	
    if distribution == "binomial":
        eval_string = "np.random." + distribution + "(10, 0.5, number_of_samples)"
    else:
        eval_string = "np.random." + distribution + "(size = number_of_samples)"  
    
	x = process_and_map(eval(eval_string), n)
    
	plt.hist(x,20) #plt.plot(x, [1]*number_of_samples,"x")
    plt.show()


if __name__ == '__main__':
	list_of_distributions = ["normal","binomial", "exponential", "poisson", "laplace", "logistic", "uniform", "rayleigh"]
	list(map(lambda dist:generate_random(100, 1000, dist), list_of_distributions))

