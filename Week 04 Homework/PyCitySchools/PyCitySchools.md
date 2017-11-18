

```python
#Import dependencies
import pandas as pd
```


```python
#Read in datasets
schools = pd.read_csv('raw_data/schools_complete.csv')
students = pd.read_csv('raw_data/students_complete.csv')
```


```python
schools.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
students.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
########## District Summary ##########

###########################################################################

#Find the Number of Students
n_schools = len(schools)
n_students = len(students)

print('# of Schools: ' + str(n_schools))
print('# of Students: ' + str(n_students))

###########################################################################

#Find the Total Budget
total_budget = schools['budget'].sum()
print('Total Budget: $' + str(total_budget))

###########################################################################

#Find Average Math and Reading Scores
math_score_avg = students['math_score'].mean()
read_score_avg = students['reading_score'].mean()

print('Avg Math Score: ' + str(math_score_avg))
print('Avg Reading Score: ' + str(read_score_avg))

###########################################################################

# Find the % of students passing Math, Reading, and Overall
# I'm making the cut-off to pass is >= 70 because a cut-off of 60 gives really high passing percentages
# and I wanted to see how the data looks with a lower percentage of passing students

perc_pass_math = len(students.loc[students['math_score'] >= 70]) / n_students * 100
perc_pass_read = len(students.loc[students['reading_score'] >= 70]) / n_students * 100

perc_pass_total = (perc_pass_math + perc_pass_read) / 2

print('% Passing Math: ' + str(round(perc_pass_math, 2)) + '%')
print('% Passing Reading: ' + str(round(perc_pass_read, 2)) + '%')
print('% Passing Overall: ' + str(round(perc_pass_total, 2)) + '%')
```

    # of Schools: 15
    # of Students: 39170
    Total Budget: $24649428
    Avg Math Score: 78.98537145774827
    Avg Reading Score: 81.87784018381414
    % Passing Math: 74.98%
    % Passing Reading: 85.81%
    % Passing Overall: 80.39%
    


```python
#Summary Table
district_summary = pd.DataFrame({'Total Schools':[n_schools],
                                'Total Students':[n_students],
                                'Total Budget':[total_budget],
                                'Average Math Score':[math_score_avg],
                                'Average Reading Score':[read_score_avg],
                                '% Passing Math':[perc_pass_math],
                                '% Passing Reading':[perc_pass_read],
                                '% Passing Overall':[perc_pass_total]
                                })

###########################################################################

#Re-Order Columns
district_summary = district_summary[[
    'Total Schools',
    'Total Students',
    'Total Budget',
    'Average Math Score',
    'Average Reading Score',
    '% Passing Math',
    '% Passing Reading',
    '% Passing Overall'
]]

###########################################################################

#Round values to 4 decimal places
district_summary = district_summary.round(4)
district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Passing Overall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.9854</td>
      <td>81.8778</td>
      <td>74.9809</td>
      <td>85.8055</td>
      <td>80.3932</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create an unformatted dataframe for potential later use
district_summary_basic = district_summary
```


```python
#Re-format District Summary Table
district_summary['Total Schools'] = district_summary['Total Schools'].map("{0:,.0f}".format)
district_summary['Total Students'] = district_summary['Total Students'].map("{0:,.0f}".format)
district_summary['Total Budget'] = district_summary['Total Budget'].map("${0:,.0f}".format)
district_summary['Average Math Score'] = district_summary['Average Math Score'].map("{0:,.2f}%".format)
district_summary['Average Reading Score'] = district_summary['Average Reading Score'].map("{0:,.2f}%".format)
district_summary['% Passing Math'] = district_summary['% Passing Math'].map("{0:,.2f}%".format)
district_summary['% Passing Reading'] = district_summary['% Passing Reading'].map("{0:,.2f}%".format)
district_summary['% Passing Overall'] = district_summary['% Passing Overall'].map("{0:,.2f}%".format)
district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Passing Overall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428</td>
      <td>78.99%</td>
      <td>81.88%</td>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>80.39%</td>
    </tr>
  </tbody>
</table>
</div>




```python
########## Schools Summary ##########

