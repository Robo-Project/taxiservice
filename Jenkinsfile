pipeline {
  parameters {
      string(name: 'SEARCH', defaultValue: 'Robot', description: 'Search wikipedia')
    }
  agent any
  stages {
    stage('setup') {
      steps {
          sh "rm -rf data"
          sh "mkdir data"
      }
    }
    stage('build and run') {
      steps {
       sh "docker run --rm \
        -v `pwd`/data:/opt/robotframework/reports:Z \
        -v `pwd`/tasks:/opt/robotframework/tests:Z \
        -e ROBOT_OPTIONS='--variable SEARCH:${SEARCH}' \
        ppodgorsek/robot-framework"
      }
    }
   stage('dbbot') {
      steps {
	      sh "python3 -m dbbot.run \
	      -b postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@172.17.0.1:5432/${POSTGRES_DB} \
	      -k `pwd`/data/output.xml"
      }
    }
  }
  post {
    always {
      robot outputPath: 'data/'
      sh "rm -r data"
    }
  }
}

