pipeline {
    agent any

    stages {
        stage('Convert CSV to Parquet') {
            steps {
                script {
                    // code to convert CSV to Parquet is here
                    // import necessary libraries
                    def pandas = sh(script: 'pip install pandas', returnStdout: true).trim()
                    def fastparquet = sh(script: 'pip install fastparquet', returnStdout: true).trim()

                    // set file paths
                    def csv_file = 'hrdata.csv'
                    def parquet_file = 'hrdata.parquet'

                    // read CSV file into a pandas DataFrame
                    def df = pandas.read_csv(csv_file)

                    // write DataFrame to Parquet file
                    df.to_parquet(parquet_file)
                }
            }
        }
    }
}
