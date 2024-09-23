<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prelim Grade Calculator</title>
</head>
<body style="background-color: rgb(180, 102, 102);">
    <h1 style="color: rgb(251, 34, 34);">Grade Calculator</h1>
    <hr>
    <center>
        <div style="margin: 20px; background-color: gainsboro; border-radius: 20px; width: fit-content;">
        <h2 style="color: rgb(135, 34, 251);">Prelim Grade Calculator</h2>
        <p style="color: rgb(121, 34, 251);">This calculator will calculate the prelim grade based on the number of absences, prelim exam grade, quizzes grade, requirements grade, and recitation grade.</p>
    <form action="https://calculator-aohh.onrender.com/calculate" method="GET">
        <label style="color: rgb(121, 34, 251);" for="absences">Number of Absences:</label>
        <input type="number" id="absences" name="absences" min="0" required><br>

        <label style="color: rgb(121, 34, 251);" for="prelim_exam">Prelim Exam Grade:</label>
        <input type="number" id="prelim_exam" name="prelim_exam" step="0.01" min="0" max="100" required><br>

        <label style="color: rgb(121, 34, 251);" for="quizzes">Quizzes Grade:</label>
        <input type="number" id="quizzes" name="quizzes" step="0.01" min="0" max="100" required><br>

        <label style="color: rgb(121, 34, 251);" for="requirements">Requirements Grade:</label>
        <input type="number" id="requirements" name="requirements" step="0.01" min="0" max="100" required><br>

        <label style="color: rgb(121, 34, 251);" for="recitation">Recitation Grade:</label>
        <input type="number" id="recitation" name="recitation" step="0.01" min="0" max="100" required><br>

        <button style="color: rgb(121, 34, 251);" type="submit">Calculate</button>
    </form>
    </center>
    </div>
</body>
</html>
