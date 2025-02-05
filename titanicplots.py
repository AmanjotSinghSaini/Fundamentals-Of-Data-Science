import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(file_path):
    # Load the dataset into a pandas DataFrame
    df = pd.read_csv('/content/titanic.csv')

    # Get the shape of the DataFrame (number of rows and columns)
    rows, columns = df.shape
    print(f"The dataset has {rows} rows, the dataset has {columns} columns.\n")

    # Check for missing values in columns
    missing_columns = df.isnull().sum()
    print("Missing values in each column:")
    print(missing_columns)

    # Calculate the percentage of missing values for each column
    missing_percentage = (missing_columns / rows) * 100
    print("\nPercentage of missing values in each column:")
    print(missing_percentage)


    # Check for missing values in rows
    missing_rows = df.isnull().sum(axis=1)
    print("\nMissing values in each row:")
    print(missing_rows)

    # Show rows with missing values (if any)
    missing_rows_data = df[missing_rows > 0]
    print("\nRows with missing values:")
    print(missing_rows_data)

    # Impute missing values for numerical columns using mean or median
    # Impute missing values for numerical columns using the mean
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for column in numeric_columns:
        if df[column].isnull().sum() > 0:
            # Use mean for numerical columns
            df[column].fillna(df[column].mean(), inplace=True)
            print(f"\nMissing values in {column} were imputed using mean.")

     # Impute missing values for categorical columns using mode
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            # Use mode for categorical columns
            df[column].fillna(df[column].mode()[0], inplace=True)
            print(f"\nMissing values in {column} were imputed using mode.")

    # Check for missing values after imputation
    missing_columns_after_imputation = df.isnull().sum()
    print("\nMissing values after imputation:")
    print(missing_columns_after_imputation)


     # Plot histograms for each numerical column before imputation
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    print("\nPlotting histograms before imputation:")
    for column in numeric_columns:
        plt.figure(figsize=(8, 6))
        df[column].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {column} before imputation')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Plot scatter plots before imputation
    if 'Age' in df.columns and 'Fare' in df.columns:
        plt.figure(figsize=(8, 6))
        df.plot(kind='scatter', x='Age', y='Fare', alpha=0.5, color='orange')
        plt.title('Scatter plot of Age vs Fare before imputation')
        plt.xlabel('Age')
        plt.ylabel('Fare')
        plt.show()

    if 'Pclass' in df.columns and 'Fare' in df.columns:
        plt.figure(figsize=(8, 6))
        df.plot(kind='scatter', x='Pclass', y='Fare', alpha=0.5, color='green')
        plt.title('Scatter plot of Pclass vs Fare before imputation')
        plt.xlabel('Pclass')
        plt.ylabel('Fare')
        plt.show()

    # Impute missing values for numerical columns using mean or median
    for column in numeric_columns:
        if df[column].isnull().sum() > 0:
            df[column].fillna(df[column].mean(), inplace=True)
            print(f"\nMissing values in {column} were imputed using mean.")

    # Impute missing values for categorical columns using mode
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            df[column].fillna(df[column].mode()[0], inplace=True)
            print(f"\nMissing values in {column} were imputed using mode.")

    # Check for missing values after imputation
    missing_columns_after_imputation = df.isnull().sum()
    print("\nMissing values after imputation:")
    print(missing_columns_after_imputation)

    # Calculate the percentage of missing values after imputation
    missing_percentage_after = (missing_columns_after_imputation / rows) * 100
    print("\nPercentage of missing values after imputation:")
    print(missing_percentage_after)

    # Plot histograms for each numerical column after imputation
    print("\nPlotting histograms after imputation:")
    for column in numeric_columns:
        plt.figure(figsize=(8, 6))
        df[column].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {column} after imputation')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Plot scatter plots after imputation
    if 'Age' in df.columns and 'Fare' in df.columns:
        plt.figure(figsize=(8, 6))
        df.plot(kind='scatter', x='Age', y='Fare', alpha=0.5, color='orange')
        plt.title('Scatter plot of Age vs Fare after imputation')
        plt.xlabel('Age')
        plt.ylabel('Fare')
        plt.show()

    if 'Pclass' in df.columns and 'Fare' in df.columns:
        plt.figure(figsize=(8, 6))
        df.plot(kind='scatter', x='Pclass', y='Fare', alpha=0.5, color='green')
        plt.title('Scatter plot of Pclass vs Fare after imputation')
        plt.xlabel('Pclass')
        plt.ylabel('Fare')
        plt.show()

# Example usage:
file_path = 'titanic.csv'  
analyze_data(file_path)