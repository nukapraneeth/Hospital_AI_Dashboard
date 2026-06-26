from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = "No prediction yet."

    patients = [
    {
        "id": "001",
        "name": "Rahul Sharma",
        "age": 25,
        "disease": "Flu",
        "doctor": "Dr. Smith",
        "status": "Admitted"
    },

    {
        "id": "002",
        "name": "Priya Patel",
        "age": 41,
        "disease": "Diabetes",
        "doctor": "Dr. Johnson",
        "status": "Stable"
    },

    {
        "id": "003",
        "name": "Arjun Kumar",
        "age": 58,
        "disease": "Heart Disease",
        "doctor": "Dr. Williams",
        "status": "Critical"
    }
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
        patients=patients    
        )

if __name__ == "__main__":
    app.run(debug=True)