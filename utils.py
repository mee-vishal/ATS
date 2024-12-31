import spacy
import PyPDF2
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Predefined industry keywords (can be extended)
industry_keywords = [
    'JavaScript', 'React', 'Node.js', 'Python', 'Machine Learning', 'Data Science', 'AI', 'Deep Learning', 
    'Software Development', 'Frontend Development', 'Backend Development', 'Database Management', 'Teamwork', 
    'Leadership', 'Problem Solving', 'Communication', 'Agile', 'Java', 'Cloud Computing', 'DevOps', 'HTML', 'CSS'
]

# Function to extract text from resume (PDF, DOCX, or TXT)
def extract_text_from_resume(file_path):
    # Handling plain text files
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    # Handling PDF files
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
    # Handling DOCX files
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        text = ''
        for para in doc.paragraphs:
            text += para.text
    else:
        raise ValueError("Unsupported file format")
    
    return text

# Function to compute ATS score
def compute_ats_score(resume_text):
    if not resume_text:
        print("Resume text is empty!")
        return 0, []

    print("Extracted resume text:", resume_text)  # Debugging step

    # Extract keywords from the resume using spaCy
    doc = nlp(resume_text)
    resume_keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    print("Extracted resume keywords:", resume_keywords)  # Debugging step

    # Ensure all keywords are lowercase for consistent comparison
    industry_keywords_lower = [keyword.lower() for keyword in industry_keywords]

    # Find exact matches for industry keywords in the resume text
    resume_text_lower = resume_text.lower()  # Convert resume text to lowercase
    matched_keywords = [keyword for keyword in industry_keywords_lower if keyword in resume_text_lower]
    print("Matched keywords (exact match):", matched_keywords)  # Debugging step

    # If no exact matches found, use TF-IDF and cosine similarity to check for semantic matches
    if not matched_keywords:
        # Vectorize the industry keywords and resume keywords
        vectorizer = TfidfVectorizer()
        all_keywords = industry_keywords_lower + resume_keywords
        tfidf_matrix = vectorizer.fit_transform(all_keywords)

        # Compute cosine similarity between the resume and industry keywords
        similarity_matrix = cosine_similarity(tfidf_matrix)
        similarity_score = similarity_matrix[0, len(industry_keywords_lower):]  # similarity with the resume keywords

        print("Similarity scores:", similarity_score)  # Debugging step

        # Check if the similarity score is above a threshold (e.g., 0.1 or 0.2)
        threshold = 0.1  # Lowered threshold for more relaxed matching
        for i in range(len(industry_keywords_lower)):
            if i < len(similarity_score) and similarity_score[i] > threshold:
                matched_keywords.append(industry_keywords_lower[i])

    print("Final matched keywords:", matched_keywords)  # Debugging step

    # Calculate final ATS score based on how many industry keywords are found in the resume
    ats_score = (len(matched_keywords) / len(industry_keywords)) * 10
    return ats_score, matched_keywords
