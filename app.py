import pandas as pd
from flask import Flask, render_template, request, Response

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():

    if request.method == "GET":
        return render_template("upload.html")

    file = request.files.get("file")

    if file is None:
        return "No file uploaded"

    if file.content_type == "text/plain":
        return file.read().decode()

    elif file.content_type in [
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel",
    ]:
        df = pd.read_excel(file)
        return df.to_html()

@app.route(rule:'/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return ""
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

