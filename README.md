
## Dataset Preparation
This implementation is built upon StreamYOLO.

Download Argoverse-1.1 full dataset and annotation at this [link](https://www.cs.cmu.edu/~mengtial/proj/streaming/).

The folder structure should be organized as below.
```shell
MTD
├── cfgs
├── ckpts
├── exps
├── sAP
├── tools
├── data
│   ├── Argoverse-1.1
│   │   ├── annotations
│   │       ├── tracking
│   │           ├── train
│   │           ├── val
│   │           ├── test 
│   ├── Argoverse-HD
│   │   ├── annotations
│   │       ├── test-meta.json
│   │       ├── train.json
│   │       ├── val.json
```

## Environment Setup
```shell
# Create virtual environment
conda create --name mtd python=3.7
conda activate mtd

pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip3 install yolox==0.3

git clone https://github.com/Yulin1004/MTD.git
cd mtd

ADDPATH=$(pwd)
echo export PYTHONPATH=$PYTHONPATH:$ADDPATH >> ~/.bashrc
source ~/.bashrc

# Installing `mmcv` for the official sAP evaluation:
# Please replace `{cu_version}` and ``{torch_version}`` with the versions you are currently using.
pip install mmcv-full==1.1.5 -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
```

## Train
#### Step1. Build symbolic link to Argoverse-HD dataset.
```shell
cd <MTD_HOME>
ln -s /path/to/your/Argoverse-1.1 ./data/Argoverse-1.1
ln -s /path/to/your/Argoverse-HD ./data/Argoverse-HD
```
#### Step2. Train model with Argoverse-HD dataset:
```shell
python tools/mtd_train.py -f cfgs/l_s50_onex_mtd_dfp_tal_filp.py -d 8 -b 32 -c /path/to/streamyolo_pretrained_weights.pth -o --fp16
```
* -d: number of gpu devices.
* -b: total batch size, the recommended number for -b is num-gpu * 8.
* --fp16: mixed precision training.
* -c: model checkpoint path.

## Online Evaluation
Modified online evaluation from [sAP](https://github.com/mtli/sAP)
```shell
cd sAP/mtd
./mtd.sh