#* Create an overview table that summarizes key metrics about each school, including:
#  * School Name
#  * School Type
#  * Total Students
#  * Total School Budget
#  * Per Student Budget
#  * Average Math Score
#  * Average Reading Score
#  * % Passing Math
#  * % Passing Reading
#  * Overall Passing Rate (Average of the above two)

###########################################################################

# Already have most of the variables in the 'schools' data frame
# We need to calculate the Per Student Budget, average math/reading scores, and % Passing Rates...
# Then add those columns to the original 'schools' df, but rename to 'schools_summary

schools['budget_per_student'] = pd.to_numeric(schools['budget'] / schools['size'])
```


```python
#Calculate Average Math/Reading Score by School
#Need to use the Students df, grouped by school

school_math_avg = pd.DataFrame(students.groupby('school')['math_score'].mean())
school_math_avg.reset_index(inplace = True)

school_read_avg = pd.DataFrame(students.groupby('school')['reading_score'].mean())
school_read_avg.reset_index(inplace = True)
```


```python
#Calculate % of Students passing Math, Reading, and Overarll
#Add binary columns for pass_math, pass_read; 1 = pass, 0 = fail to 'temp' dataframe

#Create a temp table for the students dataframe
#temp_students = students
students['math_pass'] = 0
students['read_pass'] = 0

#students['total_pass'] = 0

#Reset Math/Read Pass variables based on Math/Read Scores
students.loc[students['math_score'] >= 70, 'math_pass'] = 1
students.loc[students['reading_score'] >= 70, 'read_pass'] = 1

#students.loc[(students['math_score'] >= 70) & (students['reading_score'] >= 70), 'total_pass'] = 1
```


```python
# Group the tables by School on math_pass/read_pass
students_tot_math_pass = pd.DataFrame(students.groupby('school')['math_pass'].sum())
students_tot_math_pass.reset_index(inplace = True)

students_tot_read_pass = pd.DataFrame(students.groupby('school')['read_pass'].sum())
students_tot_read_pass.reset_index(inplace = True)

#students_tot_pass = pd.DataFrame(students.groupby('school')['total_pass'].sum())
#students_tot_pass.reset_index(inplace = True)
```


```python
#Rename 'name' column to 'school' in 'school' dataframe
schools = schools.rename(columns={'name':'school'})

#Merge the Average Math & Reading Scores into one table
merged_df = pd.merge(school_math_avg, school_read_avg, on = 'school')

#Merge above with overall School Summary table
school_summary = pd.merge(schools, merged_df, on = 'school')

#Merge the Total # of Math Pass / Reading Pass / Total Pass tables with the overall School Summary Table
school_summary = pd.merge(school_summary, students_tot_math_pass, on = 'school')
school_summary = pd.merge(school_summary, students_tot_read_pass, on = 'school')

#school_summary = pd.merge(school_summary, students_tot_pass, on = 'school')
```


```python
#Create columns for % of Math Pass / % of Read Pass
school_summary['budget_per_student'] = pd.to_numeric(school_summary['budget_per_student'])
school_summary['% Passing Math'] = pd.to_numeric(school_summary['math_pass'] / school_summary['size'] * 100)
school_summary['% Passing Reading'] = pd.to_numeric(school_summary['read_pass'] / school_summary['size'] * 100)
school_summary['% Overall Passing Rate'] = (school_summary['% Passing Math'] + school_summary['% Passing Reading']) / 2

