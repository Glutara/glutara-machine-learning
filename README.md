<br>
<div align="center">
    <div >
        <img height="150px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2FGlutara.png?alt=media&token=77d4dd88-6cca-4e4d-94f2-321124c20a61" alt=""/>
    </div>
    <div>
            <h3><b>Glutara</b></h3>
            <p><i>A Key to Your Diabetes Journey</i></p>
    </div>      
</div>
<br>
<h1 align="center">Glutara Machine Learning</h1>
Your personal whisperer: Glutara's cutting-edge machine learning deciphers your unique biological dance, translating data into actionable insights. It's your future health confidante, whispering personalized recommendations and guiding you towards empowered decisions.

### 👨🏻‍💻 &nbsp;Technology Stack

<div align="center">

<a href="https://www.tensorflow.org/">
<kbd>
<img src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Ficons%2FTensorFlow.png?alt=media&token=25493f37-e246-4a99-ba38-9fa04a286265" height="60" />
</kbd>
</a>

<a href="https://www.docker.com/">
<kbd>
<img src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Ficons%2FDocker.png?alt=media&token=3588896c-975f-496f-87d0-e7e1bce0d492" height="60" />
</kbd>
</a>

</div>
<div align="center">
<h4>TensorFlow</h4>
</div>

## Getting Started
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

## ⚙️ &nbsp;How to Run
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

## 👥 &nbsp;Contributors

| <a href="https://github.com/mikeleo03"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FLeon.png?alt=media&token=0ea1884a-32ca-471b-a3af-bf3995bbc605" alt=""/></a> | <a href="https://github.com/GoDillonAudris512"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FDillon.png?alt=media&token=bc76cc6b-5606-4351-8472-9c243c8b9da3" alt=""/></a> | <a href="https://github.com/margarethaolivia"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FOlivia.png?alt=media&token=d53f9cfd-e1e1-41b6-a28c-440904df29b8" alt=""/></a> | <a href="https://github.com/AustinPardosi"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FAustin.png?alt=media&token=f520a334-4aeb-4efe-9437-669451b6dca6" alt=""/></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div align="center"><h3><b><a href="https://github.com/mikeleo03">Michael Leon Putra Widhi</a></b></h3><i><p>Bandung Institute of Technology</i></p></div>                                                                               | <div align="center"><h3><b><a href="https://github.com/GoDillonAudris512">Go Dillon Audris</a></b></h3></a><p><i>Bandung Institute of Technology</i></p></div>                                                                          | <div align="center"><h3><b><a href="https://github.com/margarethaolivia">Margaretha Olivia Haryono</a></b></h3></a><p><i>Bandung Institute of Technology</i></p></div>                                                               | <div align="center"><h3><b><a href="https://github.com/AustinPardosi">Austin Gabriel Pardosi</a></b></h3></a><p><i>Bandung Institute of Technology</i></p></div>                                                                            |