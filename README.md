docker run -v $(pwd)/data:/opt/robotframework/reports:Z -v $(pwd)/tasks:/opt/robotframework/tests:Z -v $(pwd)/pythonscripts:/opt/robotframework/pythonscripts/ ppodgorsek/robot-framework:latest
