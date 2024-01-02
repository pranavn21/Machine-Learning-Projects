## Linear Regression using Gradient Descent

### This assignment is a part of my assignments in CS 4375: Machine Learning

---

How to run: This is a Python code generated with Google Colab Python notebooks. Ensure you are in the proper directory if using a terminal and run the following command: python <path_to_file>.py

If you are running via an IDE, then make sure that Python is installed and press Run.

# Part 1

This is my self-developed gradient descent algorithm applied to a linear regression problem. I used some libraries to implement this by myself as listed below. I used the Real Estate dataset, which can be found [here](https://archive.ics.uci.edu/dataset/477/real+estate+valuation+data+set).

The steps I took to develop my algorithm were:

- Choosing a sufficient dataset from the UCI ML Repository
- Pre-processing the dataset (removing null/NA values, removing any redundant rows, converting categorical variables to numerical variables, removing irrelevant variables, etc.)

## Trial logs
![image](https://github.com/pranavn21/Machine-Learning-Projects/assets/72369124/5d0f2d59-7ac1-476b-8bb6-137f121ae87a)
![image](https://github.com/pranavn21/Machine-Learning-Projects/assets/72369124/2373233b-d911-4e18-a835-2cd6607c3351)
![image](https://github.com/pranavn21/Machine-Learning-Projects/assets/72369124/5fca8520-d8e3-41b8-a94a-7241c113ad4e)
![image](https://github.com/pranavn21/Machine-Learning-Projects/assets/72369124/0dbbc783-0839-4aa5-8ce0-f68b32c8d16c)
![image](https://github.com/pranavn21/Machine-Learning-Projects/assets/72369124/94650eb4-f234-4e8d-aaf8-1e9716e4b78d)

---

# Part 2

This is a much simpler code as I used an already-developed ML library from the [Scikit Learn package](https://scikit-learn.org/) to perform linear regression. This aimed to compare the results between Part 1 and Part 2 to find the better algorithm.

## Report
I am satisfied that the sci-kit package found the best solution, given this data. If there was better data, then the output from this model would be better, but a linear regression model can only be so good, given this data. I can check by using statistical methods such as variance, or MSE (mean square root error) to calculate the error and find out how accurate this model is. Since this is similar to the first part, the error is probably similar and is high, indicating that the data is too varied and a linear regression model may not be the best option. However, given this data, I am satisfied with the package’s own LinearRegression model results. As seen in trials, the results improve as the learning rate is decreased, and the number of iterations is increased.

---

# Libraries utilized:

Pandas, Numpy, Matplotlib, Sklearn (sci-kit learn)

---

# References

- [GeeksForGeeks - How to find a local minimum](https://www.geeksforgeeks.org/how-to-implement-a-gradient-descent-in-python-to-find-a-local-minimum/)
- [Wikipedia - Explained variation](https://en.wikipedia.org/wiki/Explained_variation)
