# Pydocker
Python docker test 

Steps:

Create a Dockerfile to define the environment and dependencies for  Streamlit app.
Build the Docker image.
Run a container from the Docker image.



to build the docker image :
docker build -t streamlit-app .

Run the container 
docker run -d -p 8501:8501 --name streamlit-container streamlit-app
