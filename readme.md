# Deepfake-Video-Forgery-Detection 
## Getting Started
### Prerequisites
You need Python3.X and conda package manager to run this tool

## Installation
The follwing steps can be used to install the required packages :
1. Clone the repository `git clone https://github.com/tre3x/Deepfake-Video-Forgery-Detection.git`
2. Inialize a conda environment with neccessary packages `conda env create -f environment.yml`
3. Activate conda enviroment `conda activate DeepFakeDetection`
Once the conda enviroment is activated, we can procees to training the model.

## Training
For training the model, the following command can be used 
```bash
python main.py --train {training path} --val {validation path} --epochs {final epoch} --batch {batch size} --steps {steps} 
```
{training path} : Path to the training image set  
{validation path} : Path to the validation image set  
{final epochs} : Number of epochs used while training final fused model  
{batch size} : Batch Size used while training and validating  
{Steps} : Number of steps per epochs while training  