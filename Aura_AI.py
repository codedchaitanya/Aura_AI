

# import logging
# from flask import Flask, request, jsonify, render_template_string
# import tensorflow as tf
# from PIL import Image
# import numpy as np
# import io
# import json
# import base64

# # --- Configuration ---
# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # --- Thresholds for Aura's Security Checks ---
# MEAN_THRESHOLD = 80
# STD_DEV_THRESHOLD = 70
# VOLATILITY_THRESHOLD = 0.1
# PERTURBATION_COUNT = 10

# # --- NEW: Hacker-Vibe HTML Template ---
# # This is a complete redesign of the front-end with a dark theme, CSS animations, and JavaScript interactivity.

# HTML_HACKER_UI = """
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <title>AURA // AI Threat Analysis</title>
#     <link rel="preconnect" href="https://fonts.googleapis.com">
#     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#     <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap" rel="stylesheet">
#     <style>
#         :root {
#             --background: #0a0a10;
#             --primary: #00ff9d;
#             --secondary: #00f2ff;
#             --danger: #ff0055;
#             --text-color: #e6e6e6;
#             --panel-bg: rgba(20, 20, 35, 0.6);
#             --panel-border: rgba(0, 255, 157, 0.3);
#             --glow-shadow: 0 0 5px var(--primary), 0 0 10px var(--primary), 0 0 15px var(--primary);
#         }
#         body {
#             font-family: 'Fira Code', monospace;
#             background-color: var(--background);
#             color: var(--text-color);
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             min-height: 100vh;
#             margin: 0;
#             padding: 1rem;
#             font-size: 14px;
#             text-shadow: 0 0 2px rgba(0, 255, 157, 0.5);
#         }
#         .grid-container {
#             display: grid;
#             grid-template-columns: 1fr 1fr 1.5fr;
#             gap: 1.5rem;
#             width: 100%;
#             max-width: 1400px;
#         }
#         .panel {
#             background: var(--panel-bg);
#             border: 1px solid var(--panel-border);
#             border-radius: 4px;
#             padding: 1.5rem;
#             backdrop-filter: blur(10px);
#             box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
#             min-height: 400px;
#             display: flex;
#             flex-direction: column;
#         }
#         .panel h2 {
#             color: var(--primary);
#             text-transform: uppercase;
#             margin-top: 0;
#             border-bottom: 1px solid var(--panel-border);
#             padding-bottom: 0.5rem;
#             letter-spacing: 2px;
#         }
#         /* Uploader Panel */
#         #drop-zone {
#             border: 2px dashed var(--panel-border);
#             border-radius: 4px;
#             padding: 2rem;
#             text-align: center;
#             cursor: pointer;
#             transition: all 0.3s ease;
#             flex-grow: 1;
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#             align-items: center;
#         }
#         #drop-zone:hover, #drop-zone.dragover {
#             border-color: var(--primary);
#             box-shadow: var(--glow-shadow);
#             background: rgba(0, 255, 157, 0.05);
#         }
#         #file-input { display: none; }
#         #image-preview { max-width: 100%; max-height: 200px; margin-top: 1rem; border-radius: 4px; display: none; }
#         #file-name { color: var(--secondary); margin-top: 1rem; }
#         .btn-submit {
#             background: transparent;
#             border: 1px solid var(--primary);
#             color: var(--primary);
#             padding: 0.75rem 1.5rem;
#             font-family: inherit;
#             font-size: 1rem;
#             cursor: pointer;
#             margin-top: 1.5rem;
#             transition: all 0.3s ease;
#             text-transform: uppercase;
#         }
#         .btn-submit:hover { background: var(--primary); color: var(--background); box-shadow: var(--glow-shadow); }
#         .btn-submit:disabled {
#             border-color: #555;
#             color: #555;
#             cursor: not-allowed;
#             background: transparent;
#             box-shadow: none;
#         }
#         /* Analysis Panel */
#         #analysis-content { text-align: center; margin: auto; }
#         .verdict { font-size: 2.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 4px; }
#         .verdict.benign { color: var(--primary); text-shadow: var(--glow-shadow); }
#         .verdict.threat { color: var(--danger); text-shadow: 0 0 5px var(--danger), 0 0 10px var(--danger), 0 0 15px var(--danger); }
#         .scanner {
#             width: 150px; height: 150px;
#             border: 2px solid var(--secondary);
#             border-radius: 50%;
#             margin: 1rem auto;
#             position: relative;
#             animation: pulse 2s infinite;
#         }
#         .scanner::before, .scanner::after {
#             content: ''; position: absolute; top: -2px; left: 50%; width: 2px; height: 100%; background: var(--primary); transform-origin: bottom;
#         }
#         .scanner::before { animation: scan 3s linear infinite; }
#         @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
#         @keyframes pulse { 0% { box-shadow: 0 0 5px var(--secondary); } 50% { box-shadow: 0 0 20px var(--secondary); } 100% { box-shadow: 0 0 5px var(--secondary); } }

