pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Etapa Build no disponible"
            }
        }
        stage('Tests') {
            steps {
                echo "Etapa Test no disponible"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker-compose down -v"
                sh "docker-compose up -d --build"
            }
        }
    }
}
