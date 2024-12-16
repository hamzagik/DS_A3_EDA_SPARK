Netflix EDA with Apache Spark
Project Overview
This project involves performing exploratory data analysis (EDA) on the Netflix dataset using Apache Spark. The dataset contains information about Netflix movies and TV shows, including attributes like title, release year, type (movie or TV show), genres, ratings, etc. The goal is to process and analyze this large dataset efficiently using Spark to uncover insights about the content on Netflix.

Project Contents
netflix_titles.csv: The main dataset containing information about Netflix content (movies and TV shows).
credits.csv: Dataset with information about the cast and crew of the shows/movies.
netflix_eda.py: The main PySpark script for performing the exploratory data analysis.
Dockerfile: The Docker configuration file (if applicable).
README.md: This documentation file.
Technologies Used
Apache Spark (for distributed data processing)
Python (for PySpark scripting)
Docker (for containerized environment)
Setup Instructions
To run this project, follow the instructions below.

Prerequisites
Docker: Ensure Docker is installed on your machine. Follow the installation guide for your operating system from the official Docker website.
Apache Spark: This project uses Spark in a Docker container, so there’s no need for local installation of Spark.
Python: Make sure Python 3.6+ is installed, as the project is based on PySpark.
Running with Docker
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/netflix-eda-spark.git
cd netflix-eda-spark
Build and run the Docker container:

If using the default apache/spark-py image, run:
bash
Copy code
docker run -it --rm -p 4040:4040 -v ${PWD}:/app apache/spark-py bash
If using a full Apache Spark image, you can try:
bash
Copy code
docker pull apache/spark:3.3.1
docker run -it --rm -p 4040:4040 -v ${PWD}:/app apache/spark:3.3.1 bash
Run the PySpark script: Inside the Docker container, run:

bash
Copy code
spark-submit /app/netflix_eda.py
This will execute the analysis, and you should see the results in the terminal or Spark UI (accessible via http://localhost:4040).
