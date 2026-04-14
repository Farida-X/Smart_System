class StudentAdvisorAgent:

    # Constructor to initialize agent status
    def __init__(self):
        pass

    def act(self, student):
        # Extract student data (inputs / percepts)
        gpa = student["gpa"]
        attendance = student["attendance"]
        failed_courses = student["failed_courses"]
        study_hours = student["study_hours"]

        # Rule 1: If GPA is less than 2.0 → student is at academic risk
        if gpa < 2.0:
            self.status = "At Risk"
            return "CRITICAL: Low GPA → Academic probation risk"

        # Rule 2: If GPA is high and attendance is high → excellent student
        elif gpa >= 3.5 and attendance >= 90:
            self.status = "Excellent"
            return "EXCELLENT: Eligible for honors program 🎓"

        # Rule 3: If attendance is low → warning
        elif attendance < 75:
            return "WARNING: Low attendance affects performance"

        # Rule 4: If student has failed courses → must attend remedial sessions
        elif failed_courses > 0:
            return "ALERT: Must attend remedial sessions"

        # Rule 5: If study hours are low → give advice to increase study time
        elif study_hours < 3:
            return "ADVICE: Increase daily study hours"

        # Rule 6: If GPA is good (≥ 3.0) → good performance
        elif gpa >= 3.0:
            self.status = "Good"
            return "GOOD PERFORMANCE: Keep it up!"

        # Default case → needs improvement
        else:
            return "STATUS: Needs improvement"


# ---------------- Environment ----------------
students = [
    {"gpa": 1.8, "attendance": 60, "failed_courses": 2, "study_hours": 2},
    {"gpa": 3.7, "attendance": 95, "failed_courses": 0, "study_hours": 5},
    {"gpa": 2.8, "attendance": 80, "failed_courses": 1, "study_hours": 3},
    {"gpa": 3.2, "attendance": 85, "failed_courses": 0, "study_hours": 4}
]

# ---------------- Agent ----------------
agent = StudentAdvisorAgent()

# Loop through students and apply agent decisions
for step in range(len(students)):
    student = students[step]
    action = agent.act(student)

    # Print student data and agent decision
    print(f"Step {step+1}: Student = {student}")
    print(f"Action = {action}\n")