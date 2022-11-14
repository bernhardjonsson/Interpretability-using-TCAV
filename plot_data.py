import pickle
import tcav.utils_plot as utils_plot # utils_plot requires matplotlib

with open('results.bin', 'rb') as f:
    results = pickle.load(f)

utils_plot.plot_results(results, num_random_exp=3)
