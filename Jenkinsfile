
pipeline{
  agent{
    docker {image 'node:22.11.0-alpine3.20'}
  }
  stages{
    stage('Checkout') {
      steps{
        checkout scm`
      }
    }

    stage('Build') {
      steps {
        echo 'Building Project....'
      }
    }
  }
}



