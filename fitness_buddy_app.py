from flask import Flask, render_template, request
from ibm_watsonx_ai.foundation_models import Model

app = Flask(__name__)

# Replace these with your actual IBM Cloud credentials
creds = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "1I_N3NPRk_rJQrL5sT_x39yBdHoKieSuyqZTpjelVFM5"
}
project_id = "e7d5c094-af09-4c7e-8945-627bed8b8f83"

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["query"]

        model = Model(
            model_id="google/flan-ul2",  # You can also try 'ibm/granite-13b-chat-v2' if enabled
            params={
                "decoding_method": "greedy",
                "max_new_tokens": 100
            },
            credentials=creds,
            project_id=project_id
        )

        result = model.generate_text(prompt=user_input)
        response_text = result.get("generated_text", "No output received.")

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
