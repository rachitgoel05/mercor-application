from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import json
from datetime import datetime
import random
import traceback

app = Flask(__name__)
CORS(app, resources={r"/employees/*": {"origins": "*"}})

import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        db = mysql.connector.connect(
            host="35.224.61.48",
            user="trial_user",
            password="trial_user_12345#",
            port=3306,
            database="MERCOR_TRIAL_SCHEMA"
        )

        if db.is_connected():
            print("Successfully connected to the database")
            # Your logic here

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if (db.is_connected()):
            print("MySQL connection is connected")
    cursor = db.cursor(dictionary=True)
    cursor.execute("SET SESSION group_concat_max_len = 1000000")
    return db,cursor

def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print("Connection Closed")

# Set of queries to just get the data from the DB to view and analyse the data parameters and make see relationships of different tables.
@app.route('/employees/MercorUsers', methods=['GET'])
def get_MercorUsers():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM MercorUsers LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)

@app.route('/employees/skills', methods=['GET'])
def get_skills():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM Skills LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)

@app.route('/employees/MercorUserSkills', methods=['GET'])
def get_MercorUserSkills():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM MercorUserSkills LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)

@app.route('/employees/UserResume', methods=['GET'])
def get_UserResume():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM UserResume LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)

@app.route('/employees/PersonalInformation', methods=['GET'])
def get_PersonalInformation():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM PersonalInformation LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)

@app.route('/employees/WorkExperience', methods=['GET'])
def get_WorkExperience():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM WorkExperience LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)

@app.route('/employees/Education', methods=['GET'])
def get_Education():
    conn, cursor = create_connection()
    limit = int(request.args.get('limit', 100000))
    offset = int(request.args.get('offset', 0))
    query = "SELECT * FROM Education LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    employees = cursor.fetchall()
    close_connection(conn)
    return jsonify(employees)


