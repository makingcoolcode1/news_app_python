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
                sh 'apt install python3-requests'
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
