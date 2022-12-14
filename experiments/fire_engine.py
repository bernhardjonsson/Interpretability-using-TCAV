import tcav.activation_generator as act_gen
import tcav.cav as cav
import src.model as model
import tcav.tcav as tcav
import tcav.utils as utils
#import tcav.utils_plot as utils_plot # utils_plot requires matplotlib
import os
import tensorflow as tf
import pickle


project_dir = 'tcav_dir'
# the name of the parent directory that results are stored (only if you want to cache)
project_name = 'tcav_fire_engine'
working_dir = "/tmp/" + project_dir + '/' + project_name
# where activations are stored (only if your act_gen_wrapper does so)
activation_dir =  working_dir+ '/activations/'
# where CAVs are stored.
# You can say None if you don't wish to store any.
cav_dir = working_dir + '/cavs/'
# where the images live.

# TODO: replace 'YOUR_PATH' with path to downloaded models and images.
source_dir = """/mnt/c/Users/bejons/Documents/wsl_Share_Space/DeepLearning/data"""
bottlenecks = [ 'mixed3a','mixed3b','mixed4a','mixed4b','mixed4c','mixed4d','mixed4e','mixed5a','mixed5b','logit']  # @param

utils.make_dir_if_not_exists(activation_dir)
utils.make_dir_if_not_exists(working_dir)
utils.make_dir_if_not_exists(cav_dir)

# this is a regularizer penalty parameter for linear classifier to get CAVs.
alphas = [0.1]

target = 'fire engine'
concepts = ["red-c","yellow-c","blue-c","green-c"]


# Create TensorFlow session.
sess = utils.create_session()

# GRAPH_PATH is where the trained model is stored.
GRAPH_PATH = source_dir + """/inception5h/tensorflow_inception_graph.pb"""
# LABEL_PATH is where the labels are stored. Each line contains one class, and they are ordered with respect to their index in
# the logit layer. (yes, id_to_label function in the model wrapper reads from this file.)
# For example, imagenet_comp_graph_label_strings.txt looks like:
# dummy
# kit fox
# English setter
# Siberian husky ...

LABEL_PATH = source_dir + """/inception5h/imagenet_comp_graph_label_strings.txt"""

mymodel = model.GoogleNetWrapper_public(sess,
                                        GRAPH_PATH,
                                        LABEL_PATH)

act_generator = act_gen.ImageActivationGenerator(mymodel, source_dir, activation_dir, max_examples=200)
import absl
absl.logging.set_verbosity(0)
num_random_exp=25
## only running num_random_exp = 10 to save some time. The paper number are reported for 500 random runs.
mytcav = tcav.TCAV(sess,
                   target,
                   concepts,
                   bottlenecks,
                   act_generator,
                   alphas,
                   cav_dir=cav_dir,
                   num_random_exp=num_random_exp)#10)
print ('This may take a while... Go get coffee!')
results = mytcav.run(run_parallel=False)
print ('done!')
file = open('fire_engine_results.bin', 'wb')
pickle.dump(results, file)
file.close()
