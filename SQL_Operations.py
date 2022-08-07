

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
            db_print_unique_id_sql()
        elif  choice2 == 3:
            db_active_id_sql()
        else:
            print("Return to Main Operations")
            sql_oper_flag = False

def db_connect():
    mydb1 = connection.connect(host="localhost", database="projectdb", user="devuser", passwd="Logitech1234#",use_pure=True)
    return(mydb1)

def db_date_time():
    try:
        mydb1 = db_connect()
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


def db_print_unique_id_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    unique_id_query = "select distinct(id) as unqiue_id from projectdb.fitbit_data; "
    cursor1.execute(unique_id_query)
    print(f"Fitbit Unique Id data reading using cursor\n {cursor1.fetchall()}")


def db_active_id_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    active_id_query = "SELECT distinct(ID) FROM fitbit_data group by ID having sum(TotalSteps) > 0 ;"
    cursor1.execute(active_id_query)
    print(f"Fitbit Active Id data reading using cursor\n {cursor1.fetchall()}")

# 6. How many of them have not logged there activity, find out their ids
def db_activity_not_logged_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    activity_not_logged_id_query ="SELECT ID FROM fitbit_data group by ID having sum(TotalSteps) = 0;"
    cursor1.execute(activity_not_logged_id_query)
    print(f"Fitbit Activity Not Logged Id data reading using cursor\n {cursor1.fetchall()}")

# 7. Find out who is laziest person id in the dataset
def db_laziest_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    lazies_id_query ="SELECT id, sum(TotalSteps) FROM fitbit_data group by ID order by sum(TotalSteps) limit 1 ;"
    cursor1.execute(lazies_id_query)
    print(f"Fitbit Laziest Id data  using cursor\n {cursor1.fetchall()}")

# 9. How many are not active regularly
def db_not_active_regularly_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    not_active_query = " SELECT ID, totalsteps FROM fitbit_data group by ID having TotalSteps = 0;"
    cursor1.execute(not_active_query)
    print(f"Fitbit Not Active Regularly Id data  using cursor\n {cursor1.fetchall()}")


# 10. Third most active person in dataset, find out using pandas and sql
def db_third_most_activey_sql():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    third_most_active_query = " SELECT id, sum(TotalSteps) as total_steps_sum " \
                              "FROM fitbit_data " \
                              "group by ID " \
                              "order by sum(TotalSteps) " \
                              "desc limit 2,1;"
    cursor1.execute(third_most_active_query)
    print(f"Fitbit 3rd Most Active Regularly Id data  using cursor\n {cursor1.fetchall()}")

# 10. Third most active person in dataset, find out using pandas and sql
def db_third_most_activey_sql_alternate():
    mydb1 = db_connect()
    cursor1 = mydb1.cursor()
    create_view_query ="create view sum_total_steps as SELECT id, sum(TotalSteps) as total_steps_sum FROM fitbit_data group by ID order by sum(TotalSteps) desc;"
    cursor1.execute(create_view_query)
    third_most_active_query_1= "SELECT id, total_steps_sum FROM sum_total_steps AS sum1   WHERE 3-1 = (SELECT COUNT(DISTINCT total_steps_sum) FROM sum_total_steps AS sum2  WHERE sum2.total_steps_sum > sum1.total_steps_sum);  "
    cursor1.execute(third_most_active_query_1)
    print(f"Fitbit 3rd Most Active Regularly Id data  using cursor\n {cursor1.fetchall()}")

# 11. 5th most laziest person in the dataset
# 12. what is a total cumulative clories burn for a person
