from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import base64
import io
import os
import tempfile
from web_demo import generate_text_with_image

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    # 解析输入参数
    input_text = data.get('text', '')
    image_b64 = data.get('image', '')
    history = data.get('history', [])
    
    # 处理图片上传
    try:
        image_data = base64.b64decode(image_b64.split(',')[-1])
        image = Image.open(io.BytesIO(image_data))
        
        # 创建临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp:
            image.save(temp, format='PNG')
            temp_path = temp.name
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Invalid image data: ' + str(e)
        }), 400

    # 调用核心处理逻辑
    try:
        answer = generate_text_with_image(
            input_text=input_text,
            image=temp_path,
            history=history,
            request_data={
                'temperature': data.get('temperature', 0.8),
                'top_p': data.get('top_p', 0.4)
            }
        )
        
        # 清理临时文件
        os.unlink(temp_path)
        
        return jsonify({
            'status': 'success',
            'answer': answer,
            'history': history
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Processing error: ' + str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)