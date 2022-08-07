

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

import pandas as pd
import mysql.connector as connection

def sql_db_operations():
    sql_oper_flag = True
    while sql_oper_flag:
        choice2 = int(input(
            "\nSQL Db Operataions\n1.Convert Activity date into timestamp format \n2.Print Unique Activity ID\n3.Active ID's dataset"
            "\n4.ID's where Activity not logged\n5.Laziest Person in the dataset\n6.Calories Burn required and based on it how many of them are Healthiest in dataset"
            "\n7.How Many have skipped Activity\n8: Third Most Active Person in dataset\n9. Nth most laziest person in the dataset\0.What is a total cumulative clories burn for a person"
            "\n\nEnter Your Choice :"))
        if choice2 == 1:
            db_date_time()
        elif  choice2 == 2:
            db_date_time()
        else:
            print("Return to Main Operations")
            sql_oper_flag = False

def db_connect():
    mydb1 = connection.connect(host="localhost", database="projectdb", user="devuser", passwd="Logitech1234#",use_pure=True)
    return(mydb1)

def db_date_time():
    try:
        mydb1 = db_connect()
        # mydb1 = connection.connect(host="localhost",database= "projectdb", user="devuser", passwd="Logitech1234#", use_pure=True)
        cursor1 = mydb1.cursor()
        print("Show Database records with converted Date and Time")
        read_data_query = "select id, ActivityDate, STR_TO_DATE(ActivityDate, '%m/%d/%YY%HH%MM%SS') as new_activity_date from projectdb.fitbit_data; "
        cursor1.execute(read_data_query)
        print(f"Fitbit data reading using cursor\n {cursor1.fetchall()}")
        print(f"\nFitbit data reading using read_sql\n")
        print(pd.read_sql(read_data_query, mydb1))
    except Exception as e:
            mydb1.close()
            print(f"Error in Converting Date Time format : {e}")


def print_unique_id_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()


# 6. How many of them have not logged there activity, find out their ids
# SELECT ID FROM fitbit_data group by ID having sum(TotalSteps) = 0;
# SELECT COUNT(distinct(ID)) FROM fitbit_data
# group by ID
# having sum(TotalSteps) = 0;

# 9. How many are not active regularly
# SELECT ID, totalsteps FROM fitbit_data group by ID
# having TotalSteps = 0;