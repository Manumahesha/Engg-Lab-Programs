import pandas as pd
data={
    'Name':['John','Emma','Ram','Lisa','Tom'],
    'Age':[25,30,28,32,27],
    'Country':['USA','Canada','India','UK','Australia'],
    'Salary':[50000,60000,70000,80000,65000]
}

df=pd.DataFrame(data)
print("Original DataFrame")
print(df)

name_age=df[['Name','Age']]
print("Original DataFrame")    
print(df)
name_age=df[['Name','Age']]
print("Name and Age columns")
print(name_age)
      
      
filtered_df=df[df['Country']=='USA']      
print("\nfiltered DataFrame(Country='USA')")      
print(filtered_df)

sorted_df=df.sort_values("Salary",ascending=False)
print("\nsorted DataFrame(by salary in descending order)")
print(sorted_df)
average_Salary=df['Salary'].mean()

print("\nAverage salary",average_Salary)


df['Experience']=[3,6,4,8,5]
print("\nDataFrame with added experience")
print(df)
df.loc[df['Name']=='Emma','Salary']=65000
print("\nDataFrame with updating emma salary")
print(df)


df.drop('Experience',axis=1)
print("\nDataFrame after deleting the column ")
print(df)


----------------------------------------------------------------------------
  OUTPUT:-


  Original DataFrame
   Name  Age    Country  Salary
0  John   25        USA   50000
1  Emma   30     Canada   60000
2  Sant   28      India   70000
3  Lisa   32         UK   80000
4   Tom   27  Australia   65000
Original DataFrame
   Name  Age    Country  Salary
0  John   25        USA   50000
1  Emma   30     Canada   60000
2  Sant   28      India   70000
3  Lisa   32         UK   80000
4   Tom   27  Australia   65000
Name and Age columns
   Name  Age
0  John   25
1  Emma   30
2  Sant   28
3  Lisa   32
4   Tom   27

filtered DataFrame(Country='USA')
   Name  Age Country  Salary
0  John   25     USA   50000

sorted DataFrame(by ssalary in descending order)
   Name  Age    Country  Salary
3  Lisa   32         UK   80000
2  Sant   28      India   70000
4   Tom   27  Australia   65000
1  Emma   30     Canada   60000
0  John   25        USA   50000

Average salary 65000.0

DataFrame with added experience
   Name  Age    Country  Salary  Experience
0  John   25        USA   50000           3
1  Emma   30     Canada   60000           6
2  Sant   28      India   70000           4
3  Lisa   32         UK   80000           8
4   Tom   27  Australia   65000           5

DataFrame with updating emma salary
   Name  Age    Country  Salary  Experience
0  John   25        USA   50000           3
1  Emma   30     Canada   65000           6
2  Sant   28      India   70000           4
3  Lisa   32         UK   80000           8
4   Tom   27  Australia   65000           5

DataFrame after deleting the column 
   Name  Age    Country  Salary  Experience
0  John   25        USA   50000           3
1  Emma   30     Canada   65000           6
2  Sant   28      India   70000           4
3  Lisa   32         UK   80000           8
4   Tom   27  Australia   65000           5
​
