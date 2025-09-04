import pandas as pd

data = {
    'Employee': ['John', 'Emma', 'Oliver'],
    'Department': ['HR', 'Finance', 'IT'],
    'Salary': [50000, 70000, 60000],
    'Age': [28, 34, 29]
}
df = pd.DataFrame(data)

df['Bonus'] = df['Salary'] * 0.1
df = df.drop(columns=['Age'])

new_row = pd.DataFrame([{'Employee': 'Sophia', 'Department': 'Marketing', 'Salary': 65000, 'Bonus': 6500}])
df = pd.concat([df, new_row], ignore_index=True)

df = df.drop(index=0)
df = df.drop(columns=['Bonus'])

print(df)