#         /* Telemetry Panel */
#         #telemetry-output {
#             background: rgba(0,0,0,0.5);
#             padding: 1rem;
#             border-radius: 4px;
#             white-space: pre-wrap;
#             word-wrap: break-word;
#             flex-grow: 1;
#             font-size: 12px;
#             overflow-y: auto;
#             border: 1px solid #333;
#         }
#         .typing-cursor {
#             display: inline-block;
#             width: 8px;
#             height: 1em;
#             background-color: var(--primary);
#             animation: blink 1s step-end infinite;
#         }
#         @keyframes blink { 50% { opacity: 0; } }
#     </style>
# </head>
# <body>
#     <div class="grid-container">
#         <!-- Panel 1: Uploader -->
#         <div class="panel">
#             <h2>[INPUT_VECTOR]</h2>
#             <form id="upload-form" action="/predict" method="post" enctype="multipart/form-data">
#                 <label for="file-input" id="drop-zone">
#                     <p>DRAG & DROP // OR CLICK TO SELECT</p>
#                     <img id="image-preview" src="#" alt="Image Preview"/>
#                     <p id="file-name"></p>
#                 </label>
#                 <input type="file" name="image" id="file-input" accept="image/*" required>
#                 <button type="submit" class="btn-submit" id="submit-btn" disabled>INITIATE_SCAN</button>
#             </form>
#         </div>

#         <!-- Panel 2: Analysis -->
#         <div class="panel">
#             <h2>[AURA_ANALYSIS]</h2>
#             <div id="analysis-content">
#                  <div id="scanner-animation" class="scanner" style="display: none;"></div>
#                  <p id="verdict-text"></p>
#             </div>
#         </div>

#         <!-- Panel 3: Telemetry -->
#         <div class="panel">
#             <h2>[TELEMETRY_LOG]</h2>
#             <pre id="telemetry-output">Awaiting input...</pre>
#         </div>
#     </div>

# <script>
#     const dropZone = document.getElementById('drop-zone');
#     const fileInput = document.getElementById('file-input');
#     const imagePreview = document.getElementById('image-preview');
#     const fileNameDisplay = document.getElementById('file-name');
#     const submitBtn = document.getElementById('submit-btn');
#     const uploadForm = document.getElementById('upload-form');
#     const telemetryOutput = document.getElementById('telemetry-output');
#     const scanner = document.getElementById('scanner-animation');
#     const verdictText = document.getElementById('verdict-text');
    
#     // Drag and Drop functionality
#     dropZone.addEventListener('dragover', (e) => {
#         e.preventDefault();
#         dropZone.classList.add('dragover');
#     });
#     dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
#     dropZone.addEventListener('drop', (e) => {
#         e.preventDefault();
#         dropZone.classList.remove('dragover');
#         if (e.dataTransfer.files.length) {
#             fileInput.files = e.dataTransfer.files;
#             handleFileSelect(fileInput.files[0]);
#         }
#     });

#     fileInput.addEventListener('change', () => {
#         if (fileInput.files.length) {
#             handleFileSelect(fileInput.files[0]);
#         }
#     });

