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

import SQL_Connection
import SQL_Operations as sc
import Pandas_Operations as po

fitbit_flag_operations = True
while fitbit_flag_operations:
    choice = int(input("\n1.My SQL \n2.Pandas\n3\n"))
    if choice == 1:
        SQL_Connection.mysql_db_operations()
    if choice == 2:
        po.pandas_db_operations()
    else:
        print("have a good day")
        fitbit_flag_operations = False
