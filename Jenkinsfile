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
    }
}