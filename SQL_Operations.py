

# # Task 1 - FitbitDataset
# 1. Read fitbit dataset in pandas, mysql and Mongodb
# 2. While creating a table in mysql, use automation to create table in mysql. use csvkit library to automate the task
# 3. Convert all the dates available in dataset to timestamp format in pandas and in sql convert it into dateformat
# 4. Find out unique id's in data
# 5. Find out Active id dataset
# 6. How many of them have not logged there activity, find out their ids
# 7. Find out who is laziest person id in the dataset
# 8. Search on internet how much calories are burn is required for a healthy person and find out how many person we have in our data
# 9. How many are not active regularly
# 10. Third most active person in dataset, find out using pandas and sql
# 11. 5th most laziest person in the dataset
# 12. what is a total cumulative clories burn for a person

# 6. How many of them have not logged there activity, find out their ids
# SELECT ID FROM fitbit_data group by ID having sum(TotalSteps) = 0;
# SELECT COUNT(distinct(ID)) FROM fitbit_data
# group by ID
# having sum(TotalSteps) = 0;

# 9. How many are not active regularly
# SELECT ID, totalsteps FROM fitbit_data group by ID
# having TotalSteps = 0;