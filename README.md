<h2 align="center"> AlmaBetter Verfied Project - <a href="https://drive.google.com/file/d/1ZkuQx3m_hQYTtXPFjs6bSt_rNlHI5-0P/view?usp=drive_link"> Mobile Price Range Prediction </a> </h5>
<p align="center">
<img class="right" alt="Data Scienctist" width="1000" src="https://user-images.githubusercontent.com/113955196/210127415-b2067d99-45e5-4806-b9d9-723b1cbcea70.png"/>
</p>

</p>
<h2> ⏳ Dataset</h2>
<p>
In the competitive mobile phone market companies want to understand sales data of mobile phones and factors which drive the prices. The objective is to find out some relation between features of a mobile phoneleg - RAM Internal Memory, etc) and its selling price in this problem, we do not have to predict the actual price but a price range indicating how high the price is.
<p>In this Project,On the basis of the mobile Specification like Battery power, 3G enabled , wifi ,Bluetooth, Ram etc we are predicting Price range of the mobile.</p>

</p>
Dataset : <a href="https://drive.google.com/file/d/1Lp2UOU88VUeicGeGJStigrQd_6VQsFcm/view?usp=drive_link">Mobile Price Range Prediction</a>

<h2> 🗒️ Description</h2>
<ul>
   <li><p>This Project include one colab file where all the python coding is present.</p>
   <li><p>Performed exploratory data analysis using varius visualization plots.</p>
   <li><p>Trained machine learning model using Logistic regression, k-nearest neighbour, decision tree, random forest, support vector machines, nave bayes etc.</p>  
</li>
</ul>

<h2> 📊 Exploratory Data Analysis</h2>


<p>EDA stands for Exploratory Data Analysis. It is a crucial step in the data analysis process where the primary objective is to gain a better understanding of the data before applying any statistical modeling or hypothesis testing. EDA involves examining and visualizing the data through various techniques to uncover patterns, identify outliers, detect missing values, assess data quality, and understand the relationships between variables. By conducting EDA, data analysts can make informed decisions about data preprocessing, feature engineering, and modeling strategies, ultimately leading to more accurate and meaningful insights. EDA plays a fundamental role in data-driven decision-making and helps guide subsequent steps in the data analysis pipeline.</p>

<h2> 📈 Logistic Regression</h2>
<p>
  Logistic Regression is a popular supervised machine learning algorithm used for binary classification tasks. It models the relationship between the input variables and the probability of the output belonging to a specific class using a logistic function. By fitting a linear regression model to the transformed log-odds of the probabilities, logistic regression estimates the coefficients that best describe this relationship. During prediction, the algorithm applies the logistic function to the input features to compute the probability of the data point belonging to the positive class. Logistic Regression is interpretable, efficient, and can handle both numerical and categorical features. However, it assumes a linear relationship between the input variables and the log-odds, and it may struggle with complex non-linear relationships. Additionally, logistic regression can be sensitive to outliers and multicollinearity among the input variables.
</p>

<h2> ✴️ The k-Nearest Neighbors</h2>
<p>
The k-Nearest Neighbors (KNN) algorithm is a non-parametric machine learning method used for classification and regression tasks. It operates by assigning a new input data point to the class or predicting its value based on the majority vote or average of its k nearest neighbors in the feature space. The algorithm relies on the assumption that similar data points tend to belong to the same class or have similar values. It does not make any explicit assumptions about the underlying data distribution and can handle both numerical and categorical data. However, KNN's performance may be affected by the choice of the number of neighbors (k) and the distance metric used to measure similarity. It is a simple yet effective algorithm that is easy to understand and implement but can be computationally expensive for large datasets.
</p>

<h2> ✳️ Support Vector Machines</h2>
<p>
Support Vector Machines (SVM) is a powerful supervised machine learning algorithm used for both classification and regression tasks. It aims to find an optimal hyperplane that separates data points of different classes by maximizing the margin, which is the distance between the hyperplane and the nearest data points of each class. SVM can handle linearly separable data and nonlinearly separable data through the use of kernel functions that transform the original feature space into a higher-dimensional space. By doing so, SVM can capture complex relationships and achieve better performance. SVM is effective in handling high-dimensional data, can handle both numerical and categorical features, and is less affected by the presence of outliers. However, SVM may be sensitive to the choice of kernel and its hyperparameters, and its training time can be relatively high for large datasets.
</p>