'''Query to get all the candidates in a set of 10 I have defined random descriptions as in the DB 
   I checked for all the Users the description was not present.
   The query goes like:
        Fetching only the required set of data from the DB to display over the frontend added 3 request arge: LIMIT, OFFSET & search params
        LIMIT & OFFSET will help us to get only a required set of data and on further scroll will fetch next set of data
        Seach will help us to find based on the user input parameter and then show results based on that and further scorll keeping in check
        all the 3 arguments.
        The nested select is written is for to filter out the data as if I put the search where condition in the first if condition then I was facing 
        issue in filtering out based on skills:
        eg: If i put Flutter in my search paramter the result it was returning from the GROUP_CONCAT function was just Flutter & not all the skills.
        So becuase of this reason written a nested select condiition to get all the skills but only those candidates which are elegible as per the search 
        parameter.
        
'''
@app.route('/employees', methods=['GET'])
def get_employees():
    random_descriptions = [
        "A backend developer, proficient in Python and SQL, reduced server response time by 40%.",
        "An iOS developer, fluent in Swift, released an app update that increased user retention by 25%.",
        "A front-end engineer, skilled in React and CSS, led a redesign that boosted website traffic by 30%.",
        "A DevOps specialist, experienced with AWS and Docker, decreased deployment time by 50%.",
        "A machine learning engineer, familiar with TensorFlow and scikit-learn, improved model accuracy by 15%.",
        "A UX designer, adept at Figma and Sketch, conducted user tests that enhanced usability scores by 20%.",
        "A cybersecurity expert, knowledgeable in ethical hacking, implemented protocols that reduced security breaches by 60%.",
        "A data scientist, skilled in R and Python, created dashboards that improved data insights by 35%.",
        "A software architect, experienced in microservices, led a project that increased system scalability by 45%.",
        "A full-stack developer, proficient in Node.js and Angular, built an application that increased user engagement by 50%.",
        "A QA engineer, familiar with Selenium and JIRA, improved test coverage by 25%.",
        "A product manager, experienced in Agile methodologies, launched a feature that increased user adoption by 40%.",
        "A blockchain developer, skilled in Solidity, created a smart contract that reduced transaction costs by 30%.",
        "An AI specialist, familiar with natural language processing, developed a chatbot that enhanced customer support efficiency by 35%.",
        "A cloud engineer, experienced with Azure and Kubernetes, optimized cloud resource usage by 40%.",
        "A database administrator, proficient in MySQL and PostgreSQL, improved query performance by 20%.",
        "A mobile app developer, skilled in Kotlin, released a new feature that increased app downloads by 25%.",
        "A game developer, familiar with Unity and C#, created a game level that boosted player retention by 15%.",
        "A systems analyst, experienced in ERP systems, streamlined processes that increased productivity by 30%.",
        "A technical writer, skilled in API documentation, produced guides that improved developer onboarding time by 50%."
    ]

    try:
        conn, cursor = create_connection()
        print("request",request.args)
        limit = int(request.args.get('limit', 0))
        offset = int(request.args.get('offset', 0))
        searchTerm = request.args.get('search', '')
        print("limit",limit, "offset",offset)
        query = "SELECT \
                User.userId,  \
                User.name,  \
                User.fullTimeAvailability,  \
                User.partTimeAvailability,  \
                GROUP_CONCAT(DISTINCT SkillName.skillName) AS skillNames, \
                GROUP_CONCAT(DISTINCT Experience.startDate) AS jobStartDate, \
                GROUP_CONCAT(DISTINCT Experience.endDate) AS jobEndDate, \
                Experience.resumeId as resumeid, \
                PersonalInfo.location \
            FROM MercorUsers AS User \
            LEFT OUTER JOIN MercorUserSkills AS UserSkills ON UserSkills.userId = User.userId \
            LEFT OUTER JOIN Skills AS SkillName ON SkillName.skillId = UserSkills.skillId \
            LEFT OUTER JOIN UserResume AS Resume ON Resume.userId = User.userId \
            LEFT OUTER JOIN WorkExperience AS Experience ON Experience.resumeId  = Resume.resumeId \
            LEFT OUTER JOIN PersonalInformation AS PersonalInfo ON PersonalInfo.resumeId = Resume.resumeId \
            WHERE (UserSkills.isPrimary = 0) \
                AND ( \
                    User.userId IN ( \
                        SELECT User.userId  \
                        FROM MercorUsers AS User \
                        LEFT OUTER JOIN MercorUserSkills AS UserSkills ON UserSkills.userId = User.userId \
                        LEFT OUTER JOIN Skills AS SkillName ON SkillName.skillId = UserSkills.skillId \
                        WHERE  \
                            (User.name LIKE CONCAT('%', %s, '%') OR %s IS NULL) \
                            OR (SkillName.skillName LIKE CONCAT('%', %s, '%') OR %s IS NULL) \
                    ) \
                ) \
            GROUP BY User.userId, User.name, User.fullTimeAvailability, User.partTimeAvailability, PersonalInfo.location \
            LIMIT %s OFFSET %s; "
        cursor.execute(query, (searchTerm, searchTerm, searchTerm, searchTerm, int(limit),int(offset)))
        employees = cursor.fetchall()
        print("employees",employees)

        for item in employees:
            if item['location']:
                temp = json.loads(item['location'])
                item['location'] = temp

            if item['skillNames']:
                item['skillNames'] = item['skillNames'].split(',')
            try:
                if item['jobStartDate'] and list(map(int, filter(None, item['jobStartDate'].split(',')))):
                    pass
            except:
                print("here")
                newJobStartDate = []
                for value in item['jobStartDate'].split(','):
                    if len(value.split('-')) > 1:
                        newJobStartDate.append(value.split('-')[1])
                    else:
                        newJobStartDate.append(value)
                item['jobStartDate'] = (',').join(newJobStartDate)
                print(item['jobStartDate'])
            if item['jobStartDate'] and len(list(map(int, filter(None, item['jobStartDate'].split(','))))):
                item['jobStartDate'] = min(map(int, filter(None, item['jobStartDate'].split(','))))
            
            if item['jobEndDate'] and len(list(map(int, filter(None, item['jobEndDate'].split(','))))):
                item['jobEndDate'] = min(map(int, filter(None, item['jobEndDate'].split(','))))

            if type(item['jobEndDate']) == int and type(item['jobStartDate']) == int:
                item['experience'] = item['jobEndDate'] - item['jobStartDate']
            elif type(item['jobStartDate']) == type(int):
                item['experience'] = datetime.now().year - item['jobStartDate']
            else:
                item['experience'] = 0
            item['summary'] = random_descriptions[random.randint(0,len(random_descriptions)-1)]

        close_connection(conn)
        return jsonify(employees)
    except Exception as e:
        close_connection(conn)
        traceback.print_exc()
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

