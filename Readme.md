<a name="br1"></a> 

**Snowﬂake Cost Esꢀmator**

Introducꢀon:

This documentaꢀon provides guidance on using the Snowﬂake Cost Esꢀmator,

a Python script designed to calculate the esꢀmated costs associated with data

storage and computaꢀon on the Snowﬂake plaꢁorm. The cost esꢀmator

includes funcꢀons to calculate storage costs, compute costs, and generate an

overall cost esꢀmate based on user inputs.

Prerequisites:

Before using the Snowﬂake Cost Esꢀmator, ensure the following prerequisites

are met:

• Python installed (version 3.9 or higher)

• Knowledge of Snowﬂake ediꢀon types and warehouse sizes.

• A clear understanding of the data loading requirements and storage

preferences.

Seꢂng Up Snowﬂake Cost Esꢀmator:

To use the Snowﬂake Cost Esꢀmator, follow these steps:

• Open your Python IDE (e.g., PyCharm).

• Install the necessary dependencies by running the following command in

the terminal:

**pip install pandas**

Imporꢀng necessary libraries:

Pandas library allows to organize and present the cost esꢀmates and

requirements in a structured format, making it easier to understand and

analyse the results.



<a name="br2"></a> 

Esꢀmaꢀng Storage and Compute Costs:

1\. Esꢀmaꢀng Storage Cost:

The calculate\_storage\_cost funcꢀon calculates the storage cost based on the

iniꢀal data size, storage type (on-demand or capacity), and the number of

months for which the storage is required.

• Convert the iniꢀal data size from the user-speciﬁed unit to terabytes

(TB).

• Determine the storage cost based on the storage type.

• For 'on-demand' storage, calculate the cost as the product of data size, a

constant factor (40), and the number of months.

• For 'capacity' storage, calculate the cost as the product of data size, a

constant factor (23), and the number of months.

• If the provided storage\_type is neither 'on-demand' nor 'capacity', a

ValueError is raised to choose a valid storage type.

• Return the calculated storage cost.

Variable Descripꢀon:

iniꢀal\_data\_size\_tb: The iniꢀal data size in terabytes (TB).

storage\_type: The type of storage, either 'on-demand' or 'capacity'.

no\_of\_months: The number of months for which storage is required.

storage\_cost\_tb: The esꢀmated total storage cost in terabytes (TB).



<a name="br3"></a> 

2\. Esꢀmaꢀng Compute Cost:

The calculate\_compute\_cost funcꢀon computes the cost associated with data

loading and compute requirements. It considers factors such as Snowﬂake

ediꢀon type, the number of departments, warehouse size for data loading, and

the daily and monthly usage of compute resources.

Data Loading Requirements:

• Determine the credit per hour based on the speciﬁed warehouse size.

• Determine the cost per credit based on the ediꢀon type.

• Calculate the data loading requirements based on the determined credit

per hour, number of days, and hours per day for data loading.



<a name="br4"></a> 

Compute Requirements:

• Iterate through each department, asking the user for informaꢀon such as

department name, warehouse size, hours per day, and days per month.

• Calculate the compute requirements for each department based on the

credit per hour, hours per day, and days per month.

• Calculate the total compute requirements by summing up the individual

department requirements.

• Calculate the total compute cost by mulꢀplying the sum of data loading

and total compute requirements with the cost per credit.

• Return the calculated compute cost, data loading requirements, and data

loading requirements with ediꢀon cost.



<a name="br5"></a> 

Variable Descripꢀon:

ediꢀon\_type: The ediꢀon type, which can be "Standard," "Enterprise," or

"Business Criꢀcal."

num\_departments: The number of departments in the compute requirements.

warehouse\_size\_dl: The warehouse size for data loading.

no\_of\_days\_dl: The number of days for data loading requirements.

no\_of\_hours\_per\_day\_dl: The number of hours per day for data loading

requirements.

department\_data: A list to store department-speciﬁc compute requirements.

compute\_cost\_tb: The esꢀmated total compute cost.

Esꢀmaꢀng Overall Cost:

The generate\_cost\_esꢀmate funcꢀon serves as the main entry point for

generaꢀng a comprehensive cost esꢀmate. It takes user inputs for various

parameters like iniꢀal data size, ediꢀon type, warehouse size for data loading,

storage type, number of months for storage, and department-speciﬁc compute

requirements. It combines the results from the storage and compute cost

calculaꢀons to provide an overall cost esꢀmate.

• Uꢀlize the calculate\_storage\_cost funcꢀon to esꢀmate the storage cost

based on the provided input parameters.

• Uꢀlize the calculate\_compute\_cost funcꢀon to esꢀmate the compute

cost based on the provided input parameters.

• Sum up the storage cost and compute cost to obtain the total annual

cost.

• Create pandas DataFrame to organize and present the cost details in a

tabular format.

• Concatenate the Data Loading requirements and Compute requirements

DataFrames to create a combined summary DataFrame.

• Return the DataFrames containing cost esꢀmates and requirements.



<a name="br6"></a> 

• Get all the inputs required from the user.

The funcꢀon outputs two DataFrames: cost\_df containing cost details and

combined\_df summarizing data loading and compute requirements. The

results are then displayed in tabular format.



<a name="br7"></a> 

Sample Input:

Output:

The output displays a summary of the esꢀmated costs, including storage cost,

compute cost, and the total annual cost. Addiꢀonally, it provides a detailed

breakdown of department-speciﬁc data loading and compute requirements.

Conclusion:

The Snowﬂake Cost Esꢀmator provides a valuable tool for users seeking to

esꢀmate the ﬁnancial implicaꢀons of uꢀlizing Snowﬂake for data storage and

computaꢀon. In conclusion, the Snowﬂake Cost Esꢀmator empowers users to

make informed decisions regarding resource allocaꢀon and budgeꢀng within

the Snowﬂake plaꢁorm.

"# Snowflake-Cost-Estimator" 
