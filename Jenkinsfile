pipeline {
    agent any 

        stages {
            stage ('Checkout') {
                steps{
                    checkout scm
                }
            }
            stage('Build'){
                steps{
                    sh 'python3 -m venv venv || echo "Ensure python 3-venv installed in system'

                    sh '''
                    source venv/bin/activate
                    pip install requests
                    '''
                }
            }
        }

    
}