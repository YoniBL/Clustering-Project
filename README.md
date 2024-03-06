# Introduction To Clustering

This project is revolving around clustering.
Clustering is a well known machine learning unsupervised method to learn about data. Clustering focuses taking a lot of data and 
dividing it to different groups, each group holds some data points with similar properties. 
In this project I've implemented some different clustering methods, and compared one to another using scikit tools. 
The first part about this project is an implementation of the Symmetric Non-negative Matrix Factorization (SymNMF) clustering algorithm in both C and Python, along with a Python-C API for improved calculation efficiency.
The second part of the project is about other ML clustering algorithms (e.g. K-Means and Hierarchy agglomerative clustering ) 
and I compared the different methods with an alaysis file. 

## Files Overview

1. **symnmf.c** - This C program contains various functions for SymNMF clustering, including distance calculations, matrix operations, and the core SymNMF algorithm implementation.

2. **symnmfmodule.c** - This module file facilitates the Python-C API for SymNMF clustering. It allows you to access SymNMF functionality from Python, providing a seamless integration between C and Python.

3. **symnmf.py** - This Python script demonstrates how to use the SymNMF algorithm using the Python-C API. It also includes functions for initializing matrices and running the SymNMF algorithm on data.

4. **analysis.py** - This Python script performs an analysis that compares the SymNMF clustering results to those of the other clustering algorithms. It computes silhouette scores to assess the quality of clustering.

5. **kmeans.py** - An implementation of the K-means algorithm

6. **agglomerative_clustering.py** - An implementation of the Hierarchy agglomerative clustering algorithm

7. **setup.py** -  This file aids in distributing the Python-C API module.

8. **symnmf.h** - A header for the main C program.

9. **Makefile** - The Makefile smplifies the compilation of C code with predefined rules.  

Overall it's my first meaningful project, and although not alot of coding done in it, this project demonstrates proficiency in C and Python programming, including the creation of a Python-C API for efficient algorithm execution. It showcases expertise in matrix operations, numerical computation, and data manipulation using libraries like NumPy and pandas. Additionally, the project highlights knowledge and skills in machine learning evaluation, specifically in comparing clustering algorithms using silhouette scores. Overall, this project bridges programming languages, implements complex mathematical algorithms, and conducts rigorous data analysis, making it a valuable contribution to clustering and data analytics.


## Installation

To install the SymNMF Clustering Algorithm, follow these steps:

1. Clone the repository
2. Using the SymNMF in python :
import symnmf

# Load your data and configure parameters
data = ...
k = ...
iterations = ...

# Initialize and run the SymNMF algorithm
result = symnmf.symnmf(data, k, iterations)

# Analyze clustering results
# (You can use functions from the analysis.py script)

Running the analysis -
   To compare K-Means and SymNMF, run the analysis script :
   
python analysis.py <k_clusters> <data_file>

and replace k_clusters in the amount of clusters you want and data file with the path to your data file.
