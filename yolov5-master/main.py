
#import argparse
import io
#from hubconf import custom
#import detect
#import torch
from flask import Flask, render_template, request,jsonify,redirect
from PIL import Image,ImageOps
from werkzeug.utils import secure_filename
import cv2
#import pytesseract
from datetime import timedelta
import os
from detect import run

ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG', 'bmp', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__.split('.')[0])

app.send_file_max_age_default = timedelta(seconds=1)

DETECTION_URL = "/OD"

@app.route('/', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            if not (file and allowed_file(file.filename)):
                return jsonify({"error": 1001, "msg": "please check the format of uploaded picture which is limited to "
                                                      "png, jpg, JPG, PNG, bmp, jpeg"})
    #    basepath = os.path.dirname(__file__)
#        img_bytes = f.read()
#        img = Image.open(io.BytesIO(img_bytes))
        i = 1
        for file in files:
            extension = os.path.splitext(file.filename)[1]
            upload_path = 'detection/original/' + str(i) + extension
            file.save(upload_path)
            i += 1

        run_dict = {
            'weights': 'runs/train/yolov5s_results/weights/best.pt',
            'source': 'detection/original',
            'imgsz': [640, 640],
            'conf_thres': 0.8,
            'iou_thres': 0.75,
            'max_det': 5,
            'device': 'cpu',
            'view_img': False,
            'save_txt': False,
            'save_conf': True,
            'save_crop': True,
            'nosave': False,
            'classes': 0,
            'agnostic_nms': False,
            'augment': False,
            'visualize': False,
            'update': False,
            'project': 'detection/result',
            'name': '',
            'exist_ok': False,
            'line_thickness': 3,
            'hide_labels': False,
            'hide_conf': False,
            'half': False,
            'dnn': False
        }
        run(**run_dict)
#        results = model(img, size=640)
#        results = Image.open('runs/detect/result'+ f.filename)
#        gry = ImageOps.grayscale('runs/detect/result'+ f.filename)
        #print(pytesseract.image_to_string(gry, config="--oem 1 --psm 6", lang='eng')))

        # for debugging
        # data = results.pandas().xyxy[0].to_json(orient="records")
        # return data

#        results.render()  # updates results.imgs with boxes and labels
#        for img in results.imgs:
#            img_base64 = Image.fromarray(img)
#            img_base64.save("static/image0.jpg", format="JPEG")
#        return redirect("static/image0.jpg")
        return render_template("results.html")
    return render_template("Interface.html")

#def print():
#    img = Image.open(io.BytesIO(img_bytes))
#    gry = ImageOps.grayscale(img)
#    return pytesseract.image_to_string(gry, config="--oem 1 --psm 6", lang='eng')


if __name__ == "__main__":
    #    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    #    parser.add_argument("--port", default=5000, type=int, help="port number")
    #    opt = parser.parse_args()

    # Fix known issue urllib.error.HTTPError 403: rate limit exceeded https://github.com/ultralytics/yolov5/pull/7210
    #  torch.hub._validate_not_a_forked_repo = lambda a, b, c: True
#    model = custom('runs/train/yolov5s_results/weights/best.pt')
#    model = torch.hub.load('runs/train/yolov5s_results/weights/best.pt' ,source='local')
#    model.eval()
    #   app.run(host="0.0.0.0", port=opt.port)  # debug=True causes Restarting with stat
    app.run(debug=True)
