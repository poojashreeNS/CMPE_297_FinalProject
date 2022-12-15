# CMPE_297_FinalProject

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

# Team Contribution
Training Encoder (Vision Transformer) & Decoder (RoBERTa) - Priyanka Math and Poojashree NS

Traing Vision Encoder and Decoder - Tharun Mukka & Jithesh KB

Creating MLOps pipeline - Tharun Mukka & Jithesh KB

UI development - Priyanka Math and Poojashree NS
