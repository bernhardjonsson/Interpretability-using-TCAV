import pickle
import tcav.utils_plot as utils_plot # utils_plot requires matplotlib

file = 'fire_engin_results_25rand.bin'
random_exp = 25

with open(file, 'rb') as f:
    results = pickle.load(f)

utils_plot.plot_results(results, num_random_exp=random_exp)
