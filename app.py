from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = "No prediction yet."

    if request.method == "POST":

        symptoms = request.form.get("symptoms", "").lower()

        if "fever" in symptoms and "cough" in symptoms:
            prediction = "Flu"

        elif "headache" in symptoms:
            prediction = "Migraine"

        elif "chest pain" in symptoms:
            prediction = "Heart Disease Risk"

        else:
            prediction = "Consult a Doctor"

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)