'''
    This query fetches candidates based out of UserId which it clicks on.
    The query fetches all the required parameters that needs to be displayed on the frontend.
    Then filtering & correcting the formatting of the data and removing all the empty data so that the Application should be 
    processing all the information and the frontend should only be used to display data and remove the cluttered data in backend only.
'''
@app.route('/employees/<id>', methods=['GET'])
def get_employee(id):
    conn, cursor = create_connection()
    query = "SELECT \
            User.userId,  \
            User.name,  \
            User.email,  \
            User.phone, \
            User.profilePic, \
            User.lastLogin, \
            User.fullTimeStatus, \
            User.workAvailability, \
            User.fullTime, \
            User.fullTimeAvailability, \
            User.fullTimeSalary, \
            User.fullTimeSalaryCurrency, \
            User.partTimeSalary, \
            User.partTimeSalaryCurrency, \
            User.partTime, \
            User.partTimeAvailability, \
            User.isActive, \
            User.Summary, \
            User.fullTimeAvailability,  \
            User.partTimeAvailability,  \
            CONCAT('[',     \
                    GROUP_CONCAT(   \
                        DISTINCT JSON_OBJECT(   \
                            'skillName', IFNULL(SkillName.skillName, 'N/A'),    \
                            'skillValue', IFNULL(SkillName.skillValue, 'N/A')   \
                        ) ORDER BY SkillName.skillName SEPARATOR ', '   \
                    ),  \
                ']') AS skillJSON,  \
            Resume.resumeId, \
            Resume.url as resumeURL, \
            Resume.filename as resumeFileName, \
            Resume.ocrGithubUsername as github, \
            Resume.isInvitedToInterview as resumeInvitation, \
            PersonalInfo.name as PersonalInfoName, \
            PersonalInfo.location, \
            PersonalInfo.phone as PhoneNo, \
            CONCAT('[',     \
                GROUP_CONCAT( \
                    DISTINCT JSON_OBJECT( \
                        'workExperienceCompany', IFNULL(WorkExperience.company, 'N/A'),  \
                        'workExperienceRole', IFNULL(WorkExperience.role, 'N/A'),  \
                        'workExperienceStartDate', IFNULL(WorkExperience.startDate, 'N/A'),  \
                        'workExperienceEndDate', IFNULL(WorkExperience.endDate, 'N/A'),  \
                        'workExperienceDescription', IFNULL(WorkExperience.description, 'N/A'),  \
                        'workExperienceLocationCity', IFNULL(WorkExperience.locationCity, 'N/A'),  \
                        'workExperienceLocationCountry', IFNULL(WorkExperience.locationCountry, 'N/A') \
                    ) ORDER BY WorkExperience.startDate SEPARATOR ', ' \
                ), \
                ']') AS workExperienceJSON, \
            CONCAT('[',     \
                GROUP_CONCAT(  \
                    DISTINCT JSON_OBJECT( \
                        'EducationDegree', IFNULL(Education.degree, 'N/A'), \
                        'EducationMajor', IFNULL(Education.major, 'N/A'), \
                        'EducationSchool', IFNULL(Education.school, 'N/A'), \
                        'EducationStartDate', IFNULL(Education.startDate, 'N/A'), \
                        'EducationEndDate', IFNULL(Education.endDate , 'N/A') \
                    ) ORDER BY Education.startDate SEPARATOR ', ' \
                ), \
               ']' ) AS educationJSON \
        FROM MercorUsers AS User \
        LEFT OUTER JOIN MercorUserSkills AS UserSkills ON UserSkills.userId = User.userId \
        LEFT OUTER JOIN Skills AS SkillName ON SkillName.skillId = UserSkills.skillId \
        LEFT JOIN UserResume AS Resume ON Resume.userId = User.userId \
        LEFT JOIN PersonalInformation AS PersonalInfo ON PersonalInfo.resumeId = Resume.resumeId \
        LEFT JOIN WorkExperience AS WorkExperience ON WorkExperience.resumeId = Resume.resumeId \
        LEFT JOIN Education AS Education ON Education.resumeId = Resume.resumeId \
        WHERE User.userId = %s \
        GROUP BY User.userId, User.name, User.email, User.phone, User.profilePic, \
            User.lastLogin, User.fullTimeStatus, User.workAvailability, User.fullTime, \
            User.fullTimeAvailability, User.fullTimeSalary, User.fullTimeSalaryCurrency, \
            User.partTimeSalary, User.partTimeSalaryCurrency, User.partTime, User.partTimeAvailability, \
            User.isActive, User.Summary, Resume.resumeId, resumeURL, resumeFileName, github, \
            resumeInvitation, PersonalInfoName,location, PhoneNo" 
    cursor.execute(query, (id,))
    employee = cursor.fetchone()
    jsonify(employee)
    if employee['educationJSON']:
        employee['educationJSON'] = json.loads(employee['educationJSON'])
    if employee['location']:
        employee['location'] = json.loads(employee['location'])
    if employee['workExperienceJSON']:
        employee['workExperienceJSON'] = json.loads(employee['workExperienceJSON'])
        itemsToDelete = []
        for item in range(0,len(employee['workExperienceJSON'])):
            if not (employee['workExperienceJSON'][item]['workExperienceCompany'] and \
                    employee['workExperienceJSON'][item]['workExperienceRole'] ):
                itemsToDelete.append(item)
        for index in sorted(itemsToDelete,reverse = True):
            del employee['workExperienceJSON'][index]
    
    if employee['skillJSON']:
        employee['skillJSON'] = json.loads(employee['skillJSON'])
    if employee['PhoneNo']:
        print(json.loads(employee['PhoneNo']))
        employee['PhoneNo'] = json.loads(employee['PhoneNo'])[0]
    experience = 0
    minStartDate = float('inf')
    maxEndDate = 0
    for item in employee['workExperienceJSON']:
        try:
            minStartDate = min(minStartDate,int(item['workExperienceStartDate']))
            maxEndDate = max(maxEndDate, int(item['workExperienceEndDate']))
        except:
            continue
    print(maxEndDate,minStartDate)
    employee['experience'] = maxEndDate - minStartDate
    close_connection(conn)
    return jsonify(employee)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)
