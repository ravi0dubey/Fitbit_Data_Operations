import pandas as pd
import csv
import csvkit

def pandas_db_operations():
    pandas_flag = True
    while pandas_flag:
        choice1 = int(input("\nPandas Operataions\n1.Read Fitbit Dataset \n2.Convert Activity date into timestamp format \n3.Print Unique Activity ID\n4.Active ID's dataset\n5.ID's where Activity not logged\n6.Laziest Person in the dataset\n8.How Many have skipped Activity \n"))
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
        elif choice1 == 6:
            lazy_id()
        elif choice1 == 8:
            not_active_regularly_id()
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
