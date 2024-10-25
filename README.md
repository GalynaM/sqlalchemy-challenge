## Hawaii Climate Analysis and Exploration.
Project focuses on working with database through sqlalchemy Session.query.

### Libraries used:
* Matplotlib.pyplot, datetime, numpy, pandas area plot, sqlalchemy.

### Database:
* SQLite.

### Part 1 climate_starter.ipynb
* Basic climate analysis and data exploration of SQLite climate database using Python and SQLAlchemy.
* Precipitation and Station Analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
* Precipitation for the last 12 months.
![image](https://github.com/user-attachments/assets/29bfadf5-0452-4c60-bf4f-7fbec56a0d3b)
* Temperatures from the last 12 months from the most active station.
![image](https://github.com/user-attachments/assets/c3572c13-ffe6-4cab-a6e3-95c7541de5b9)

### Part 2
* Climate App that shows results of analysis.
* Flask API was created using Flask, hmtl, css.
* app.py

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
  ![image](https://github.com/user-attachments/assets/5b081f76-9028-42de-a942-b612d5a70f34)
* The total amount of rainfall per weather station for the trip dates using the previous year's matching dates.
  ![image](https://github.com/user-attachments/assets/419b3032-72ef-416a-8b85-9a32dd304a9f)

