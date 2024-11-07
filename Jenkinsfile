pipeline{
    agent any

    stages {
        stage('Checkout') {
            steps{
                checkout scm
            }
        }

        stage('Build'){
            steps{
                sh 'python3 -m venv venv'

                sh '''
                . venv/bin/activate
                pip install requests
                '''
            }
        }

        stage ('test'){
            steps{
                sh '''
                . venv/bin/activate

                python -m unittest discover  # or pytest if using pytest
                '''
            }
        }
    }
}