#     function handleFileSelect(file) {
#         if (file && file.type.startsWith('image/')) {
#             const reader = new FileReader();
#             reader.onload = (e) => {
#                 imagePreview.src = e.target.result;
#                 imagePreview.style.display = 'block';
#             };
#             reader.readAsDataURL(file);
#             fileNameDisplay.textContent = `FILE: ${file.name}`;
#             submitBtn.disabled = false;
#         }
#     }

#     uploadForm.addEventListener('submit', function(e) {
#         e.preventDefault();
#         submitBtn.disabled = true;
#         submitBtn.textContent = 'ANALYZING...';
#         verdictText.innerHTML = '';
#         telemetryOutput.innerHTML = '';
#         scanner.style.display = 'block';
        
#         const formData = new FormData(this);
        
#         fetch('/predict', {
#             method: 'POST',
#             body: formData
#         })
#         .then(response => response.json())
#         .then(data => {
#             displayResults(data);
#         })
#         .catch(error => {
#             console.error('Error:', error);
#             displayResults({ status: 'Error', message: 'Failed to fetch analysis from server.' });
#         });
#     });
    
#     function typeWriter(element, text, speed = 20) {
#         let i = 0;
#         element.innerHTML = ''; // Clear previous text
#         const cursor = '<span class="typing-cursor"></span>';
#         element.innerHTML = cursor;

#         function typing() {
#             if (i < text.length) {
#                 element.innerHTML = text.substring(0, i + 1) + cursor;
#                 i++;
#                 setTimeout(typing, speed);
#             } else {
#                 element.innerHTML = text; // Remove cursor when done
#             }
#         }
#         typing();
#     }

#     function displayResults(data) {
#         scanner.style.display = 'none';
#         submitBtn.disabled = false;
#         submitBtn.textContent = 'INITIATE_SCAN';

#         const statusClass = data.status === 'Benign' ? 'benign' : 'threat';
#         const verdict = data.status === 'Benign' ? 'SYSTEM SECURE // BENIGN' : 'THREAT DETECTED // HOSTILE';
        
#         verdictText.innerHTML = `<p class="verdict ${statusClass}">${verdict}</p>`;

#         // Pretty print JSON for telemetry
#         const formattedJson = JSON.stringify(data, null, 4);
#         typeWriter(telemetryOutput, formattedJson);
#     }
    
#     // Display initial results if the page was loaded from a form submission
#     const initialResult = {{ result_json | tojson | safe }};
#     if (initialResult && Object.keys(initialResult).length > 0) {
#         // This part handles the case where non-JS clients submit the form.
#         // With our JS fetch, this part is less critical but good for fallback.
#         const preview = document.getElementById('image-preview');
#         if (initialResult.image_preview) {
#             preview.src = initialResult.image_preview;
#             preview.style.display = 'block';
#         }
#         displayResults(initialResult.data);
#     }

# </script>
# </body>
# </html>
# """

# # --- Model Loading ---
# try:
#     protected_model = tf.keras.applications.MobileNetV2(weights='imagenet')
#     logging.info("Protected model (MobileNetV2) loaded successfully.")
# except Exception as e:
#     logging.error(f"Failed to load the model: {e}")
#     protected_model = None

# # --- Core Aura Logic (Functions remain the same) ---
# def statistical_analysis(image_array):
#     mean_val = np.mean(image_array)
#     std_dev_val = np.std(image_array)
#     is_anomaly = bool(mean_val < MEAN_THRESHOLD or std_dev_val > STD_DEV_THRESHOLD)
#     message = (f"Mean={mean_val:.2f}, StdDev={std_dev_val:.2f}. Anomaly detected: {is_anomaly}.")
#     logging.info(f"[Aura Stat Check] {message}")
#     return {
#         'mean_pixel_value': float(mean_val),
#         'std_dev_pixel_value': float(std_dev_val),
#         'is_anomaly': is_anomaly,
#         'message': message
#     }

