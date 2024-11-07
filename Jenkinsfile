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
                source venv/bin/activate
                pip install requests
                '''
            }
        }
    }
}