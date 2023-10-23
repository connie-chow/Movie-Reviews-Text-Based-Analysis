# Movie Reviews Prediction Modeling Project
This is a final project for ADS509: Building a Text Based Analysis Classification Model To Determine Movie Review Sentiment

[Business Case Presentation (Business & Executive Audiences)](https://docs.google.com/presentation/d/148sGmTrqkthCvEs_wwvh8I8FSqE4T2kByE2uJKcvSPE/edit?usp=sharing)
<br>
[Technical Presentation (Data Science Audiences)](https://docs.google.com/presentation/d/1ceFUqH39ycUjJNCHokU0Omur2VmzXEG2BoXHk2ruCkM/edit?usp=sharing)

#### -- Project Status: [In-Progress]

## Project Intro & Description
 In this project, movie reviews were loaded from Rotten Tomatoes and TMdb.  These movie reviews are then preprocessed and analyzed to observe the relation between the text and the movie reviewer sentiment, ultimately the reviewer's rating for the movie as "good" or "bad".  A classification model was built using Naive Bayes algorithm and checked against several topic modeling algorithms such as LDA, LSA and NMT.

The goal of the project is to be able to predict a movie reviewer's rating based on the review written.  This has applications to movie pilot selection and incubation within the movie studio production industry.

### Team 3
* Jacqueline Vo
* Connie Chow

### Methods Used
* Data Pre-Processing
* Exploratory Data Analysis
* Feature Extraction
* Predictive Modeling
* Topic Modeling


### Technologies
* Python
* nltk package
* Pandas


## Needs of this project
- Data Exploration
- Descriptive Statistics
- Data Preprocessing
- Standard Text Cleaning Techniques
- Statistical Modeling
- Evaluation & Writeup/Reporting


## Getting Started
1. Clone this repo using raw data.
2. Add code and push new code into repo. To ensure cohesive code make sure to run all cells prior to upload. 
3. Use ###### flags for output


## Modeling
- Naive Bayes Classification model in nltk package was used to build a classification model for movie review text
- LinearSVC

## Modeling Results
- Words that were most informative for a movie review being good: wonderfully, outstanding, standup, ups...
- Words that were most informative for a movei review being bad: dumbest, unfunny, simpsons, wonder, homocidal, finished, amatuerish, hercule, nutcase, stinks...
- Out of the top 25 most informative words, 17 or 68% of the words were indicative of bad reviews.  We can make a generalized conclusion that more reviews are written in which there is a poor sentiment after watching the movie. 

