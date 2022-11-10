from config import DIRECTORY, WATERMARK_IMAGE, ALLOWED_EXTENSIONS
import os
import shutil
from flask import Flask, render_template, redirect, request, flash, send_file
from werkzeug.utils import secure_filename
from PIL import Image
from resizeimage import resizeimage
from time import sleep


app = Flask(__name__)

images = []

@app.route('/', methods=['GET'])
def index():
    return render_template("homepage.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'files' not in request.files:
            flash('Não há arquivos para upload')
            return redirect(request.url)

    files = request.files.getlist("files")
    
    for file in files:
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)   
            file.save(os.path.join(DIRECTORY, filename))
            hasFiles = True
            images.append(DIRECTORY + "/" + filename)

    if hasFiles:
        try:
            print("Images uploaded")
            return 'Images uploaded'
        except Exception as e:
            print(e)
        finally:
            sleep(30)
            return redirect('/resize')

@app.route("/resize", methods=["GET"])
def resize():
    try:
        for image in images:
            img = Image.open(image)
            img = resizeimage.resize_cover(img, [720, 540])
            img.save(image, img.format)
    except Exception as e:
        print(e)
    finally:
        print("Images resized")
        sleep(30)
        return redirect('/watermark')

@app.route("/watermark", methods=["GET"])
def watermark():
    try:
        for image in images:
            photo = Image.open(image)
            watermark = Image.open(WATERMARK_IMAGE).convert("RGBA")
            photo.paste(watermark, (0, 0), watermark)  
            photo.save(image, photo.format)
                
    except Exception as e:
        print(e)

    finally:
        print("Images watermarked")
        sleep(30)
        return redirect('/zip_images')

@app.route("/zip_images", methods=["GET"])
def zip_images():
    try:
        shutil.make_archive("images", "zip", DIRECTORY)
    except Exception as e:
        print(e)
    finally:
        print('Images zipped')
        sleep(30)
        return redirect('/download')

@app.route("/download", methods=["GET"])
def download():
    return send_file('images.zip')

@app.route("/delete_images", methods=["POST"])
def delete_images():
    for filename in os.listdir(DIRECTORY):
        file_path = os.path.join(DIRECTORY, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    os.remove('images.zip')

    print("Images and zip file deleted")
    return redirect('/')



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)