# Third-Project


Source: "Rain in Australia" Kaggle dataset — daily weather observations across Australian weather stations.
Dataset source:https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package.

Team_Name : Riders of the Storm
Team_Members : Avaritsioti Olympia, George Zippidis, Zervos Theologos, Georgia Samara.



SCOPE: 3rd Data Science Project for Big Blue Data Academy Bootcamp.


DATA: This dataset comprises about ten(10) years of daily weather observations from numerous locations across Australia.


CONTEXT : Ever wondered if you should carry an umbrella tomorrow? With this dataset, you can predict next-day rain by training classification models on the target variable RainTomorrow.


- `Folder1/`: Exercises for Module 1 (Python for Data Science)
- `Folder1/`: Exercises for Module 1 (Python for Data Science)
- `Folder1/`: Exercises for Module 1 (Python for Data Science)
- `Folder1/`: Exercises for Module 1 (Python for Data Science)


Our project includes :

	⦁	Exploratory Data Analysis process.
	⦁	Data Cleanning & Feature Engineering through seer python using Pandas mostly.
	⦁	Train & Split methodology.
	⦁	Predictions using Regression and Ensemble models.



MAIN GOAL :	"Will it rain tomorrow?" (Yes/No) — a binary prediction that shapes travel plans


DATA : 

	⦁	Daily Observations are estimated around (126k) -- Post Data Cleanning.
	⦁	Variables including target / Features (11) -- Post Data Processing.
	⦁	Majority class is No-rain(1) with 78% of total outputs.
	⦁	Minority class is Rain-Tomorrow with 22% of total outputs.
	
	

DATA PREPARATION PROCESS :
	
	⦁	Missing Values (Pragmatic handling to keep dataset usable).
	⦁	Feature Engineering (Combine 9am/3pm readings into daily averages + month seasonality).
	⦁	Train/Test Split (Random stratified (75/25) to preserve class balance).
	⦁	SMOTE Application (Synthetic oversampling applied on training set only (not test)).



HOW WE MEASURE SUCCESS :
	
	WHY ACCURACY MISLEADS (With 78% No Rain class, a model that always predicts "No Rain" achieves 78% accuracy — useless for travel planning).
		
		Primary Metrics
			
			⦁	Balanced : Accuracy: Treats both classes fairly.
			⦁	Macro F1: Balances precision and recall.


	NEW GOAL :
	
		Improve RECALL for "Rain=Yes" while controlling false alarms.


		

MODELS :

	⦁	LOGISTIC REGRESSION (BINARY CLASSIFICATION PROBLEM).
	⦁	RANDOM FOREST CLASSIFIER (DEEPER & CLEARER ANSWERS, NON LINEAR BASELINE (MULTIPLE ESTIMATORS TYPE).
	⦁	GRADIENT BOOSTING (STRONG TABULAR MODEL, PROGRESSIVE OVERLOAD AND ACCURACY).




RESULTS : 

	Winner model: RANDOM FOREST
		
		⦁	Balanced Accuracy : 78 %
		
		⦁	Macro F1 :+1 :		72 %
		
		⦁	Macro Recall :		77 %
		
	
	Key Metric : 
	
		⦁	Minority-class recall (Rain=Yes): 77%

		Confusion Matrix application (Presentation) of correct True Positives and False Positives values ( 77 % False Positive for (1) which means with had 77 percentage correct predictions on our (True(Yes) - Rain=Yes) outcome.

		


Limitations & Next Steps

	Current Limitations :
	
		⦁	Random split (not time-based).
		⦁	Location removed.
		⦁	Pragmatic missing-value handling.



	Future Improvements

		⦁	Time-based validation.
		⦁	Compare "with vs without persistence features".
		⦁	Calibrate probabilities.





----------------------------------- AN EXPLAINABLE RAIN-RISK PREDICTOR THAT SUPPORTS BETTER TRAVEL PLANNING DECISIONS ----------------------------------------------------