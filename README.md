## Hawaii Climate Analysis and Exploration.
Project focuses on working with database through sqlalchemy Session.query.

### Libraries used:
* Matplotlib.pyplot, datetime, numpy, pandas area plot, sqlalchemy.
* Html, css, flask.

### Database:
* SQLite.

### Part 1 Basic climate analysis and data exploration of SQLite climate database using Python and SQLAlchemy.
* climate_starter.ipynb

* Precipitation and Station Analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
* Precipitation for the last 12 months.
![image](https://github.com/user-attachments/assets/29bfadf5-0452-4c60-bf4f-7fbec56a0d3b)
* Temperatures from the last 12 months from the most active station.
![image](https://github.com/user-attachments/assets/c3572c13-ffe6-4cab-a6e3-95c7541de5b9)

### Part 2 Climate App that shows results of analysis.
* app.py
  
* Flask API was created using Flask, sqlalchemy, jsonify. Server response was generated in JSON format.
<img src = "https://github.com/user-attachments/assets/65dad5f4-7967-402d-9f31-abd382d4bed9" width="500" height="300"/>
<img src="https://github.com/user-attachments/assets/2c347fab-77aa-4edf-86e6-03bc57ea8ec0" width="400" height="300"/>




#### Bonus Part 1 Compare the Temperatures from Months of June and December across all years
* temp_analysis_bonus_1_starter.ipynb
  
* Temperature analysis was done using paired t-test:
  - June mean temperature = 75F,
  - December mean temperature = 71F.
  - To check if this difference is statistically significant we performed the Independent Ttest and found:
  - pvalue <<<< 0.1, which means that the difference in the Average of June and December Temperatures is statistically significant.

#### Bonus Part 2 For selected period of time analyse Temperatures and calculate the total amount of rainfall per weather station
* temp_analysis_bonus_2_starter.ipynb
  
* Find Min, Max, Average Temperatures for selected period of time using SQL function, show Temperature analysis using error bar
  <img src = "https://github.com/user-attachments/assets/5b081f76-9028-42de-a942-b612d5a70f34" width="400" height="500"/>
* The total amount of rainfall per weather station for the trip dates using the previous year's matching dates.
  <img src = "https://github.com/user-attachments/assets/419b3032-72ef-416a-8b85-9a32dd304a9f" width="600" height="400"/>

