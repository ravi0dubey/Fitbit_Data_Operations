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
# 13. Explore over an internet that how much calories burn is required for a healthy person and find out how many healthy person we have in our dataset

import pandas as pd
import csv
import csvkit

def pandas_db_operations():
    pandas_flag = True
    while pandas_flag:
        choice1 = int(input("\nPandas Operataions\n1.Read Fitbit Dataset \n2.Convert Activity date into timestamp format \n3.Print Unique Activity ID\n4.Active ID's dataset"
                            "\n5.ID's where Activity not logged\n7.Laziest Person in the dataset\n8.Calories Burn required and based on it how many of them are Healthiest in dataset"
                            "\n9.How Many have skipped Activity\n10: Third Most Active Person in dataset\n11. Nth most laziest person in the dataset\n12.What is a total cumulative clories burn for a person"
                            "\n\nEnter Your Choice :"))
        if choice1 == 1:
            pandas_print_dataset()
        elif choice1 == 2:
            convert_date_timestamp()
        elif choice1 == 3:
            unique_activity_id()
        elif choice1 == 4:
            active_id()
        elif choice1 == 5:
            activity_not_logged()
        elif choice1 == 7:
            lazy_id()
        elif choice1 == 8:
            calories_burn_active_id()
        elif choice1 == 9:
            not_active_regularly_id()
        elif choice1 == 10:
            third_active_regularly_id()
        elif choice1 == 11:
            fifth_laziest_id()
        elif choice1 == 12:
            calories_burn_per_Id()
        else:
            print("Return to Main Operations")
            pandas_flag = False


def pandas_read_csv():
    # sys.setrecursionlimit(5000)
    fitbit_data_set1 =pd.read_csv('D://Study//Data Science//Python//ineuron//Data_Set//FitBit_Data.csv')
    return fitbit_data_set1


def pandas_print_dataset():
    df1= pandas_read_csv()
    print(f"Dataset read from fitbit: \n{df1}")

def convert_date_timestamp():
    df1 = pandas_read_csv()
    # converting the string to datetime format
    df1['ActivityDate_New'] = pd.to_datetime(df1['ActivityDate'], infer_datetime_format=True)
    print(f"Dataset with date converted: \n{df1}")

def unique_activity_id():
    df1 = pandas_read_csv()
    # Finding unique Activity Id
    a_list = df1['Id'].unique()
    print(f"Printing Unique Activity Id1: \n{pd.DataFrame(a_list) }")


def active_id():
    df1 = pandas_read_csv()
    print(f"Active ID's dataset: \n{df1[df1['TotalSteps']>0] }")

def activity_not_logged():
    df1 = pandas_read_csv()
    a1 = df1.groupby(['Id'])[['TotalSteps', 'TotalDistance']].agg(['sum', 'mean', 'count'])
    print(f"Activity Not Logged ID's dataset: \n")
    print(a1.sort_values(by=[('TotalSteps', 'sum'), ('TotalDistance', 'sum')], ascending=True).head(1))


def lazy_id():
    df1 = pandas_read_csv()
    # print(f"Lazy ID's dataset: \n{pd.DataFrame(df1[(df1['TotalSteps']==0) & (df1['SedentaryMinutes']==max(df1['SedentaryMinutes']))]['Id'].unique())}")
    print(f"Lazy ID's dataset: \n")
    b = df1.groupby(['Id'])[['TotalSteps', 'TotalDistance', 'SedentaryMinutes']].agg(['sum'])
    print(b.sort_values(by=[('TotalSteps', 'sum'), ('TotalDistance', 'sum')], ascending=True).head(1))



def calories_burn_active_id():
    df1 = pandas_read_csv()
    healthy_df1 = df1.groupby('Id')['Calories'].agg(['sum', 'mean'],2).sort_values(by=['mean'], ascending=False)
    carlories_to_burn= int(input("How many Calories should be burnt on Average: "))
    print(f"Healthy Dataset in descending Order where Calories burned is greater than {carlories_to_burn}\n")
    print(healthy_df1[healthy_df1['mean'] > carlories_to_burn])
    print(f"Count of Healthy Id's:\n {healthy_df1[healthy_df1['mean'] > carlories_to_burn].count()}")

def count_skipped_days(steps_val):
    # skipped_val= int(input("Enter How many days skipped data you want : "))
    skipped_val = 5
    if steps_val >=skipped_val:
        return "Y"
    else:
        return "N"


def not_active_regularly_id():
    df1 = pandas_read_csv()
    a = df1[df1['TotalSteps'] == 0]
    a1 = a.groupby(['Id'])[['TotalSteps']].count()
    a1['count_skipped'] = a1['TotalSteps'].apply(count_skipped_days)
    print("\n How many are not active regularly\n")
    print(a1[a1['count_skipped'] == 'Y'])

def third_active_regularly_id():
    df1= pandas_read_csv()
    b = df1.groupby(['Id'])[['TotalDistance']].agg(['sum']).sort_values(by=('TotalDistance', 'sum'), ascending=False)
    n = int(input("Enter which nth active value you want: "))
    print(f"{n}th active value from dataset is : {b.iloc[n - 1]}")

def fifth_laziest_id():
    df1 = pandas_read_csv()
    b = df1.groupby(['Id'])[['TotalSteps', 'TotalDistance', 'SedentaryMinutes']].agg(['sum'])
    b.sort_values(by=[('TotalSteps', 'sum'), ('TotalDistance', 'sum')], ascending=True)
    n = int(input("Enter which nth active value you want: "))
    print(f"\n{n}th Laziest_ID from dataset is : {b.iloc[n - 1]}")

def calories_burn_per_Id():
    df1 = pandas_read_csv()
    b = df1.groupby(['Id'])[['Calories']].agg(['sum'])
    print(f"Total Calories Burn Per ID :\n{b}")