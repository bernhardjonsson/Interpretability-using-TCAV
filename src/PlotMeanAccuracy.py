import numpy as np

# Make a dictionary with the mean accuracies for each bottleneck
# results for fire engine is called results_FE
# results for suit is called results_suit
accuracy_dict_fire_engine = {bottleneck: np.mean([test["cav_accuracies"]["overall"] for test in results_FE if test["bottleneck"] == bottleneck]) for bottleneck in bottlenecks}
accuracy_dict_suit = {bottleneck: np.mean([test["cav_accuracies"]["overall"] for test in results_suit if test["bottleneck"] == bottleneck]) for bottleneck in bottlenecks}


# Plot mean accuracies for each bottleneck
import matplotlib.pyplot as plt
fontsize = 20
fig, axs = plt.subplots()
fig.set_size_inches(10,7)
plt.plot(accuracy_dict_fire_engine.keys(), accuracy_dict_fire_engine.values(),color='red', marker='o')
plt.plot(accuracy_dict_suit.keys(), accuracy_dict_suit.values(),color='green', marker='o')
plt.ylabel("Accuracies of linear classifiers\n used to learn CAVs",fontsize=fontsize-8)
plt.legend(["red,blue,green,yellow"], ["","",""]) # FILL IN MISSING LEGEND
#plt.xlabel("Bottlenecks")