import population
import crossbreed
import numpy as np

x = population.random_population(8)

# for row in x:
#     print(row, items.adaptation_function(row))


# y = items.tournament_selection(x, 8)

# print(y)

a = np.array(['1', '2', '3', '4', '5', '6', '7'])
b = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(crossbreed.do_crossbreed_single_point(np.array([a, b]), 4))
