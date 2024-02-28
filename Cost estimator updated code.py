#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Cost Estimator
import pandas as pd
def calculate_storage_cost(initial_data_size_tb, storage_type, no_of_months):
    # Convert initial data size to TB
    data_size_tb = initial_data_size_tb/5
    if storage_type == 'on-demand':
        storage_cost_tb = data_size_tb * 40 * no_of_months
    elif storage_type == 'capacity':
        storage_cost_tb = data_size_tb * 23 * no_of_months
    else:
        raise ValueError("Invalid storage type. Please choose 'on-demand' or 'capacity'.")
    return storage_cost_tb
    
def calculate_compute_cost(edition_type, num_departments, warehouse_size_dl, no_of_days_dl, no_of_hours_per_day_dl, department_data):
    # Determine credit per hour based on warehouse size
    if warehouse_size_dl == 'x-small':
        credit_per_hour_dl = 1.0
    elif warehouse_size_dl == 'small':
        credit_per_hour_dl = 2.0
    elif warehouse_size_dl == 'medium':
        credit_per_hour_dl = 4.0  
    elif warehouse_size_dl == 'large':
        credit_per_hour_dl = 8.0  
    elif warehouse_size_dl == 'x-large':
        credit_per_hour_dl = 16.0  
    elif warehouse_size_dl == '2x-large':
        credit_per_hour_dl = 32.0
    else:
        raise ValueError("Invalid warehouse size for Data Loading Requirement. Please choose 'x-small', 'small', 'medium', 'large', 'x-large', or '2x-large'")
    
    # Determine cost per credit based on edition
    if edition_type == "Standard":
        cost_per_credit = 2
    elif edition_type == "Enterprise":
        cost_per_credit = 3
    elif edition_type == "Business Critical":
        cost_per_credit = 4
    else:
        raise ValueError("Invalid Edition type. Please enter the correct edition type")
    data_loading_req = credit_per_hour_dl * no_of_days_dl * no_of_hours_per_day_dl
    data_loading_req_edt = data_loading_req * cost_per_credit
    
    
    total_compute_req = 0
    for _ in range(num_departments):
        dept_name = input("Enter the department name: ")
        warehouse_size_cr = input("Enter the warehouse size (x-small/small/medium/large/x-large/2x-large): ")
        no_of_hours_per_day_cr = int(input(f"Enter the number of hours per day for {dept_name}: "))
        no_of_days_per_month_cr = int(input(f"Enter the number of days per month for {dept_name}: "))
        if warehouse_size_cr == 'x-small':
            credit_per_hour_cr = 1.0
        elif warehouse_size_cr == 'small':
            credit_per_hour_cr = 2.0
        elif warehouse_size_cr == 'medium':
            credit_per_hour_cr = 4.0  
        elif warehouse_size_cr == 'large':
            credit_per_hour_cr = 8.0  
        elif warehouse_size_cr == 'x-large':
            credit_per_hour_cr = 16.0  
        elif warehouse_size_cr == '2x-large':
            credit_per_hour_cr = 32.0
        else:
            raise ValueError("Invalid warehouse size. Please choose 'x-small', 'small', 'medium', 'large', 'x-large', or '2x-large'")
        dept_compute_req = credit_per_hour_cr * no_of_days_per_month_cr * no_of_hours_per_day_cr
        dept_compute_req_edt = dept_compute_req * cost_per_credit
        total_compute_req += dept_compute_req
        department_data.append({'Department Name': dept_name, 'Requirement': dept_compute_req, 'Requirement Edition': dept_compute_req_edt})

    sam_compute_cost_tb =  (data_loading_req + total_compute_req)
    compute_cost_tb = sam_compute_cost_tb * cost_per_credit
    return compute_cost_tb, data_loading_req, data_loading_req_edt

def generate_cost_estimate():
    initial_data_size_tb = float(input("Enter Initial Data Size (TB): "))
    edition_type = input("Enter the edition type(Standard/Enterprise/Business Critical): ")
    warehouse_size_dl = input("Enter Warehouse Size for Data Loading(x-small/small/medium/large/x-large/2x-large): ")
    no_of_days_dl = int(input("Enter Number of Days for Data Loading Req: "))
    no_of_hours_per_day_dl = int(input("Enter Number of Hours per Day for Data Loading Req: "))
    storage_type = input("Enter Storage Type (on-demand/capacity): ")
    no_of_months = int(input("Enter Number of Months for Storage: "))
    num_departments = int(input("Enter the number of departments: "))
    department_data = []
    storage_cost_tb = calculate_storage_cost(initial_data_size_tb, storage_type, no_of_months)
    compute_cost_tb, data_loading_req, data_loading_req_edt = calculate_compute_cost(edition_type, num_departments, warehouse_size_dl, no_of_days_dl, no_of_hours_per_day_dl,department_data)
    total_cost_tb = storage_cost_tb + compute_cost_tb
    cost_df = pd.DataFrame({
        'No of months': no_of_months,
        'Storage Cost (TB)': [storage_cost_tb],
        'Compute Cost (TB)': [compute_cost_tb],
        'Total Annual Cost (TB)': [total_cost_tb]
    })
    compute_req_df = pd.DataFrame(department_data)
    data_loading_df = pd.DataFrame({
        'Department Name': ['Data Loading'],
        'Requirement': [data_loading_req],
        'Requirement Edition': [data_loading_req_edt]
    })
    combined_df = pd.concat([data_loading_df, compute_req_df], ignore_index=True)
    return cost_df,compute_req_df, data_loading_df, combined_df

cost_estimate_df,compute_req_df,data_loading_df, combined_df = generate_cost_estimate()
print(cost_estimate_df.to_string(index=False))
print("\nRequirements:")
print(combined_df.to_string(index=False))


# In[ ]:





# In[ ]:





# In[ ]:




