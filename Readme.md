<a name="br1"></a> 

**Snowﬂake Cost Estimator**

Introduction:

This documentaton provides guidance on using the Snowﬂake Cost Estimator, a Python script designed to calculate the estimated costs 

associated with data storage and computation on the Snowﬂake platorm. The cost estimator includes functions to calculate storage costs, 

compute costs, and generate an overall cost estimate based on user inputs.

Prerequisites:

Before using the Snowﬂake Cost Estimator, ensure the following prerequisites are met:

• Python installed (version 3.9 or higher)

• Knowledge of Snowﬂake edition types and warehouse sizes.

• A clear understanding of the data loading requirements and storage preferences.

Seꢂng Up Snowﬂake Cost Estimator:

To use the Snowﬂake Cost Estimator, follow these steps:

• Open your Python IDE (e.g., PyCharm).

• Install the necessary dependencies by running the following command in the terminal:

**pip install pandas**

Importing necessary libraries:

Pandas library allows to organize and present the cost estimates and requirements in a structured format, making it easier to understand 

and analyse the results.



<a name="br2"></a> 

Estimating Storage and Compute Costs:

1\. Estimating Storage Cost:

The calculate_storage_cost function calculates the storage cost based on the

initial data size, storage type (on-demand or capacity), and the number of

months for which the storage is required.

• Convert the initial data size from the user-speciﬁed unit to terabytes (TB).

• Determine the storage cost based on the storage type.

• For 'on-demand' storage, calculate the cost as the product of data size, a constant factor (40), and the number of months.

• For 'capacity' storage, calculate the cost as the product of data size, a constant factor (23), and the number of months.

• If the provided storage\type is neither 'on-demand' nor 'capacity', a ValueError is raised to choose a valid storage type.

• Return the calculated storage cost.

Variable Description:

initial_data_size_tb: The initial data size in terabytes (TB).

storage_type: The type of storage, either 'on-demand' or 'capacity'.

no_of_months: The number of months for which storage is required.

storage_cost_tb: The estimated total storage cost in terabytes (TB).



<a name="br3"></a> 

2\. Estimating Compute Cost:

The calculate_compute_cost function computes the cost associated with data loading and compute requirements. It considers factors such 

as Snowﬂake edition type, the number of departments, warehouse size for data loading, and the daily and monthly usage of compute 

resources.

Data Loading Requirements:

• Determine the credit per hour based on the speciﬁed warehouse size.

• Determine the cost per credit based on the edition type.

• Calculate the data loading requirements based on the determined credit per hour, number of days, and hours per day for data loading.



<a name="br4"></a> 

Compute Requirements:

• Iterate through each department, asking user for information such as department name, warehouse size, hours per day, and days per month.

• Calculate the compute requirements for each department based on the credit per hour, hours per day, and days per month.

• Calculate the total compute requirements by summing up the individual department requirements.

• Calculate the total compute cost by multiplying the sum of data loading and total compute requirements with the cost per credit.

• Return the calculated compute cost, data loading requirements, and data loading requirements with edition cost.



<a name="br5"></a> 

Variable Description:

edition_type: The edition type, which can be "Standard," "Enterprise," or "Business Critical."

num_departments: The number of departments in the compute requirements.

warehouse_size_dl: The warehouse size for data loading.

no_of_days_dl: The number of days for data loading requirements.

no_of_hours_per_day_dl: The number of hours per day for data loading requirements.

department_data: A list to store department-speciﬁc compute requirements.

compute_cost_tb: The estimated total compute cost.

Estimating Overall Cost:

The generate_cost_estimate function serves as the main entry point for generating a comprehensive cost estimate. It takes user inputs 

for various parameters like initial data size, edition type, warehouse size for data loading, storage type, number of months for storage, 

and department-speciﬁc compute requirements. It combines the results from the storage and compute cost calculations to provide an overall 

cost estimate.

• Utilize the calculate_storage_cost function to estimate the storage cost based on the provided input parameters.

• Utilize the calculate_compute_cost function to estimate the compute cost based on the provided input parameters.

• Sum up the storage cost and compute cost to obtain the total annual cost.

• Create pandas DataFrame to organize and present the cost details in a tabular format.

• Concatenate the Data Loading requirements and Compute requirements.

• Return the DataFrames containing cost estimates and requirements.



<a name="br6"></a> 

• Get all the inputs required from the user.

• The function outputs two DataFrames: costdf containing cost details and combineddf summarizing data loading and compute requirements. 

The results are then displayed in tabular format.



<a name="br7"></a> 

Output:

The output displays a summary of the estimated costs, including storage cost, compute cost, and the total annual cost. Additionally, it 

provides a detailed breakdown of department-speciﬁc data loading and compute requirements.

Conclusion:

The Snowﬂake Cost Estimator provides a valuable tool for users seeking to estimate the ﬁnancial implications of utilizing Snowﬂake for 

data storage and computation. In conclusion, the Snowﬂake Cost Estimator empowers users to make informed decisions regarding resource 

allocation and budgeting within the Snowﬂake platform.

"# Snowflake-Cost-Estimator" 
