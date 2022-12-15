# CMPE_297_FinalProject

## Description
Using any natural language words to automatically generate an image's caption or description is a very difficult undertaking. The goal of our project is to put into practice an image caption generator that responds to user input to produce captions for a picture. To translate the comprehension of the image into words in the appropriate sequence, it needs both computer vision techniques to comprehend the image's content and a language model from the field of natural language processing. Due to the mutual exclusivity of images and text sequences, this job requires the use of two interconnected models, one of which is dedicated to image encoding and the other to text decoding. As part of this project, first a language model named Roberta will be trained and fine tuned on captions and then a captioning model will be initialized and trained using Vision Encoder Decoder module of hugging face library.

All the model artifacts and datasets are available in this drive [link](https://drive.google.com/drive/folders/1sEPuz6B-4aWoA1gmQQQ2pgalU3pvx8Nz?usp=sharing)

Presentation video: [link](https://drive.google.com/file/d/128xtnxmLGZYFE5t_nVnItm9T_cvOYDC4/view?usp=sharing)


https://user-images.githubusercontent.com/89234077/206963311-5c7ecf47-e2fc-4814-a59f-1ecb8019478f.mp4


Project Report: [link](https://github.com/poojashreeNS/CMPE_297_FinalProject/blob/main/Report.pdf)

MLOps Doc: [link](https://github.com/poojashreeNS/CMPE_297_FinalProject/blob/main/MLOps-Doc.pdf)

Presentation: [link](https://github.com/poojashreeNS/CMPE_297_FinalProject/blob/main/Image%20Caption%20Generator.pdf)

Colab: [link](https://github.com/poojashreeNS/CMPE_297_FinalProject/blob/main/Image_Caption_Transfer_Learning_updated.ipynb)

# Running the Streamlit application in local
please create a new conda environment and activate it

* Create new conda environment
  ```sh
  conda create --name {env_name}
  ```

* Activate the newly created environment
  ```sh
  conda activate {env_name}
  ```
* Install the packages from the requirements file
  ```sh
  pip install -r requirements.txt
  ```

* Start the application
  ```sh
  streamlit run apy.py
  ```

# Results
![UI Screenshot with generated caption for the image](https://github.com/poojashreeNS/CMPE_297_FinalProject/blob/main/images/UI_results.png)

# Demo
Access the Application [here](https://tmukka-test.hf.space/)

# Build & Deploy Steps
1.	Read more about [DagsHub](https://dagshub.com/docs/)

### DagsHub Instructions
1. Press the green ‘+ Create’ button on the top right and click ‘Connect A Repo’
2. Click on the GitHub connect button and authorize in GitHub
3. Choose to either give access to all your repositories or specific ones you want to connect
4. Click the repository you want to connect on DagsHub and click Connect Repository

### MLflow
1. Select the best performing model

### Deployment on Huggingface Space
1. Create a Streamlit SDK Space on Huggingface Space
2. Upload all the project files to deploy the application on Huggingface Space

# Team Contribution
Training Encoder (Vision Transformer) & Decoder (RoBERTa) - Priyanka Math and Poojashree NS

Traing Vision Encoder and Decoder - Tharun Mukka & Jithesh KB

Creating MLOps pipeline - Tharun Mukka & Jithesh KB

UI development - Priyanka Math and Poojashree NS
