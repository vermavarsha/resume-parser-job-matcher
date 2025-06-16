from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def prepare_resume_text(resume):
    return ' '.join([
        ', '.join(resume.get('skills', [])),
        ' '.join(resume.get('experience', [])),
        ' '.join(resume.get('education', []))
    ])

def compute_embeddings(resumes,job_descriptions):
    resume_texts = [prepare_resume_text(r) for r in resumes]
    job_texts = [j['text'] for j in job_descriptions]

    resume_embeddings = model.encode(resume_texts, convert_to_tensor=True)
    job_embeddings = model.encode(job_texts, convert_to_tensor=True)

    return resume_embeddings, job_embeddings


# Match
def match_resumes_to_jobs(resumes, job_descriptions, top_n=5):
    resume_embeddings, job_embeddings = compute_embeddings(resumes, job_descriptions)
    match_results = []
    for j_idx, job in enumerate(job_descriptions):
        job_scores = []
        for r_idx, resume in enumerate(resumes):
            sim = util.cos_sim(job_embeddings[j_idx], resume_embeddings[r_idx])
            score = round(float(sim[0][0]) * 100, 2)

            job_scores.append({
                'Job Title': job['title'],
                'Resume Name': resume['name'],
                'Match Score (%)': score,
                'Skills': ', '.join(resume['skills']),
                'years_of_experience': ', '.join(resume['experience']),
                'Email': resume['email'],
                'Phone': resume['phone']
            })

        top_matches = sorted(job_scores, key=lambda x: x['Match Score (%)'], reverse=True)[:top_n]
        match_results.extend(top_matches)
    return match_results
