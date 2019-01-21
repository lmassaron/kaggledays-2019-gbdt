# kaggledays-2019-gbdt
![Kaggle Days Paris](https://kaggledays.com/wp-content/uploads/sites/2/2018/11/46508555_1939772529664297_1579296553191866368_n-1024x536.png)

## Kaggle Days Paris
### Competitive GBDT specification and optimization workshop

## Instructors
* Luca Massaron [@lmassaron](https://www.linkedin.com/in/lmassaron/) - Data Scientist / Author / Google Developer Expert in Machine Learning 
* Pietro Marinelli [@pietro-marinelli-0098b427](https://www.linkedin.com/in/pietro-marinelli-0098b427/) - Freelance Data Scientist

## About the workshop

Gradient Boosting Decision Trees (GBDT) are presently the state of the art for building predictors for tabular data. However, they seldom perform the best out-of-the-box (using default hyper-parameters). 

The over-sophistication of GBDT hyper-parameters renders finding the optimal settings difficult because of high combinatorial complexity and long running times for experiments. 

[Random Optimization](https://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf) (BERGSTRA, James; BENGIO, Yoshua. Random search for hyper-parameter optimization. Journal of Machine Learning Research, 2012, 13.Feb: 281-305.) and [Bayesian Optimization](https://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf) (SNOEK, Jasper; LAROCHELLE, Hugo; ADAMS, Ryan P. Practical bayesian optimization of machine learning algorithms. In: Advances in neural information processing systems. 2012. p. 2951-2959) are the answer.

In this workshop we show you how to use different optimization approaches based on [Scikit-Optimize](https://github.com/scikit-optimize/scikit-optimize), a library built on top of NumPy, SciPy and Scikit-Learn, and presenting an easy and fast approach to set them ready and usable.

## Prerequisites

You should be aware of the role of hyper-parameter optimization in machine learning and why it is important to tune hyper-parameters.  

## Obtaining the Tutorial Material
In order to make the workshop easily accessible, we suggest accessing it on the cloud:
* Using [Google Colab](https://colab.research.google.com/github/lmassaron/kaggledays-2019-gbdt)
* Using [Kaggle Kernels]()

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
