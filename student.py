import pandas as pd
import os

EXCEL_FILE = "students.xlsx"

def save_student_data():
    # Take input from user
    rollno = input("Enter Roll No: ")
    std = input("Enter Std: ")
    schoolcode = input("Enter School Code: ")
    city = input("Enter City: ")
    name = input("Enter Name: ")

    data = input[rollno,std,schoolcode,city,name]

    df_new = pd.DataFrame(data)

    # If Excel exists, append new data; else create new file
    if os.path.exists(EXCEL_FILE):
        df_existing = pd.read_excel(EXCEL_FILE)
        df_all = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_all = df_new

    # Save to Excel
    df_all.to_excel(EXCEL_FILE, index=False)

    print(f"✅ Data saved to {EXCEL_FILE}")

if __name__ == "__main__":
    save_student_data()
