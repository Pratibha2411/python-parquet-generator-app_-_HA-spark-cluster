pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install pandas'
            }
        }

        stage('Convert CSV to Parquet') {
            steps {
                // code to convert CSV to Parquet is here
                // # import fastparquet as fp #in case if fastparquet doesn't work

                // # Set file paths
                csv_file = 'hrdata.csv'
                parquet_file = 'hrdata.parquet'

                // # Read CSV file into a pandas DataFrame
                df = pd.read_csv(csv_file)

                // # Write DataFrame to Parquet file
                df.to_parquet(parquet_file)
            }
        }

    // add more stages as needed
    }
}
