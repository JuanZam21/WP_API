pipeline{
    agent any
    stages{
        stage('Build'){
            step{
                echo "Etapa Build no disponible"
            }
        }
        stage('Tests'){
            step{
                echo "Etapa Test no disponible"
            }
        }
        {
            stage('Deploy'){
                step{
                    sh "docker-compose down -v"
                    sh "docker-compose up -d --build"

                }
            }
        }
    }

}