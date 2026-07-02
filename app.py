from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        disease = request.form["disease"]
        doctor = request.form["doctor"]
        status = request.form["status"]

        new_patient = {
            "id": str(len(patients) + 1).zfill(3),
            "name": name,
            "age": age,
            "disease": disease,
            "doctor": doctor,
            "status": status
        }

        patients.append(new_patient)

        return redirect(url_for("patients_page"))

    return render_template("add_patient.html")

if __name__ == "__main__":
        app.run(debug=True)