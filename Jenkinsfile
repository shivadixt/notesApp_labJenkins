pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:shivadixt/notesApp_labJenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    . venv/bin/activate
                    pkill -f "python app.py" || true
                    nohup python app.py > app.log 2>&1 &
                    sleep 2
                '''
            }
        }
    }

    post {
        success {
            echo 'Tests passed! Pipeline completed successfully.'
        }
        failure {
            echo 'Something failed — check the logs above.'
        }
    }
}
