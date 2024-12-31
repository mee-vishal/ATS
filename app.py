import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from utils import extract_text_from_resume, compute_ats_score  # Importing functions from utils.py
import spacy

# Initialize the Flask app
app = Flask(__name__)

# Set up file upload configurations
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'docx'}  # Add file extensions you want to allow

# Load spaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Predefined industry keywords (can be extended)
industry_keywords = [
    'JavaScript', 'React', 'Node.js', 'Python', 'Machine Learning', 'Data Science', 'AI', 'Deep Learning', 
    'Software Development', 'Frontend Development', 'Backend Development', 'Database Management', 'Teamwork', 
    'Leadership', 'Problem Solving', 'Communication', 'Agile', 'Java', 'Cloud Computing', 'DevOps', 'HTML', 'CSS'
]

# Route to display the resume upload form
@app.route('/')
def index():
    return render_template('index.html')

# Route to process the uploaded resume and show extracted keywords and ATS score
@app.route('/process', methods=['POST'])
def process_resume():
    if 'resume' not in request.files:
        return render_template('index.html', message="No file uploaded")

    file = request.files['resume']
    if file.filename == '':
        return render_template('index.html', message="No selected file")

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Extract text from the resume (supports .txt, .pdf, and .docx)
    resume_text = extract_text_from_resume(file_path)

    # Get ATS score and matched keywords
    ats_score, matched_keywords = compute_ats_score(resume_text)

    # Extract all keywords from the resume using spaCy
    doc = nlp(resume_text)
    resume_keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]

    # Combine the matched keywords from the industry list and the extracted keywords from the resume
    all_keywords = list(set(industry_keywords + resume_keywords))

    # Provide feedback based on ATS score
    ats_feedback = []
    if ats_score < 5:
        ats_feedback.append("Consider adding more industry-specific keywords to improve ATS compatibility.")
    if ats_score < 7:
        ats_feedback.append("Your resume could benefit from using more action verbs in your experience section.")
    if ats_score >= 7:
        ats_feedback.append("Your resume is well-optimized for ATS. Great job!")

    # Send the results and feedback to the template
    return render_template('process.html', ats_score=ats_score, matched_keywords=matched_keywords, 
                           score=round(ats_score, 2), all_keywords=all_keywords, ats_feedback=ats_feedback)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
