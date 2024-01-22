pipeline{
    agent any
    stages{
        steps('Build'){
            step{
                echo "Etapa Build no disponible"
            }
        }
        steps('Tests'){
            step{
                echo "Etapa Test no disponible"
            }
        }
        {
            steps('Deploy'){
                step{
                    sh "docker-compose down -v"
                    sh "docker-compose up -d --build"

                }
            }
        }
    }

}