<h2> 🌲 Decision Tree </h2>
<p>
  A decision tree is a machine learning algorithm used for both classification and regression tasks. It represents a flowchart-like structure, where each internal node represents a feature or attribute, each branch represents a decision rule, and each leaf node represents an outcome or a class label. The decision tree recursively partitions the data based on the values of different features, with the goal of maximizing the separation between different classes or minimizing the prediction error. By following the decision path from the root node to a leaf node, the decision tree can make predictions or assign class labels to new instances based on the learned rules. Decision trees are intuitive, interpretable, and capable of handling both categorical and numerical features, making them widely used in various domains for their simplicity and ability to capture complex decision-making processes.
</p>

<h2> 🎄 Random Forest </h2>
<p>
Random Forest is a powerful machine learning algorithm that combines multiple decision trees to make predictions. It works by constructing an ensemble of decision trees, each trained on a random subset of the data and using a random subset of features. Random Forest leverages the principle of "wisdom of the crowd" by aggregating the predictions from individual trees to produce a final prediction. This approach helps to reduce overfitting and increase the model's generalization ability. Random Forest is suitable for both classification and regression tasks, providing accurate and robust predictions even in the presence of noisy or high-dimensional data. It also allows for feature importance assessment, enabling insights into which features contribute the most to the prediction. Random Forest is widely used in various domains due to its flexibility, scalability, and ability to handle complex relationships within the data.
</p>
<h2> 🛠️ Performance metric for regression problems</h2>
<p>
Following metric are used to check the performance of a classification problem: -

1. Accuracy: - It measures the overall correctness of the model's predictions by calculating the ratio of correctly classified instances to the total number of instances. However, accuracy may not be reliable if the classes are imbalanced.

2. Precision: - It calculates the proportion of correctly predicted positive instances out of all instances predicted as positive. Precision provides insights into the model's ability to avoid false positives.

3. Recall: - It calculates the proportion of correctly predicted positive instances out of all actual positive instances. Recall indicates the model's ability to capture positive instances.

4. F1 Score: - It is the harmonic mean of precision and recall, providing a balanced measure of a model's performance. The F1 score considers both precision and recall, making it useful when classes are imbalanced.

5. Confusion Matrix: - It is a tabular representation that shows the count of true positive, true negative, false positive, and false negative predictions for each class. It provides a comprehensive view of a model's performance across all classes.
</p>

<h2> 📋 Documents </h2>
<ul>
   <li><p>High Level Document(HLD) for Yes bank closing price prediction : <a href="https://docs.google.com/document/d/1_igAZ0sWDZghSHzNDNSzs2a_rCk7MlH1/edit?usp=drive_link&ouid=109337113827293771758&rtpof=true&sd=true"> Word Document </a>. </p>
</li>
</ul>
<h2> 📔 Summary : </h2>


<p>
In this project we developed multi-class Classifiers.Classification algorithms are more than just a sorting mechanism for organising unlabeled data instances into distinct groupings. Classifiers include a unique set of dynamic rules that include an interpretation mechanism for dealing with ambiguous or unknown values, all of which are suited to the kind of inputs being analysed. Most classifiers also utilise probability estimates, which enable end-users to adjust data categorization using utility functions.

1. From EDA we can see that here are mobile phones in 4 price ranges. The number of elements is almost similar.

2. half the devices have Bluetooth, and half don’t

3. there is a gradual increase in battery as the price range increases

4. Ram has continuous increase with price range while moving from Low cost to Very high cost.

5. costly phones are lighter.

6. RAM, battery power, pixels played more significant role in deciding the price range of mobile phone.

7. form all the above experiments we can conclude that XGboost classifier and linear regression with using hyperparameters we got the best results.

</p>
