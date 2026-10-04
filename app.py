from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from questions import QUESTIONS

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-publishing"

ACCESS_CODE = "EXCELLENTIA2026"
DURATION_SECONDS = 100 * 60


def access_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("access_granted"):
            return redirect(url_for("access"))
        return view(*args, **kwargs)
    return wrapped

@app.route("/", methods=["GET", "POST"])
def access():
    if request.method == "POST":
        code = request.form.get("code", "").strip()
        if code == ACCESS_CODE:
            session.clear()
            session["access_granted"] = True
            session["started_at"] = __import__("time").time()
            return redirect(url_for("quiz"))
        return render_template("access.html", error="Code incorrect. Vérifie le code puis réessaie.")
    return render_template("access.html", error=None)


@app.route("/quiz")
@access_required
def quiz():
    return render_template(
        "quiz.html",
        questions=QUESTIONS,
        duration=DURATION_SECONDS
    )


@app.route("/submit", methods=["POST"])
@access_required
def submit():
    answers = request.form
    score = 0
    corrections = []

    for q in QUESTIONS:
        selected = answers.get(f"q{q['id']}")
        correct = q["answer"]
        is_correct = selected == correct
        if is_correct:
            score += 1

        corrections.append({
            "id": q["id"],
            "subject": q["subject"],
            "question": q["question"],
            "selected": q["choices"].get(selected, "Aucune réponse"),
            "correct": q["choices"][correct],
            "is_correct": is_correct,
            "explanation": q["explanation"],
        })

    session.clear()
    return render_template(
        "results.html",
        score=score,
        total=len(QUESTIONS),
        corrections=corrections
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("access"))


if __name__ == "__main__":
    app.run(debug=True)
