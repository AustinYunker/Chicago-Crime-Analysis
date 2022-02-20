# Chicago Crime Analysis

#### Project Status: [Completed as of February 20th, 2022]

## Project Intro/Objective
The purpose of this project is to analyze crimes in Chicago, Illinois and give the probability of an arrest being made. The potential impact is twofold: the city of Chicago could better utilize their resources between crimes with an exceptionally high chance of an arrest compared to those with extremely low odds and investigate why specific types of crimes have such a low chance of arrest.

### Methods Used
* Data Visualization
* Machine Learning
  * Logistic Regression
  * Naive Bayes
  * Linear SVC
  * Random Forest
  * XGBoost
  * Deep Learning

### Technologies 
* Python (pandas, numpy, matplotlib, tensorflow, keras)
* Google BigQuery


## Project Description
The data came from Google BigQuery's public data sources. I intended to explore the relationship between crime details and arrest status. To do this, I examined crime type, location, domestic status, community area, district, month of the year, and hour of the day. Since I was interested in predicting an arrest, I focused on the differences in arrest percentage and not just the total number of arrests. Overall, there was a large class imbalance between the number of crimes with an arrest compared to non arrests with nearly 75% of all crimes resulting in no arrest. Therefore, the models were scored using the f1 method. The models were trained on crimes between 2011-2020 and then tested on 2021. This was done since the models would be used on current crimes. Numerous models were used to determine the best method of predicting an arrest. Nearly all models considered gave similar test results with the main difference being the time it took to fit the model. In addition to predicting arrests, I also was interested in looking at the difference between traditional models compared to using deep learning methodologies. The best traditional model was the XGBoost with a test f1-score of 58.23% and accuracy of 90.91% compared to the best deep learning model with a test f1-score of 57.36% and accuracy of 90.52%. From there, both models were put into "production" by being introduced to new crime instances. Ideally, a Web API would be designed in which a user could enter the details of the crime and a probability of arrest would be returned. Both gave near identical predicted probabilities on every new instance. Overall, both models gave much lower f1-scores than expected. My current belief is that since the ratio of arrests to non-arrest was drastically different with a ratio of 1:3 between 2011 - 2020 and 1:7 for 2021. This large difference more than likely effected the model's performance. More specifically, the models were trained on a concept that drifted in the test set. The biggest challenge revolved around the time required to fit the models due to the nearly 3 million rows in the data set.

## Needs of this project

- Web API that users can query for a probability of an arrest

## Getting Started

1. Fork and then Clone this repo
2. Raw Data is kept at Google BigQuery. 
    * To access, you'll need to setup a free account. You can do so [here](https://cloud.google.com/bigquery?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1011347&utm_content=text-ad-none-any-DEV_c-CRE_573203586659-ADGP_Desk%20%7C%20BKWS%20-%20PHR%20%7C%20Txt%20~%20Data%20Analytics%20~%20BigQuery_Big%20Query-KWID_43700068782255081-aud-388092988201%3Akwd-300487425311&utm_term=KW_google%20bigquery-ST_google%20bigquery&gclsrc=aw.ds&gclid=CjwKCAiA6seQBhAfEiwAvPqu14q7OKCAazrTELuSwrUZqDBUd5QNdgdYN1inSrmcY65-yGdVj_XAPRoCr6kQAvD_BwE). 
    * After you'll need to change to project id string used in the fetch chicago data function.
4. Data processing/transformation scripts/modules are kept in this repository.

## Featured Notebooks
* [Data Cleaning](https://github.com/AustinYunker/Chicago-Crime-Analysis/blob/main/Data%20Cleaning%20and%20Exploration.ipynb)
* [Data Visualization](https://github.com/AustinYunker/Chicago-Crime-Analysis/blob/main/Data%20Visualization.ipynb)
* [Traditional Models](https://github.com/AustinYunker/Chicago-Crime-Analysis/blob/main/Chicago%20Models%20Part%201.ipynb)
* [Deep Learning Models](https://github.com/AustinYunker/Chicago-Crime-Analysis/blob/main/Chicago%20Models%20Part%202.ipynb)
* [Productionizing the Models](https://github.com/AustinYunker/Chicago-Crime-Analysis/blob/main/Productionize%20Models.ipynb)


## Contact
* Feel free to contact me with any questions or if you are interested in contributing!

## Acknowledgements 
* This style of README was adopted from Rocio Ng and the original template can be found [here](https://github.com/sfbrigade/data-science-wg/blob/master/dswg_project_resources/Project-README-template.md)
