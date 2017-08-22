import numpy as np
import matplotlib.pyplot as plt


def process_and_map(numbers, low, high):
    minimum_rand, maximum_rand = min(numbers), max(numbers)
    return list(map(lambda num : int( (high - low) / (maximum_rand - minimum_rand) * (num - minimum_rand)) + low, numbers))


def plot_graph(low=1, high=100, samples=100, distribution="normal"):
    plt.title(distribution)
    if distribution == "binomial":
        eval_string = "np.random." + distribution + "(10, 0.5, samples)"
    else:
        eval_string = "np.random." + distribution + "(size = samples)"  

    x = process_and_map(eval(eval_string), low, high)
    
    plt.hist(x, 20) #plt.plot(x, [1]*samples,"x")
    plt.show()


def get_random(low=1, high=100, samples=10, distribution="normal"):
    if distribution == "binomial":
        eval_string = "np.random." + distribution + "(10, 0.5, samples)"
    else:
        eval_string = "np.random." + distribution + "(size = samples)"  

    x = process_and_map(eval(eval_string), low, high)
    
    if len(x) == 1:
        return x[0]
    
    return x

def test():
    distributions = ["normal", "binomial", "exponential", "poisson", "laplace", "logistic", "uniform", "rayleigh"]
    #list(map(lambda dist:plot_graph(1, 100, 1000, dist), distributions))
    
    l = 1
    h = 100
    for d in distributions:
        print(d)
        print('Winning Door Choice: ', end='')
        print(get_random(l, h, samples=10, distribution=d))
        print('Contestent Door Choice: ', end='')
        print(get_random(l, h, samples=10, distribution=d))
        print()


if __name__ == '__main__':
    test()