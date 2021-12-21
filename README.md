![KaggleDays_Paris](./kaggledaysparis.png)

# kaggledays-2019-gbdt

Original workshop in Paris:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lmassaron/kaggledays-2019-gbdt/blob/master/Kaggle%20Days%20Paris%20-%20%20GBDT%20workshop.ipynb)

First part of the updated workshop (basics of Skopt and GBM):

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lmassaron/kaggledays-2019-gbdt/blob/master/skopt_workshop_part1.ipynb)

Second part of the updated workshop (LightGBM, XGBoost, CAtBoost, NAS):

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lmassaron/kaggledays-2019-gbdt/blob/master/skopt_workshop_part2.ipynb)

## Video of the workshop on Kaggle Youtube channel
![https://www.youtube.com/watch?v=YQL45hDuP-o](./kaggle_youtube.PNG) 
https://www.youtube.com/watch?v=YQL45hDuP-o

## Kaggle Days Paris
### Competitive GBDT Specification and Optimization Workshop

## Instructors
* Luca Massaron [@lmassaron](https://www.linkedin.com/in/lmassaron/) - Data Scientist / Author / Google Developer Expert in Machine Learning 

![competition](https://road-to-kaggle-grandmaster.vercel.app/api/badges/lucamassaron/competition)
![dataset](https://road-to-kaggle-grandmaster.vercel.app/api/badges/lucamassaron/dataset)
![notebook](https://road-to-kaggle-grandmaster.vercel.app/api/badges/lucamassaron/notebook)
![discussion](https://road-to-kaggle-grandmaster.vercel.app/api/badges/lucamassaron/discussion)

* Pietro Marinelli [@pietro-marinelli-0098b427](https://www.linkedin.com/in/pietro-marinelli-0098b427/) - Freelance Data Scientist

![competition](https://road-to-kaggle-grandmaster.vercel.app/api/badges/pietromarinelli/competition)
![dataset](https://road-to-kaggle-grandmaster.vercel.app/api/badges/pietromarinelli/dataset)
![notebook](https://road-to-kaggle-grandmaster.vercel.app/api/badges/pietromarinelli/notebook)
![discussion](https://road-to-kaggle-grandmaster.vercel.app/api/badges/pietromarinelli/discussion)

## About the workshop

Gradient Boosting Decision Trees (GBDT) presently represent the state of the art for building predictors for flat table data. However, they seldom perform the best out-of-the-box (using default values) because of the many hyper-parameters to tune. Especially in the most recent GBDT implementations, such as LightGBM, the over-sophistication of hyper-parameters renders finding the optimal settings by hand or simple grid search difficult because of high combinatorial complexity and long running times for experiments. 

[Random Optimization](https://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf) (BERGSTRA, James; BENGIO, Yoshua. Random search for hyper-parameter optimization. Journal of Machine Learning Research, 2012, 13.Feb: 281-305.) and [Bayesian Optimization](https://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf) (SNOEK, Jasper; LAROCHELLE, Hugo; ADAMS, Ryan P. Practical bayesian optimization of machine learning algorithms. In: Advances in neural information processing systems. 2012. p. 2951-2959) are often the answer you'll find from experts.

In this workshop we demonstrate how to use different optimization approaches based on [Scikit-Optimize](https://github.com/scikit-optimize/scikit-optimize), a library built on top of NumPy, SciPy and Scikit-Learn, and we present an easy and fast approach to set them ready and usable.

## Prerequisites

You should be aware of the role and importance of hyper-parameter optimization in machine learning.  

## Obtaining the Tutorial Material
In order to make the workshop easily accessible, we are offering cloud access:
* Using [Google Colab](https://colab.research.google.com/github/lmassaron/kaggledays-2019-gbdt/blob/master/Kaggle%20Days%20Paris%20-%20%20GBDT%20workshop.ipynb) 
* Using [Kaggle Kernels](https://www.kaggle.com/lucamassaron/kaggle-days-paris-gbdt-workshop)

We also have a brief exercise that can be found at:
* Using [Google Colab](https://colab.research.google.com/github/lmassaron/kaggledays-2019-gbdt/blob/master/Kaggle%20Days%20Paris%20-%20Skopt%20%2B%20CatBoost%20exercise.ipynb)
* Using [Kaggle Kernels (with solution)](https://www.kaggle.com/lucamassaron/kaggle-days-paris-skopt-catboost-solution)

The solution can be found [here](https://github.com/lmassaron/kaggledays-2019-gbdt/blob/master/Kaggle%20Days%20Paris%20-%20Skopt%20%2B%20CatBoost%20solution.ipynb).

All the materials can be cloned from Github at the [kaggledays-2019-gbdt](https://github.com/lmassaron/kaggledays-2019-gbdt) repository. We also have prepared a stand-alone Windows installation using WinPython (just require us for the link).

## Local installation notes

In order to successfully run this workshop on your local computer, you need a Python3 installation (we suggest installing the most recent [Anaconda](https://www.anaconda.com/download/) distribution) and at least the following packages:

* numpy >= 1.15.4
* pandas >= 0.23.4
* scipy >= 1.1.0
* skopt >= 0.5.2
* sklearn >= 0.20.2
* lightgbm >= 2.2.2
* xgboost >= 0.81
* catboost >= 0.12.2
