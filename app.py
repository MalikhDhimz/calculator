from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grades(absences, prelim_exam, quizzes, requirements, recitation):
    if absences >= 4:
        return "FAILED", None, None, None
    
    attendance = max(100 - (10 * absences), 0)
    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)
    prelim_grade = (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)
    
    
    required_midterm_for_passing = (75 - (0.2 * prelim_grade)) / 0.80
    required_final_for_passing = (75 - (0.2 * prelim_grade)) / 0.80
    required_midterm_for_dl = (90 - (0.2 * prelim_grade)) / 0.80
    required_final_for_dl = (90 - (0.2 * prelim_grade)) / 0.80

    return prelim_grade, required_midterm_for_passing, required_final_for_passing, required_midterm_for_dl, required_final_for_dl

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    absences = int(request.form['absences'])
    prelim_exam = float(request.form['prelim_exam'])
    quizzes = float(request.form['quizzes'])
    requirements = float(request.form['requirements'])
    recitation = float(request.form['recitation'])

    result = calculate_grades(absences, prelim_exam, quizzes, requirements, recitation)

    if result[0] == "FAILED":
        return render_template('result.html', failed=True)
    else:
        prelim_grade, req_midterm_pass, req_final_pass, req_midterm_dl, req_final_dl = result
        return render_template('result.html', failed=False, 
                               prelim_grade=prelim_grade, 
                               req_midterm_pass=req_midterm_pass, 
                               req_final_pass=req_final_pass, 
                               req_midterm_dl=req_midterm_dl, 
                               req_final_dl=req_final_dl)

if __name__ == '__main__':
    app.run(debug=True)
