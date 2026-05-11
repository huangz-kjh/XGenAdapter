# XGenAdapter

多模态大模型适配工具，支持图像理解和文本生成任务

## 功能特性
- 支持LoRA微调训练
- 提供gradio网页demo和API服务
- 兼容HuggingFace模型生态
- 支持多轮对话和长上下文

<img width="703" height="275" alt="image" src="https://github.com/user-attachments/assets/8809e4d7-1317-40e6-b98f-58d9fb99e668" />
<img width="709" height="344" alt="image" src="https://github.com/user-attachments/assets/2cafc4f4-a397-43d4-b026-69879829f54e" />
<img width="627" height="354" alt="image" src="https://github.com/user-attachments/assets/790e6f38-9ebc-43c6-8f32-80c5ceb91f73" />



## 安装依赖
```bash
pip install -r requirements.txt
```

## 快速开始
### 训练模式
```python
python finetune_XGenAdapter.py --dataset_path ./data/demo
```
<img width="588" height="336" alt="image" src="https://github.com/user-attachments/assets/2a6f6ad9-12b0-46b4-b1a9-d96d24ee53e7" />
<img width="701" height="289" alt="image" src="https://github.com/user-attachments/assets/202f309c-d845-46c7-918a-ba789825b21b" />
<img width="701" height="388" alt="image" src="https://github.com/user-attachments/assets/1c045246-7d08-412b-8872-2c630e0b7ea0" />


### 交互演示
```bash
python web_demo.py
```
<img width="675" height="273" alt="image" src="https://github.com/user-attachments/assets/5aa619ae-275a-4af1-98a4-e5edcf67c842" />


### API服务
```bash
python api_server.py --port 8000
```

## 数据准备
1. 将图片放入`data/demo`目录
2. 运行数据处理脚本：
```bash
python data/build_images_data.py
```
