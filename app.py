from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form method="post" action="/vaccination_status">
            <label for="regno">Registration Number:</label>
            <input type="text" id="regno" name="regno"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/vaccination_status', methods=['POST'])
def vaccination_status():
    regno = request.form['regno']
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='db',
                                        database='covid_db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT Vaccination_Status FROM Students WHERE RegNo = '{regno}'")
        status = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f"Vaccination Status of Student with Registration Number {regno}: {status}"
    except Exception as e:
        return str(e)

if
