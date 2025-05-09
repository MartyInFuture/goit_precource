import pandas as pd
import matplotlib.pyplot as plt

students_data = {
    'Name': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Maria', 'Petro', 'Sophia', 'Max', 'Natalia', 'Vadym'],
    'Age': [21, 22, 20, 19, 23, 22, 21, 20, 19, 21],
    'Subject': ['Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)
print(students_df)

print('-------------------------')
older_students = students_df[students_df['Age'] > 22]
print(older_students)

students_df.plot(x = 'Name', y = 'Age', kind='bar')
plt.show()