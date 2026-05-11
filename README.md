# XGenAdapter

多模态大模型适配工具，支持图像理解和文本生成任务

## 功能特性
- 支持LoRA微调训练
- 提供gradio网页demo和API服务
- 兼容HuggingFace模型生态
- 支持多轮对话和长上下文

<img width="1198" height="466" alt="image" src="https://github.com/user-attachments/assets/bf346038-e557-4c32-b226-cd2b8b332ca5" />
<img width="1168" height="602" alt="image" src="https://github.com/user-attachments/assets/35fc86dd-a93d-4ee4-9798-408dab1e706b" />
<img width="1207" height="552" alt="image" src="https://github.com/user-attachments/assets/e693b4ec-0cb8-4bfa-85da-72eeaff47429" />


## 安装依赖
```bash
pip install -r requirements.txt
```

## 快速开始
### 训练模式
```python
python finetune_XGenAdapter.py --dataset_path ./data/demo
```
<img width="1085" height="608" alt="image" src="https://github.com/user-attachments/assets/75b427dd-bb1a-478b-96c7-156bda299f02" />

### 交互演示
```bash
python web_demo.py
```
<img width="1266" height="716" alt="image" src="https://github.com/user-attachments/assets/13e679fb-fc87-4216-b03c-d32a09906f7b" />

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
