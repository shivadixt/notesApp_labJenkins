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
            environment {
                BUILD_ID = "dontKillMe"
            }
            steps {
                sh '''
                    . venv/bin/activate
                    pkill -f "python app.py" || true
                    sleep 1
                    setsid nohup python app.py > app.log 2>&1 < /dev/null &
                    sleep 2
                    echo "Checking if app started..."
                    ps aux | grep "python app.py" | grep -v grep
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully — app should be live on port 5000.'
        }
        failure {
            echo 'Something failed — check the logs above.'
        }
    }
}
