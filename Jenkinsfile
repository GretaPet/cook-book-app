pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
              sh  'bash setup.sh'
            }
        }
        stage('Test') {
            steps {
                sh 'bash test.sh'
            }
        }
        stage('Run') {
            steps {
                sh 'sudo systemctl start application'
            }
        }
    }
}