school_summary = school_summary[['school', 'type', 'size', 'budget', 'budget_per_student', 'math_score', 'reading_score',
               '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]
```


```python
#Create an unformatted dataframe for later
school_summary_basic = school_summary
school_summary_basic.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget_per_student</th>
      <th>math_score</th>
      <th>reading_score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>94.860875</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>73.807983</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rename columns
school_summary = school_summary.rename(columns={'school':'School Name',
                                                'type':'School Type',
                                                'size':'Total Students',
                                                'budget':'Total School Budget',
                                                'budget_per_student':'Per Student Budget',
                                                'math_score':'Average Math Score',
                                                'reading_score':'Average Reading Score',
                                               })

#Round numeric columns to 4 decimal places
school_summary = school_summary.round(4)
```


```python
#Reformat Columns
school_summary['Total Students'] = school_summary['Total Students'].map('{0:,.0f}'.format)
school_summary['Total School Budget'] = school_summary['Total School Budget'].map('${0:,.0f}'.format)
school_summary['Per Student Budget'] = school_summary['Per Student Budget'].map('${0:,.2f}'.format)
school_summary['Average Math Score'] = school_summary['Average Math Score'].map('{0:,.2f}'.format)
school_summary['Average Reading Score'] = school_summary['Average Reading Score'].map('{0:,.2f}'.format)
school_summary['% Passing Math'] = school_summary['% Passing Math'].map('{0:,.2f}%'.format)
school_summary['% Passing Reading'] = school_summary['% Passing Reading'].map('{0:,.2f}%'.format)
school_summary['% Overall Passing Rate'] = school_summary['% Overall Passing Rate'].map('{0:,.2f}%'.format)
```


```python
#Sort from highest to lowest % Overall Passing  Rate
school_summary = school_summary.sort_values('% Overall Passing Rate', ascending = False)
#school_summary.reset_index(inplace = True)
school_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1,858</td>
      <td>$1,081,356</td>
      <td>$582.00</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>94.13%</td>
      <td>97.04%</td>
      <td>95.59%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1,635</td>
      <td>$1,043,130</td>
      <td>$638.00</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>93.27%</td>
      <td>97.31%</td>
      <td>95.29%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1,468</td>
      <td>$917,500</td>
      <td>$625.00</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>93.39%</td>
      <td>97.14%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858</td>
      <td>$609.00</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>94.59%</td>
      <td>95.95%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2,283</td>
      <td>$1,319,574</td>
      <td>$578.00</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>93.87%</td>
      <td>96.54%</td>
      <td>95.20%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1,800</td>
      <td>$1,049,400</td>
      <td>$583.00</td>
      <td>83.68</td>
      <td>83.95</td>
      <td>93.33%</td>
      <td>96.61%</td>
      <td>94.97%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1,761</td>
      <td>$1,056,600</td>
      <td>$600.00</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>93.87%</td>
      <td>95.85%</td>
      <td>94.86%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087</td>
      <td>$581.00</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>92.51%</td>
      <td>96.25%</td>
      <td>94.38%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4,976</td>
      <td>$3,124,928</td>
      <td>$628.00</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>66.68%</td>
      <td>81.93%</td>
      <td>74.31%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4,635</td>
      <td>$3,022,020</td>
      <td>$652.00</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>66.75%</td>
      <td>80.86%</td>
      <td>73.81%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2,739</td>
      <td>$1,763,916</td>
      <td>$644.00</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>68.31%</td>
      <td>79.30%</td>
      <td>73.80%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4,761</td>
      <td>$3,094,650</td>
      <td>$650.00</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>66.06%</td>
      <td>81.22%</td>
      <td>73.64%</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2,917</td>
      <td>$1,910,635</td>
      <td>$655.00</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>65.68%</td>
      <td>81.32%</td>
      <td>73.50%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2,949</td>
      <td>$1,884,411</td>
      <td>$639.00</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>65.99%</td>
      <td>80.74%</td>
      <td>73.36%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3,999</td>
      <td>$2,547,363</td>
      <td>$637.00</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>66.37%</td>
      <td>80.22%</td>
      <td>73.29%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a Table of the Top 5 Performing Schools by Overall Passing Rate
schools_top5 = school_summary.head(5)
schools_top5
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1,858</td>
      <td>$1,081,356</td>
      <td>$582.00</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>94.13%</td>
      <td>97.04%</td>
      <td>95.59%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1,635</td>
      <td>$1,043,130</td>
      <td>$638.00</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>93.27%</td>
      <td>97.31%</td>
      <td>95.29%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1,468</td>
      <td>$917,500</td>
      <td>$625.00</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>93.39%</td>
      <td>97.14%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858</td>
      <td>$609.00</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>94.59%</td>
      <td>95.95%</td>
      <td>95.27%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2,283</td>
      <td>$1,319,574</td>
      <td>$578.00</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>93.87%</td>
      <td>96.54%</td>
      <td>95.20%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a Table of the Bottom 5 Performing Schools by Overall Passing Rate
schools_bottom5 = school_summary.tail(5)
schools_bottom5
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2,739</td>
      <td>$1,763,916</td>
      <td>$644.00</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>68.31%</td>
      <td>79.30%</td>
      <td>73.80%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4,761</td>
      <td>$3,094,650</td>
      <td>$650.00</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>66.06%</td>
      <td>81.22%</td>
      <td>73.64%</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2,917</td>
      <td>$1,910,635</td>
      <td>$655.00</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>65.68%</td>
      <td>81.32%</td>
      <td>73.50%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2,949</td>
      <td>$1,884,411</td>
      <td>$639.00</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>65.99%</td>
      <td>80.74%</td>
      <td>73.36%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3,999</td>
      <td>$2,547,363</td>
      <td>$637.00</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>66.37%</td>
      <td>80.22%</td>
      <td>73.29%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Math Scores by Grade**
# Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

# Create separate tables from the students table for each grade level
grade9 = students.loc[students['grade'] == '9th']
grade10 = students.loc[students['grade'] == '10th']
grade11 = students.loc[students['grade'] == '11th']
grade12 = students.loc[students['grade'] == '12th']
```


```python
#Group datasets by school and calculate the average math_score
grade9_math = pd.DataFrame(grade9.groupby('school')['math_score'].mean())
grade9_math.reset_index(inplace = True)
grade9_math = grade9_math.rename(columns = {'math_score':'Grade 9 Math Score'})

grade10_math = pd.DataFrame(grade10.groupby('school')['math_score'].mean())
grade10_math.reset_index(inplace = True)
grade10_math = grade10_math.rename(columns = {'math_score':'Grade 10 Math Score'})

grade11_math = pd.DataFrame(grade11.groupby('school')['math_score'].mean())
grade11_math.reset_index(inplace = True)
grade11_math = grade11_math.rename(columns = {'math_score':'Grade 11 Math Score'})

grade12_math = pd.DataFrame(grade12.groupby('school')['math_score'].mean())
grade12_math.reset_index(inplace = True)
grade12_math = grade12_math.rename(columns = {'math_score':'Grade 12 Math Score'})

```


```python
#Merge data sets on the 'school' variable
temp = pd.merge(grade9_math, grade10_math, on = 'school')
temp = pd.merge(temp, grade11_math, on = 'school')
temp = pd.merge(temp, grade12_math, on = 'school')

math_grades = temp.rename(columns = {'school':'Avg Math Scores',
                                     'Grade 9 Math Score':'Grade 9',
                                    'Grade 10 Math Score':'Grade 10',
                                    'Grade 11 Math Score':'Grade 11',
                                    'Grade 12 Math Score':'Grade 12'
                                    })
```


```python
#Round columns to 4 decimal places
math_grades = math_grades.round(4)
math_grades

#Re-format Columns
math_grades['Grade 9'] = math_grades['Grade 9'].map('{0:,.2f}'.format)
math_grades['Grade 10'] = math_grades['Grade 10'].map('{0:,.2f}'.format)
math_grades['Grade 11'] = math_grades['Grade 11'].map('{0:,.2f}'.format)
math_grades['Grade 12'] = math_grades['Grade 12'].map('{0:,.2f}'.format)

math_grades
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Math Scores</th>
      <th>Grade 9</th>
      <th>Grade 10</th>
      <th>Grade 11</th>
      <th>Grade 12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>77.08</td>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.09</td>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>76.40</td>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>77.36</td>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>82.04</td>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>77.44</td>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.79</td>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>77.03</td>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>77.19</td>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.63</td>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>76.86</td>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.42</td>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.59</td>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.09</td>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.26</td>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading Scores by Grade**
# Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

# Create separate tables from the students table for each grade level
grade9_read = students.loc[students['grade'] == '9th']
grade10_read = students.loc[students['grade'] == '10th']
grade11_read = students.loc[students['grade'] == '11th']
grade12_read = students.loc[students['grade'] == '12th']

grade9_read.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>math_pass</th>
      <th>read_pass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Brittney Walker</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>79</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>William Long</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>71</td>
      <td>79</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Group datasets by school and calculate the average read_score
grade9_read = pd.DataFrame(grade9_read.groupby('school')['reading_score'].mean())
grade9_read.reset_index(inplace = True)
grade9_read = grade9_read.rename(columns = {'reading_score':'Grade 9'})

grade10_read = pd.DataFrame(grade10_read.groupby('school')['reading_score'].mean())
grade10_read.reset_index(inplace = True)
grade10_read = grade10_read.rename(columns = {'reading_score':'Grade 10'})

grade11_read = pd.DataFrame(grade11_read.groupby('school')['reading_score'].mean())
grade11_read.reset_index(inplace = True)
grade11_read = grade11_read.rename(columns = {'reading_score':'Grade 11'})

grade12_read = pd.DataFrame(grade12_read.groupby('school')['reading_score'].mean())
grade12_read.reset_index(inplace = True)
grade12_read = grade12_read.rename(columns = {'reading_score':'Grade 12'})
```


```python
temp2 = pd.merge(grade9_read, grade10_read, on = 'school')
temp2 = pd.merge(temp2, grade11_read, on = 'school')
temp2 = pd.merge(temp2, grade12_read, on = 'school')

reading_grades = temp2.rename(columns = {'school':'Avg Reading Scores'})
reading_grades
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Reading Scores</th>
      <th>Grade 9</th>
      <th>Grade 10</th>
      <th>Grade 11</th>
      <th>Grade 12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Round columns to 4 decimal places
reading_grades = reading_grades.round(4)
reading_grades

#Re-format Columns
reading_grades['Grade 9'] = reading_grades['Grade 9'].map('{0:,.2f}'.format)
reading_grades['Grade 10'] = reading_grades['Grade 10'].map('{0:,.2f}'.format)
reading_grades['Grade 11'] = reading_grades['Grade 11'].map('{0:,.2f}'.format)
reading_grades['Grade 12'] = reading_grades['Grade 12'].map('{0:,.2f}'.format)

reading_grades
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Reading Scores</th>
      <th>Grade 9</th>
      <th>Grade 10</th>
      <th>Grade 11</th>
      <th>Grade 12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.30</td>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.68</td>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.20</td>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.63</td>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.37</td>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.87</td>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.68</td>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.29</td>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>81.26</td>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.81</td>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.99</td>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>84.12</td>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.73</td>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.94</td>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.83</td>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
#**Scores by School Spending**

#* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#  * Average Math Score
#  * Average Reading Score
#  * % Passing Math
#  * % Passing Reading
#  * Overall Passing Rate (Average of the above two)

```


```python
#Recreate school_summary without formatting -- otherwise the binning doesn't work
```


```python
#See the min/max budget per student of the school_summary table to see what reasonable ranges are
print('Min: ' + str(school_summary_basic['budget_per_student'].min()))
print('Max: ' + str(school_summary_basic['budget_per_student'].max()))
```

    Min: 578.0
    Max: 655.0
    


```python
#Create bins
bins = [0, 585, 615, 645, 675]
group_labels = ['$0-$585', '$585-$615','$615-$645','$645-$675']
```


```python
# Place the data series into a new column inside of the DataFrame
school_summary_bins = school_summary_basic
school_summary_bins['budget_category'] = pd.cut(school_summary_basic['budget_per_student'], bins, labels = group_labels)
school_summary_bins.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget_per_student</th>
      <th>math_score</th>
      <th>reading_score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>budget_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
      <td>$645-$675</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
      <td>$615-$645</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>94.860875</td>
      <td>$585-$615</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>73.807983</td>
      <td>$645-$675</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
      <td>$615-$645</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create new data frame
school_spending = school_summary_bins[['budget_category', 
                                       'math_score',
                                       'reading_score',
                                       '% Passing Math',
                                       '% Passing Reading',
                                       '% Overall Passing Rate']]

#Rename columns
school_spending = school_spending.rename(columns = {'budget_category':'Budget Range',
                                     'math_score':'Avg Math Score',
                                    'reading_score':'Avg Reading Score'
                                    })
```


```python
# Create a GroupBy object based upon "budget_category"
school_spending = school_spending.groupby('Budget Range')
school_spending.mean()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Budget Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$0-$585</th>
      <td>83.455399</td>
      <td>83.933814</td>
      <td>93.460096</td>
      <td>96.610877</td>
      <td>95.035486</td>
    </tr>
    <tr>
      <th>$585-$615</th>
      <td>83.599686</td>
      <td>83.885211</td>
      <td>94.230858</td>
      <td>95.900287</td>
      <td>95.065572</td>
    </tr>
    <tr>
      <th>$615-$645</th>
      <td>79.079225</td>
      <td>81.891436</td>
      <td>75.668212</td>
      <td>86.106569</td>
      <td>80.887391</td>
    </tr>
    <tr>
      <th>$645-$675</th>
      <td>76.997210</td>
      <td>81.027843</td>
      <td>66.164813</td>
      <td>81.133951</td>
      <td>73.649382</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Re-format dataframe
#school_spending['Avg Math Score'] = school_spending['Avg Math Score'].map('{0:,.2f}'.format)
#school_spending['Avg Reading Score'] = school_spending['Avg Reading Score'].map('{0:,.2f}'.format)
#school_spendings['Passing Math'] = school_spending['% Passing Math'].map('{0:,.2f}%'.format)
#school_spending['% Passing school_spendingading'] = school_spending['% Passing Reading'].map('{0:,.2f}%'.format)
#school_spending['% Overall Passing Rate'] = school_spending['% Overall Passing Rate'].map('{0:,.2f}%'.format)

#scool_spending
```


```python
#**Scores by School Size**

#* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#  * Average Math Score
#  * Average Reading Score
#  * % Passing Math
#  * % Passing Reading
#  * Overall Passing Rate (Average of the above two)

#See the min/max budget per student of the school_summary table to see what reasonable ranges are
print('Min: ' + str(school_summary_basic['size'].min()))
print('Max: ' + str(school_summary_basic['size'].max()))

#Create bins
bins = [0, 1500, 3000, 4500, 6000]
group_labels = ['0-1500', '1500-3000','3000-4500','4500-6000']

# Place the data series into a new column inside of the DataFrame
school_summary_size = school_summary_basic
school_summary_size['size_bins'] = pd.cut(school_summary_basic['size'], bins, labels = group_labels)
school_summary_size.head()
```

    Min: 427
    Max: 4976
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget_per_student</th>
      <th>math_score</th>
      <th>reading_score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>budget_category</th>
      <th>size_bins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
      <td>$645-$675</td>
      <td>1500-3000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
      <td>$615-$645</td>
      <td>1500-3000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>94.860875</td>
      <td>$585-$615</td>
      <td>1500-3000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>73.807983</td>
      <td>$645-$675</td>
      <td>4500-6000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
      <td>$615-$645</td>
      <td>0-1500</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create new data frame
school_size = school_summary_size[['size_bins', 
                                       'math_score',
                                       'reading_score',
                                       '% Passing Math',
                                       '% Passing Reading',
                                       '% Overall Passing Rate']]

#Rename columns
school_size = school_size.rename(columns = {'size_bins':'Size Range',
                                     'math_score':'Avg Math Score',
                                    'reading_score':'Avg Reading Score'
                                    })
```


```python
# Create a GroupBy object based upon "Size Range"
school_size = school_size.groupby('Size Range')
school_size.mean()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Size Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-1500</th>
      <td>83.664898</td>
      <td>83.892148</td>
      <td>93.497607</td>
      <td>96.445946</td>
      <td>94.971776</td>
    </tr>
    <tr>
      <th>1500-3000</th>
      <td>80.904987</td>
      <td>82.822740</td>
      <td>83.556977</td>
      <td>90.588593</td>
      <td>87.072785</td>
    </tr>
    <tr>
      <th>3000-4500</th>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>4500-6000</th>
      <td>77.136883</td>
      <td>80.978256</td>
      <td>66.496861</td>
      <td>81.339570</td>
      <td>73.918215</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_summary_basic.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget_per_student</th>
      <th>math_score</th>
      <th>reading_score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>budget_category</th>
      <th>size_bins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
      <td>$645-$675</td>
      <td>1500-3000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
      <td>$615-$645</td>
      <td>1500-3000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>94.860875</td>
      <td>$585-$615</td>
      <td>1500-3000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>73.807983</td>
      <td>$645-$675</td>
      <td>4500-6000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
      <td>$615-$645</td>
      <td>0-1500</td>
    </tr>
  </tbody>
</table>
</div>




```python
#**Scores by School Type**

#* Create a table that breaks down school performances based on School Type (District, Charter).
#  Include in the table each of the following:
#  * Average Math Score
#  * Average Reading Score
#  * % Passing Math
#  * % Passing Reading
#  * Overall Passing Rate (Average of the above two)

#Create new data frame
school_type = school_summary_basic[['type', 'size', 'budget_per_student',
                                       'math_score',
                                       'reading_score',
                                       '% Passing Math',
                                       '% Passing Reading',
                                       '% Overall Passing Rate']]

#Rename columns
school_type = school_type.rename(columns = {'type':'School Type', 'size':'School Size',
                                            'budget_per_student':'Per Student Budget',
                                     'math_score':'Avg Math Score',
                                    'reading_score':'Avg Reading Score'
                                    })
```


```python
# Create a GroupBy object based on "School Type"
school_type = school_type.groupby('School Type')
school_type.mean()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Per Student Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>1524.250000</td>
      <td>599.500000</td>
      <td>83.473852</td>
      <td>83.896421</td>
      <td>93.620830</td>
      <td>96.586489</td>
      <td>95.103660</td>
    </tr>
    <tr>
      <th>District</th>
      <td>3853.714286</td>
      <td>643.571429</td>
      <td>76.956733</td>
      <td>80.966636</td>
      <td>66.548453</td>
      <td>80.799062</td>
      <td>73.673757</td>
    </tr>
  </tbody>
</table>
</div>




```python
##### Three Observable Trends #####

# 1.a) Of the 15 schools in the district, the top 8 by % Overall Passing Rate are the Charter Schools, while the bottom 7 are all District Schools
# 1.b) Passing rates are significantly higher overall for Charter Schools vs. District Schools.
#      No charter school has an overall passing rate lower than 94%, while no district school has a passing rate above 74%

# 2.0) Charter Schools have almost twice as many students as the district schools on average

# 3.0) However, the average budget per student is over $43 higher at district schools compared to charter schools.
#      As such, it appears that there is no relationship between student performance and the school's budget in this data set.

```
