# MTD
Multi-Timestep Detector for Delayed Streaming Perception

## Benchmark
<table width="1000px" cellspacing="10">
<tr>
  <th align="center">Model</th>
  <th align="center">Size</th>
  <th align="center">sAP 0.5:0.95</th>
  <th align="center">sAP50</th>
  <th align="center">sAP75</th>
  <th align="center">weights</th>
</tr>
<tr>
  <td colspan="6" align="center">None (27ms±1)</td>
</tr>
<tr>
    <tr>
      <td align="center">StreamYOLO</td>
      <td align="center">600×960</td>
      <td align="center">36.9</td>
      <td align="center">58.1</td>
      <td align="center">37.6</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">DaDe</td>
      <td align="center">600×960</td>
      <td align="center">36.9</td>
      <td align="center">58.0</td>
      <td align="center">37.6</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">MTD</td>
      <td align="center">600×960</td>
      <td align="center">36.9</td>
      <td align="center">58.1</td>
      <td align="center">37.7</td>
      <td align="center"><a href="https://github.com/Yulin1004/MTD/releases/download/v1.0.0/mtd_l_s50_one_x.pth">weight</a></td>
    </tr>
<tr>
  <td colspan="6" align="center">Low (59ms±1)</td>
</tr>
<tr>
    <tr>
      <td align="center">StreamYOLO</td>
      <td align="center">600×960</td>
      <td align="center">26.2</td>
      <td align="center">48.0</td>
      <td align="center">24.4</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">DaDe</td>
      <td align="center">600×960</td>
      <td align="center">27.8</td>
      <td align="center">49.0</td>
      <td align="center">26.8</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">MTD</td>
      <td align="center">600×960</td>
      <td align="center">29.1</td>
      <td align="center">51.5</td>
      <td align="center">28.0</td>
      <td align="center"><a href="https://github.com/Yulin1004/MTD/releases/download/v1.0.0/mtd_l_s50_one_x.pth">weight</a></td>
    </tr>
<tr>
  <td colspan="6" align="center">Medium (69ms±1)</td>
</tr>
    <tr>
      <td align="center">StreamYOLO</td>
      <td align="center">600×960</td>
      <td align="center">25.3</td>
      <td align="center">46.8</td>
      <td align="center">23.1</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">DaDe</td>
      <td align="center">600×960</td>
      <td align="center">25.3</td>
      <td align="center">46.9</td>
      <td align="center">23.5</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">MTD</td>
      <td align="center">600×960</td>
      <td align="center">26.4</td>
      <td align="center">49.0</td>
      <td align="center">24.2</td>
      <td align="center"><a href="https://github.com/Yulin1004/MTD/releases/download/v1.0.0/mtd_l_s50_one_x.pth">weight</a></td>
    </tr>
<tr>
  <td colspan="6" align="center">High (90ms±1)</td>
</tr>
<tr>
    <tr>
      <td align="center">StreamYOLO</td>
      <td align="center">600×960</td>
      <td align="center">22.7</td>
      <td align="center">43.3</td>
      <td align="center">20.5</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">DaDe</td>
      <td align="center">600×960</td>
      <td align="center">22.4</td>
      <td align="center">42.2</td>
      <td align="center">20.1</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
<b>
    <tr>
      <td align="center">MTD</td>
      <td align="center">600×960</td>
      <td align="center">24.1</td>
      <td align="center">46.1</td>
      <td align="center">21.4</td>
      <td align="center"><a href="https://github.com/Yulin1004/MTD/releases/download/v1.0.0/mtd_l_s50_one_x.pth">weight</a></td>
    </tr>
</b>
</table>

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
cd MTD

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
