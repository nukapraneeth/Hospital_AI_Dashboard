from flask import Flask, render_template, request

from data.patients import patients

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = "No prediction yet."

    search_query = request.args.get("search", "").lower()

    filtered_patients = patients

    if search_query:
        filtered_patients = [
            patient for patient in patients
            if search_query in patient["name"].lower()
            or search_query in patient["disease"].lower()
            or search_query in patient["status"].lower()
        ]

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
        prediction=prediction,
        patients=filtered_patients,
        search_query=search_query
    )

@app.route("/patients")
def patients_page():

    return render_template(
        "patients.html",
        patients=patients
    )

if __name__ == "__main__":
        app.run(debug=True)