# def confidence_volatility_analysis(image_array, model):
#     if model is None:
#         return {'confidence_volatility': 0, 'is_volatile': False, 'message': 'Model not loaded.'}
#     perturbations = image_array + np.random.normal(0, 0.5, size=(PERTURBATION_COUNT, 224, 224, 3))
#     perturbations = np.clip(perturbations, 0, 255)
#     predictions = model.predict(perturbations, verbose=0)
#     confidences = np.max(predictions, axis=1)
#     volatility = np.std(confidences)
#     is_volatile = bool(volatility > VOLATILITY_THRESHOLD)
#     message = f"Confidence volatility is {volatility:.4f}. Volatile: {is_volatile}."
#     logging.info(f"[Aura Volatility Check] {message}")
#     return {
#         'confidence_volatility': float(volatility),
#         'is_volatile': is_volatile,
#         'message': message
#     }

# # --- Flask Web Application ---
# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     """Renders the main page with the upload form."""
#     return render_template_string(HTML_HACKER_UI, result_json={})

# @app.route('/predict', methods=['POST'])
# def predict():
#     """Handles the AJAX request from the new UI."""
#     if protected_model is None:
#         return jsonify({'error': 'AI model is not available.'}), 503

#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided.'}), 400

#     file = request.files['image']
    
#     try:
#         # Read file for processing
#         image_bytes = file.read()
#         image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
#         image = image.resize((224, 224))
#         image_array = np.array(image)
#         processed_image = np.expand_dims(image_array, axis=0)
#     except Exception as e:
#         logging.error(f"Error processing image: {e}")
#         return jsonify({'error': f'Invalid or corrupt image file: {e}'}), 400

#     logging.info(f"--- New Request for file '{file.filename}' from IP {request.remote_addr} ---")
    
#     # --- AURA'S SECURITY GATEWAY LOGIC ---
#     stat_details = statistical_analysis(image_array)
#     vol_details = confidence_volatility_analysis(processed_image, protected_model)
#     is_statistical_anomaly = stat_details['is_anomaly']
#     is_volatile = vol_details['is_volatile']

#     response_data = {}

#     if is_statistical_anomaly or is_volatile:
#         logging.warning(f"Threat Detected for file '{file.filename}'. Anomaly: {is_statistical_anomaly}, Volatility: {is_volatile}")
#         response_data = {
#             'status': 'Threat Detected',
#             'threat_type': 'Adversarial Attack Pattern',
#             'details': {'statistical_analysis': stat_details, 'confidence_volatility': vol_details}
#         }
#         return jsonify(response_data), 403 # Send JSON with 403 status
#     else:
#         logging.info(f"Scan complete for '{file.filename}'. Input appears benign.")
#         predictions = protected_model.predict(processed_image, verbose=0)
#         decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
#         output_predictions = [{'label': label, 'score': float(score)} for _, label, score in decoded_predictions]
#         response_data = {
#             'status': 'Benign',
#             'predictions': output_predictions,
#             'details': {'statistical_analysis': stat_details, 'confidence_volatility': vol_details}
#         }
#         return jsonify(response_data)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

import logging
from flask import Flask, request, jsonify, render_template_string
import tensorflow as tf
from PIL import Image
import numpy as np
import io
import json
import base64

# --- Configuration ---
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Thresholds for Aura's Security Checks ---
MEAN_THRESHOLD = 80
STD_DEV_THRESHOLD = 70
VOLATILITY_THRESHOLD = 0.1
PERTURBATION_COUNT = 10

# --- NEW: Hacker-Vibe HTML Template ---
# This is a complete redesign of the front-end with a dark theme, CSS animations, and JavaScript interactivity.

