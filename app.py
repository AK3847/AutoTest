from flask import Flask, render_template, request
import os
import markdown2

from utils import generate_response

app = Flask(__name__)


UPLOAD_FOLDER = "test_uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_files = request.files.getlist("images")
        text_input = request.form.get("text_input", "")

        file_paths = []
        for file in uploaded_files:
            if file.filename != "":
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(file_path)
                file_paths.append(file_path)

        generate_response(image_paths=file_paths, user_prompt=text_input)
        response_md = open("response_markdown.md", "r")
        response_md_html = markdown2.markdown(response_md.read())
        return render_template("index.html", output_html=response_md_html)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.3")
