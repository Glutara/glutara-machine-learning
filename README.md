<div align="center"><img src = "assets/glutara.png" width = 20% height= 20%></div>

<div align="center">
An IOT-based system with non-invasive wearable Continuous Glucose Monitor (CGM) for diabetic people
</div>

## Table of Contents

- [App Overview](#app-overview)
- [Prerequisite](#prerequisite)
- [How to Run](#how-to-run)
- [Team](#team)

## App Overview
Millions of individuals worldwide grapple with the relentless challenges of managing diabetes, a chronic condition that demands consistent monitoring and care. Despite the advancements in technology, the process remains burdensome, with traditional finger-pricking glucose monitoring causing discomfort and hindering regular monitoring. This issue is exacerbated for those leading busy lives, leaving little time for necessary health measures. The fear of potential health emergencies, particularly for individuals living alone, further
compounds the need for a more accessible and painless solution. Glutara aims to revolutionize
blood glucose monitoring by offering a seamless and affordable solution, addressing the
fundamental challenges faced by those managing diabetes on a daily basis.

This repository is dedicated to manage the code needed to create, train, and serve the machine learning algorithm model used by Glutara to determine the blood sugar levels.

## Prerequisite
Make sure you already do these things before running the code
1. Install Python languange on your computer
2. Install the package you need to run the code (pandas, numpy, tensorflow) using this following command
    ``` bash
    pip install pandas numpy tensorflow
    ```
3. Install Docker on your computer
4. Download the Tensorflow Serving image to Docker using this following command
    ``` bash
    docker pull tensorflow/serving
    ```

## How to Run
On this example of how to run, we will use the port 8605 to host Tensorflow Serving 
1. Clone this repository from terminal using this following command
    ``` bash
    git clone https://github.com/Glutara/glutara-machine-learning.git
    ```
2. There should be some model files inside tensorflow_model/1 directory. But if not, then navigate to src directory and execute this command to save the model. Skip this step if the model is already present
    ``` bash
    python main.py
    ```
3. After saving the model, open your terminal and create a Docker container using this following command
    ``` bash
    docker run -it -v path/to/repository/directory:/glutara-machine-learning -p 8605:8605 --entrypoint /bin/bash tensorflow/serving
    ```
    Executing this command should also open the container command line
4. Run Tensorflow Serving by using this following command inside the container command line
    ``` bash
    tensorflow_model_server --rest_api_port=8605 --model_name=glutara_model --model_base_path=/glutara-machine-learning/tensorflow_model
    ```
5. The Tensorflow Serving should be running and ready to respond to inference request. You can also check the serving by opening
   http://localhost:8605/v1/models/glutara_model

## Team

Created and developed by AMN:
| Name                           |   Role   |
| ------------------------------ | :------: |
| Michael Leon Putra Widhi       | Hustler  |
| Margaretha Olivia Haryono      | Hipster  |
| Go Dillon Audris               | Hacker   |
| Austin Gabriel Pardosi         | Hacker   |