HTML_HACKER_UI = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AURA // AI Threat Analysis</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --background: #0a0a10;
            --primary: #00ff9d;
            --secondary: #00f2ff;
            --danger: #ff0055;
            --text-color: #e6e6e6;
            --panel-bg: rgba(20, 20, 35, 0.6);
            --panel-border: rgba(0, 255, 157, 0.3);
            --glow-shadow: 0 0 5px var(--primary), 0 0 10px var(--primary), 0 0 15px var(--primary);
        }
        body {
            font-family: 'Fira Code', monospace;
            background-color: var(--background);
            color: var(--text-color);
            display: flex;
            flex-direction: column; /* Changed for header/footer */
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 1rem;
            font-size: 14px;
            text-shadow: 0 0 2px rgba(0, 255, 157, 0.5);
        }
        .main-container {
            width: 100%;
            max-width: 1400px;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
        /* NEW: Header Styles */
        header {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 4px;
            padding: 1rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        }
        .logo h1 {
            margin: 0;
            color: var(--primary);
            font-size: 1.8rem;
            text-shadow: var(--glow-shadow);
            text-transform: uppercase;
        }
        .status-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .status-light {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: var(--primary);
            box-shadow: var(--glow-shadow);
            animation: pulse-status 2s infinite;
        }
        @keyframes pulse-status {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        .grid-container {
            display: grid;
            grid-template-columns: 1fr 1fr 1.5fr;
            gap: 1.5rem;
            width: 100%;
        }
        .panel {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 4px;
            padding: 1.5rem;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
            min-height: 400px;
            display: flex;
            flex-direction: column;
        }
        .panel h2 {
            color: var(--primary);
            text-transform: uppercase;
            margin-top: 0;
            border-bottom: 1px solid var(--panel-border);
            padding-bottom: 0.5rem;
            letter-spacing: 2px;
        }
        /* Uploader Panel */
        #drop-zone {
            border: 2px dashed var(--panel-border);
            border-radius: 4px;
            padding: 2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        #drop-zone:hover, #drop-zone.dragover {
            border-color: var(--primary);
            box-shadow: var(--glow-shadow);
            background: rgba(0, 255, 157, 0.05);
        }
        #file-input { display: none; }
        #image-preview { max-width: 100%; max-height: 200px; margin-top: 1rem; border-radius: 4px; display: none; }
        #file-name { color: var(--secondary); margin-top: 1rem; }
        .btn-submit {
            background: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
            padding: 0.75rem 1.5rem;
            font-family: inherit;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 1.5rem;
            transition: all 0.3s ease;
            text-transform: uppercase;
        }
        .btn-submit:hover { background: var(--primary); color: var(--background); box-shadow: var(--glow-shadow); }
        .btn-submit:disabled {
            border-color: #555;
            color: #555;
            cursor: not-allowed;
            background: transparent;
            box-shadow: none;
        }
        /* Analysis Panel */
        #analysis-content { text-align: center; margin: auto; }
        .verdict { font-size: 2.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 4px; }
        .verdict.benign { color: var(--primary); text-shadow: var(--glow-shadow); }
        .verdict.threat { color: var(--danger); text-shadow: 0 0 5px var(--danger), 0 0 10px var(--danger), 0 0 15px var(--danger); }
        .scanner {
            width: 150px; height: 150px;
            border: 2px solid var(--secondary);
            border-radius: 50%;
            margin: 1rem auto;
            position: relative;
            animation: pulse 2s infinite;
        }
        .scanner::before, .scanner::after {
            content: ''; position: absolute; top: -2px; left: 50%; width: 2px; height: 100%; background: var(--primary); transform-origin: bottom;
        }
        .scanner::before { animation: scan 3s linear infinite; }
        @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        @keyframes pulse { 0% { box-shadow: 0 0 5px var(--secondary); } 50% { box-shadow: 0 0 20px var(--secondary); } 100% { box-shadow: 0 0 5px var(--secondary); } }

        /* Telemetry Panel */
        #telemetry-output {
            background: rgba(0,0,0,0.5);
            padding: 1rem;
            border-radius: 4px;
            white-space: pre-wrap;
            word-wrap: break-word;
            flex-grow: 1;
            font-size: 12px;
            overflow-y: auto;
            border: 1px solid #333;
        }
        .typing-cursor {
            display: inline-block;
            width: 8px;
            height: 1em;
            background-color: var(--primary);
            animation: blink 1s step-end infinite;
        }
        @keyframes blink { 50% { opacity: 0; } }
        
        /* NEW: Footer Styles */
        footer {
            width: 100%;
            max-width: 1400px;
            text-align: center;
            font-size: 0.8rem;
            color: #555;
            padding-top: 1rem;
            border-top: 1px solid rgba(0, 255, 157, 0.1);
        }
    </style>
