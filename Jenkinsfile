pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'python3 -m pip install --user requests'
                
            }
        }

        stage('Test') {

            steps{
                echo 'Running Test Stage'
                sh 'python3 main.py'
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    
                    withSonarQubeEnv('Sonar-scanner-1') {  // Ensure 'SonarQube' matches your Jenkins setup
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
    }
}
