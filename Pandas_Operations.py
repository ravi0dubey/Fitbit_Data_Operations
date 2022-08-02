import pandas as pd
import csv
import csvkit

def pandas_db_operations():
    pandas = True
    while sql_flag:
        choice1 = int(input("\nPandas Operataions\n1.Able to connect to MYSQL \n2.Create script of table Fitbit \n3.Create a table fitbit in MYSQL\n4. Do a bulk load fitbit dataset in MYSQL\n"))
        if choice1 == 1:
            connect_db()
        elif choice1 == 2:
            create_table_script()
        elif choice1 == 3:
            create_mysql_table()
        elif choice1 == 4:
            load_mysql_table()
        else:
            print("Return to Main Operations")
            sql_flag = False


def pandas_read_csv():
    fitbit_data_set1 =pd.read_csv('D://Study//Data Science//Python//ineuron//Data_Set//FitBit_Data.csv')
