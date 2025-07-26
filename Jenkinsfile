pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/shreya-singh27/Automated-docker-builds-with-jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-app-image .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker rm -f flask-app || true'
                    sh 'docker run -d --name flask-app -p 5000:5000 flask-app-image'
                }
            }
        }
    }
}
