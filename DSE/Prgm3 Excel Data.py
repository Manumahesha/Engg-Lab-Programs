import pandas as pd
df=pd.read_excel(r'D:\employee.xlsx')

print("first few rows:")
print(df.head())

print("\n summary statistics:")
print(df.describe())

filtered_data=df[df['Age']>30]
print("\n filtered dt(Age>30):")
print(filtered_data)

sorted_data=df.sort_values(by='Annual Salary',ascending=False)
print("\n sorted data(by salary):")
print(sorted_data)

df['Bonus']=df['Annual Salary']*0.1
print("\n data with new column(Bonus):")
df.to_excel('output.xlsx',index=False)
print("\n data written to output.xlsx")

//output
first few rows:
     EEID        Full Name                 Job Title Department  \
0  E02387      Emily Davis                Sr. Manger         IT   
1  E04105    Theodore Dinh       Technical Architect         IT   
2  E02572     Luna Sanders                  Director    Finance   
3  E02832  Penelope Jordan  Computer Systems Manager         IT   
4  E01639        Austin Vo               Sr. Analyst    Finance   

            Business Unit  Gender  Ethnicity  Age  Hire Date  Annual Salary  \
0  Research & Development  Female      Black   55 2016-04-08         141604   
1           Manufacturing    Male      Asian   59 1997-11-29          99975   
2     Speciality Products  Female  Caucasian   50 2006-10-26         163099   
3           Manufacturing  Female  Caucasian   26 2019-09-27          84913   
4           Manufacturing    Male      Asian   55 1995-11-20          95409   

   Bonus %        Country       City  Exit Date  
0     0.15  United States    Seattle 2021-10-16  
1     0.00          China  Chongqing        NaT  
2     0.20  United States    Chicago        NaT  
3     0.07  United States    Chicago        NaT  
4     0.00  United States    Phoenix        NaT  

 summary statistics:
               Age  Annual Salary      Bonus %
count  1000.000000    1000.000000  1000.000000
mean     44.382000  113217.365000     0.088660
std      11.246981   53545.985644     0.117856
min      25.000000   40063.000000     0.000000
25%      35.000000   71430.250000     0.000000
50%      45.000000   96557.000000     0.000000
75%      54.000000  150782.250000     0.150000
max      65.000000  258498.000000     0.400000

 filtered dt(Age>30):
       EEID      Full Name               Job Title  Department  \
0    E02387    Emily Davis              Sr. Manger          IT   
1    E04105  Theodore Dinh     Technical Architect          IT   
2    E02572   Luna Sanders                Director     Finance   
4    E01639      Austin Vo             Sr. Analyst     Finance   
5    E00644   Joshua Gupta  Account Representative       Sales   
..      ...            ...                     ...         ...   
995  E03094   Wesley Young             Sr. Analyst   Marketing   
996  E01909   Lillian Khan                 Analyst     Finance   
997  E04398    Oliver Yang                Director   Marketing   
998  E02521    Lily Nguyen             Sr. Analyst     Finance   
999  E03545    Sofia Cheng          Vice President  Accounting   

              Business Unit  Gender  Ethnicity  Age  Hire Date  Annual Salary  \
0    Research & Development  Female      Black   55 2016-04-08         141604   
1             Manufacturing    Male      Asian   59 1997-11-29          99975   
2       Speciality Products  Female  Caucasian   50 2006-10-26         163099   
4             Manufacturing    Male      Asian   55 1995-11-20          95409   
5                 Corporate    Male      Asian   57 2017-01-24          50994   
..                      ...     ...        ...  ...        ...            ...   
995     Speciality Products    Male  Caucasian   33 2016-09-18          98427   
996     Speciality Products  Female      Asian   44 2010-05-31          47387   
997     Speciality Products    Male      Asian   31 2019-06-10         176710   
998     Speciality Products  Female      Asian   33 2012-01-28          95960   
999               Corporate  Female      Asian   63 2020-07-26         216195   

     Bonus %        Country       City  Exit Date  
0       0.15  United States    Seattle 2021-10-16  
1       0.00          China  Chongqing        NaT  
2       0.20  United States    Chicago        NaT  
4       0.00  United States    Phoenix        NaT  
5       0.00          China  Chongqing        NaT  
..       ...            ...        ...        ...  
995     0.00  United States   Columbus        NaT  
996     0.00          China    Chengdu 2018-01-08  
997     0.15  United States      Miami        NaT  
998     0.00          China    Chengdu        NaT  
999     0.31  United States      Miami        NaT  

[850 rows x 14 columns]

 sorted data(by salary):
       EEID     Full Name        Job Title  Department  \
989  E04354  Raelynn Rios   Vice President       Sales   
232  E04742  Kinsley Vega   Vice President  Accounting   
900  E02522  Silas Rivera   Vice President       Sales   
549  E01371    Dominic Le   Vice President   Marketing   
610  E04170  Grayson Chin   Vice President          IT   
..      ...           ...              ...         ...   
787  E02732    Alice Tran          Analyst   Marketing   
182  E03719    Jack Brown          Analyst   Marketing   
823  E00862   Levi Moreno  Systems Analyst          IT   
782  E04109   Leah Bryant   IT Coordinator          IT   
781  E03928    Miles Dang   IT Coordinator          IT   

              Business Unit  Gender  Ethnicity  Age  Hire Date  Annual Salary  \
989           Manufacturing  Female     Latino   43 2016-08-21         258498   
232               Corporate  Female     Latino   33 2020-12-16         258426   
900               Corporate    Male     Latino   48 2000-02-28         258081   
549               Corporate    Male      Asian   41 2014-10-04         257194   
610  Research & Development    Male      Asian   26 2020-05-09         256561   
..                      ...     ...        ...  ...        ...            ...   
787               Corporate  Female      Asian   39 2014-07-29          40897   
182               Corporate    Male  Caucasian   55 2004-12-07          40752   
823  Research & Development    Male     Latino   64 2020-06-27          40316   
782           Manufacturing  Female  Caucasian   55 2004-04-30          40124   
781     Speciality Products    Male      Asian   61 2000-09-24          40063   

     Bonus %        Country            City Exit Date  
989     0.35  United States        Columbus       NaT  
232     0.40         Brazil  Rio de Janerio       NaT  
900     0.30  United States         Chicago       NaT  
549     0.35          China       Chongqing       NaT  
610     0.39  United States          Austin       NaT  
..       ...            ...             ...       ...  
787     0.00  United States         Seattle       NaT  
182     0.00  United States         Phoenix       NaT  
823     0.00         Brazil          Manaus       NaT  
782     0.00  United States          Austin       NaT  
781     0.00  United States           Miami       NaT  

[1000 rows x 14 columns]

 data with new column(Bonus):

data written to output.xlsx
