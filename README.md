# Chicago Crime Analysis

#### Project Status: [Completed as of February 20th, 2022]

## Project Intro/Objective
The purpose of this project is to analyze crimes in Chicago, Illinois and give the probability of an arrest being made. The potential impact is twofold: the city of Chicago could better utilize their resources between crimes with an exceptionally high chance of an arrest compared to those with extremely low odds and investigate why specific types of crimes have such a low chance of arrest.

### Methods Used
* Data Visualization
* Machine Learning
  * Logistic Regression
  * Naive Bayes
  * Random Forest
  * XGBoost
  * Deep Learning

### Technologies 
* Python (pandas, numpy, matplotlib, tensorflow, keras)
* Google BigQuery


## Project Description
The data came from Google BigQuery's public data sources. I intended to explore the relationship between crime details and arrest status. To do this, I examined crime type, location, domestic status, community area, district, month of the year, and hour of the day. Since I was interested in predicting an arrest, I focused on the differences in percentages of arrest and not just the total. Overall, there was a large class imbalance between the number of crimes with an arrest compared to non arrests with nearly 75% of all crimes resulting in no arrest. Therefore, the models were scored using the f1 method. Numerous models were used to determine the best method of predicting an arrest. Nearly all models considered gave similar results with the main difference being the time it took to fit the model. The biggest challenges revolved around the time required 

(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- etc. (be as specific as possible)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](link)
* [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link)


## Contributing DSWG Members

**Team Leads (Contacts) : [Full Name](https://github.com/[github handle])(@slackHandle)**

#### Other Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Full Name](https://github.com/[github handle])| @johnDoe        |
|[Full Name](https://github.com/[github handle]) |     @janeDoe    |

## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!