</head>
<body>
    <div class="main-container">
        <!-- NEW: Header -->
        <header>
            <div class="logo">
                <h1>AURA_AI</h1>
            </div>
            <div class="status-indicator">
                <span>SYSTEM_STATUS:</span>
                <div class="status-light"></div>
                <span>ONLINE</span>
            </div>
        </header>

        <div class="grid-container">
            <!-- Panel 1: Uploader -->
            <div class="panel">
                <h2>[INPUT_VECTOR]</h2>
                <form id="upload-form" action="/predict" method="post" enctype="multipart/form-data">
                    <label for="file-input" id="drop-zone">
                        <p>DRAG & DROP // OR CLICK TO SELECT</p>
                        <img id="image-preview" src="#" alt="Image Preview"/>
                        <p id="file-name"></p>
                    </label>
                    <input type="file" name="image" id="file-input" accept="image/*" required>
                    <button type="submit" class="btn-submit" id="submit-btn" disabled>INITIATE_SCAN</button>
                </form>
            </div>

            <!-- Panel 2: Analysis -->
            <div class="panel">
                <h2>[AURA_ANALYSIS]</h2>
                <div id="analysis-content">
                     <div id="scanner-animation" class="scanner" style="display: none;"></div>
                     <p id="verdict-text"></p>
                </div>
            </div>

            <!-- Panel 3: Telemetry -->
            <div class="panel">
                <h2>[TELEMETRY_LOG]</h2>
                <pre id="telemetry-output">Awaiting input...</pre>
            </div>
        </div>

        <!-- NEW: Footer -->
        <footer>
            <p>&copy; 2025 AURA Defensive Systems // v1.2.0 // Kernel: SecureML_Guard</p>
        </footer>
    </div>

<script>
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const imagePreview = document.getElementById('image-preview');
    const fileNameDisplay = document.getElementById('file-name');
    const submitBtn = document.getElementById('submit-btn');
    const uploadForm = document.getElementById('upload-form');
    const telemetryOutput = document.getElementById('telemetry-output');
    const scanner = document.getElementById('scanner-animation');
    const verdictText = document.getElementById('verdict-text');
    
    // Drag and Drop functionality
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });
    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            handleFileSelect(fileInput.files[0]);
        }
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length) {
            handleFileSelect(fileInput.files[0]);
        }
    });

    function handleFileSelect(file) {
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
            };
            reader.readAsDataURL(file);
            fileNameDisplay.textContent = `FILE: ${file.name}`;
            submitBtn.disabled = false;
        }
    }

    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        submitBtn.disabled = true;
        submitBtn.textContent = 'ANALYZING...';
        verdictText.innerHTML = '';
        telemetryOutput.innerHTML = '';
        scanner.style.display = 'block';
        
        const formData = new FormData(this);
        
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                // For HTTP errors like 403, the browser won't parse it as JSON by default
                // So we need to handle it. We can still try to get the JSON body.
                return response.json().then(errData => {
                    throw errData; // Throw error to be caught by .catch
                });
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
        })
        .catch(errorData => {
            // This will catch both network errors and the thrown error from a bad HTTP status
            console.error('Error:', errorData);
            displayResults(errorData);
        });
    });
    
    function typeWriter(element, text, speed = 20) {
        let i = 0;
        element.innerHTML = ''; // Clear previous text
        const cursor = '<span class="typing-cursor"></span>';
        element.innerHTML = cursor;

        function typing() {
            if (i < text.length) {
                element.innerHTML = text.substring(0, i + 1) + cursor;
                i++;
                setTimeout(typing, speed);
            } else {
                element.innerHTML = text; // Remove cursor when done
            }
        }
        typing();
    }

    function displayResults(data) {
        scanner.style.display = 'none';
        submitBtn.disabled = false;
        submitBtn.textContent = 'INITIATE_SCAN';

        const statusClass = data.status === 'Benign' ? 'benign' : 'threat';
        const verdict = data.status === 'Benign' ? 'SYSTEM SECURE // BENIGN' : 'THREAT DETECTED // HOSTILE';
        
        verdictText.innerHTML = `<p class="verdict ${statusClass}">${verdict}</p>`;

        // Pretty print JSON for telemetry
        const formattedJson = JSON.stringify(data, null, 4);
        typeWriter(telemetryOutput, formattedJson);
    }
    
    // Display initial results if the page was loaded from a form submission
    const initialResult = {{ result_json | tojson | safe }};
    if (initialResult && Object.keys(initialResult).length > 0) {
        // This part handles the case where non-JS clients submit the form.
        // With our JS fetch, this part is less critical but good for fallback.
        const preview = document.getElementById('image-preview');
        if (initialResult.image_preview) {
            preview.src = initialResult.image_preview;
            preview.style.display = 'block';
        }
        displayResults(initialResult.data);
    }

