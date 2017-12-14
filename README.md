# w209_Group_Project


# Project was largely built in Tableau. Data and Tableau files are too large to upload to Github. Please visit:

## Final Project Webpage
http://people.ischool.berkeley.edu/~amy/209_final_project/index.html

### Tableau Vizzes
https://public.tableau.com/profile/matthew.nelson6182#!/ . 
https://public.tableau.com/profile/varadarajan.srinivasan#!/




**A) To build data used in the above vizzes:**

1. Unzip the Data
2. Edit the hardcoded locations of that data in both city_AQI_build.py and county_AQI_build.py
3. Run both city_AQI_build.py and county_AQI_build.py

**B) To build the data for Toxics Vizzes:**
1. Run the 4 notebooks Data-Download-HAPS.ipynb, Data-Download-VOCS.ipynb, Data-Download-Lead.ipynb, Data-Download-NONOxNOy.ipynb
2. Run the Data_Combine_All_Toxics.ipynb
3. Data will be downloaded from EPA website and consolidated into one single file. Users will have to modify the directory path in each piece of code.

**C) For Cancer Data creation:**
1. Cancer_Data_Code.ipynb and cancer merge.ipynb

**D) For AQI Severity Dashboard data:**
1. Once city_AQI dataset is created using city_AQI_build.py, run the Code_For_AQI_by_Severity.ipynb notebook using the city_AQI.csv dataset.
