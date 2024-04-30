# Use the official Python image as a base
FROM python:3.9-slim

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true

# Install system dependencies
RUN apt-get update && \
    apt-get install -y sudo

# Install required Python packages
RUN pip install streamlit

# Create a non-root user
RUN groupadd -r streamlit && useradd -r -g streamlit streamlit

# Set up sudo for non-root user without password
RUN echo "streamlit ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY app.py /app/app.py

# Change ownership of the application files to the non-root user
RUN chown -R streamlit:streamlit /app

# Switch to non-root user
USER streamlit

# Expose the Streamlit port
EXPOSE $STREAMLIT_SERVER_PORT

# Command to run the Streamlit app
CMD ["streamlit", "run", "--server.port=$STREAMLIT_SERVER_PORT", "--server.headless=$STREAMLIT_SERVER_HEADLESS", "app.py"]
