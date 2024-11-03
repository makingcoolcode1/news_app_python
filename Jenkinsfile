pipeline {
    agent any 
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover'  // Replace with your testing command
            }
        }
        stage('Build') {
            steps {
                sh 'python setup.py build'  // Replace with your build command
            }
        }
    }
}
