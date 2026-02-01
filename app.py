from dataclasses import dataclass
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@dataclass(frozen=True)
class Module:
    title: str
    duration: str
    status: str


@dataclass(frozen=True)
class Course:
    id: int
    title: str
    category: str
    instructor: str
    level: str
    description: str
    modules: list[Module]
    assignments: list[str]
    enrolled: int
    progress: int


COURSES = [
    Course(
        id=1,
        title="Foundations of Product Design",
        category="Design",
        instructor="Camila Reyes",
        level="Beginner",
        description=(
            "Learn the fundamentals of user-centered design, from research and "
            "wireframing to prototyping and testing."
        ),
        modules=[
            Module("Design research essentials", "1h 10m", "Complete"),
            Module("Personas & journey maps", "1h 40m", "In progress"),
            Module("Wireframes to prototypes", "2h 05m", "Locked"),
        ],
        assignments=["Persona workshop", "Prototype walkthrough"],
        enrolled=248,
        progress=45,
    ),
    Course(
        id=2,
        title="Data Analytics with Python",
        category="Data",
        instructor="Jordan Patel",
        level="Intermediate",
        description=(
            "Analyze, visualize, and communicate insights using pandas, NumPy, and "
            "storytelling dashboards."
        ),
        modules=[
            Module("Data cleaning pipelines", "1h 25m", "Complete"),
            Module("Exploratory analysis", "2h 10m", "In progress"),
            Module("Dashboards & storytelling", "1h 50m", "Locked"),
        ],
        assignments=["Data quality report", "Executive dashboard"],
        enrolled=312,
        progress=62,
    ),
    Course(
        id=3,
        title="Customer Success Playbook",
        category="Business",
        instructor="Avery Kim",
        level="All levels",
        description=(
            "Build retention workflows, onboarding journeys, and playbooks for "
            "customer health monitoring."
        ),
        modules=[
            Module("Lifecycle mapping", "55m", "Complete"),
            Module("Health score modeling", "1h 35m", "Complete"),
            Module("Renewal playbooks", "1h 05m", "In progress"),
        ],
        assignments=["Lifecycle worksheet", "Renewal strategy"],
        enrolled=189,
        progress=78,
    ),
]

DASHBOARD = {
    "learner": "Taylor Morgan",
    "role": "Learning Experience Manager",
    "active_courses": COURSES[:2],
    "completed_courses": [COURSES[2]],
    "announcements": [
        "New cohort discussion on Friday at 10:00 AM.",
        "Upload your mid-course reflections by next Tuesday.",
    ],
    "deadlines": [
        {"title": "Persona workshop", "course": "Foundations of Product Design", "due": "Mar 20"},
        {"title": "Executive dashboard", "course": "Data Analytics with Python", "due": "Mar 28"},
    ],
}


@app.route("/")
def index():
    return render_template("index.html", courses=COURSES)


@app.route("/courses")
def courses():
    return render_template("courses.html", courses=COURSES)


@app.route("/courses/<int:course_id>")
def course_detail(course_id: int):
    course = next((item for item in COURSES if item.id == course_id), None)
    if course is None:
        return redirect(url_for("courses"))
    return render_template("course_detail.html", course=course)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", dashboard=DASHBOARD)


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
