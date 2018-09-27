# assignment
# max, min, mean age for female
df_female = df[df['Sex'] == 'female']
df_female['Age'].max()
df_female['Age'].min()
df_female['Age'].mean()

# max, min, mean age for male
df_male = df[df['Sex'] == 'male']
df_male['Age'].max()
df_male['Age'].min()
df_male['Age'].mean()

# how many females are there for Pclass
df_male['Pclass'].value_counts()

# how many males are there for Pclass
df_female['Pclass'].value_counts()

# female count based on port
df_female['Embarked'].value_counts()

# male count based on port
df_male['Embarked'].value_counts()