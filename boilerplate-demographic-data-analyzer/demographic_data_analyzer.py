import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = round(df_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bach = df[df['education'] == 'Bachelors']
    bach_ratio = df_bach.shape[0] / df.shape[0]
    percentage_bachelors = round(bach_ratio * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    df_high = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    df_low = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]

    higher_education = df_high.shape[0]
    lower_education = df_low.shape[0]
    
    df_high_rich = df_high[df_high['salary'] == '>50K']
    df_low_rich = df_low[df_low['salary'] == '>50K']
    
    high_rich_ratio = df_high_rich.shape[0] / higher_education
    low_rich_ratio = df_low_rich.shape[0] / lower_education

    higher_education_rich = round(high_rich_ratio * 100, 1)
    lower_education_rich = round(low_rich_ratio * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_minwork = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = df_minwork.shape[0]
    
    df_minwork_rich = df_minwork[df_minwork['salary'] == '>50K']

    minwork_rich_ratio = df_minwork_rich.shape[0] / num_min_workers
    
    rich_percentage = round(minwork_rich_ratio * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    df_rich = df[df['salary'] == '>50K']
    rich_country_count = df_rich['native-country'].value_counts()
    highest_ratio = 0
    highest_country = ''
    for i1, v1 in country_count.items():
      for i2, v2 in rich_country_count.items():
        if i1 == i2:
          ratio = v2 / v1
          if ratio > highest_ratio:
            highest_ratio = ratio
            highest_country = i1
    
    highest_earning_country = highest_country
    highest_earning_country_percentage = round(highest_ratio * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_india = df[df['native-country'] == 'India']
    df_india_rich = df_india[df_india['salary'] == '>50K']
    occupations = df_india_rich['occupation']
    top_IN_occupation = occupations.value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
