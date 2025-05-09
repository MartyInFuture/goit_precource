import pandas as pd

poll = pd.read_csv('pandas/2017_jun_final.csv')

print(poll.head())
print('-------------------------')
print(poll.shape)
print('-------------------------')
print(poll.dtypes)
print('-------------------------')
print((poll.isnull().sum() / len(poll)).round(2) * 100)
print('-------------------------')

# Зберігаємо тільки стовпці без пропусків або названий "Мова.програмування"
cleaned_poll = poll.loc[:, (poll.columns == 'Язык.программирования') | (~poll.isnull().any())]

print((cleaned_poll.isnull().sum() / len(cleaned_poll)).round(2) * 100)
print('-------------------------')
print(cleaned_poll.shape)
print('-------------------------')  
poll_no_missing = cleaned_poll.dropna()
print(poll_no_missing.shape)
print('-------------------------')

only_python = poll_no_missing[poll_no_missing['Язык.программирования'] == 'Python']
print(only_python.shape)
print('-------------------------')
salary_stats = poll.groupby('Должность')['Зарплата.в.месяц'].agg(['min', 'max'])
print(salary_stats)

print('-------------------------')  

def fill_avg_salary(row):
  return (row['min'] + row['max']) / 2

print(fill_avg_salary(salary_stats.loc['Project manager']))

salary_stats['avg'] = salary_stats.apply(fill_avg_salary, axis=1)
print('-------------------------')
print(salary_stats)
print('-------------------------')
print(salary_stats["avg"].describe())

# salary_stats.to_csv('pandas/salary_stats.csv')

test = pd.read_csv('pandas/salary_stats.csv')
print(test.shape)