</script>
</body>
</html>
"""

# --- Model Loading ---
try:
    protected_model = tf.keras.applications.MobileNetV2(weights='imagenet')
    logging.info("Protected model (MobileNetV2) loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load the model: {e}")
    protected_model = None

# --- Core Aura Logic (Functions remain the same) ---
def statistical_analysis(image_array):
    mean_val = np.mean(image_array)
    std_dev_val = np.std(image_array)
    is_anomaly = bool(mean_val < MEAN_THRESHOLD or std_dev_val > STD_DEV_THRESHOLD)
    message = (f"Mean={mean_val:.2f}, StdDev={std_dev_val:.2f}. Anomaly detected: {is_anomaly}.")
    logging.info(f"[Aura Stat Check] {message}")
    return {
        'mean_pixel_value': float(mean_val),
        'std_dev_pixel_value': float(std_dev_val),
        'is_anomaly': is_anomaly,
        'message': message
    }

def confidence_volatility_analysis(image_array, model):
    if model is None:
        return {'confidence_volatility': 0, 'is_volatile': False, 'message': 'Model not loaded.'}
    perturbations = image_array + np.random.normal(0, 0.5, size=(PERTURBATION_COUNT, 224, 224, 3))
    perturbations = np.clip(perturbations, 0, 255)
    predictions = model.predict(perturbations, verbose=0)
    confidences = np.max(predictions, axis=1)
    volatility = np.std(confidences)
    is_volatile = bool(volatility > VOLATILITY_THRESHOLD)
    message = f"Confidence volatility is {volatility:.4f}. Volatile: {is_volatile}."
    logging.info(f"[Aura Volatility Check] {message}")
    return {
        'confidence_volatility': float(volatility),
        'is_volatile': is_volatile,
        'message': message
    }

# --- Flask Web Application ---
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the main page with the upload form."""
    return render_template_string(HTML_HACKER_UI, result_json={})

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the AJAX request from the new UI."""
    if protected_model is None:
        return jsonify({'error': 'AI model is not available.'}), 503

    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided.'}), 400

    file = request.files['image']
    
    try:
        # Read file for processing
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image = image.resize((224, 224))
        image_array = np.array(image)
        processed_image = np.expand_dims(image_array, axis=0)
    except Exception as e:
        logging.error(f"Error processing image: {e}")
        return jsonify({'error': f'Invalid or corrupt image file: {e}'}), 400

    logging.info(f"--- New Request for file '{file.filename}' from IP {request.remote_addr} ---")
    
    # --- AURA'S SECURITY GATEWAY LOGIC ---
    stat_details = statistical_analysis(image_array)
    vol_details = confidence_volatility_analysis(processed_image, protected_model)
    is_statistical_anomaly = stat_details['is_anomaly']
    is_volatile = vol_details['is_volatile']

    response_data = {}

    if is_statistical_anomaly or is_volatile:
        logging.warning(f"Threat Detected for file '{file.filename}'. Anomaly: {is_statistical_anomaly}, Volatility: {is_volatile}")
        response_data = {
            'status': 'Threat Detected',
            'threat_type': 'Adversarial Attack Pattern',
            'details': {'statistical_analysis': stat_details, 'confidence_volatility': vol_details}
        }
        return jsonify(response_data), 403 # Send JSON with 403 status
    else:
        logging.info(f"Scan complete for '{file.filename}'. Input appears benign.")
        predictions = protected_model.predict(processed_image, verbose=0)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
        output_predictions = [{'label': label, 'score': float(score)} for _, label, score in decoded_predictions]
        response_data = {
            'status': 'Benign',
            'predictions': output_predictions,
            'details': {'statistical_analysis': stat_details, 'confidence_volatility': vol_details}
        }
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



