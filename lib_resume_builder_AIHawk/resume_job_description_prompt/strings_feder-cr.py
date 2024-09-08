prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, LinkedIn profile, and GitHub profile.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

- **My information:**  
  {personal_information}

- **Template to Use**
```
<header>
  <h1>[Name and Surname]</h1>
  <div class="contact-info"> 
    <p class="fas fa-map-marker-alt">
      <span>[Your City, Your Country]</span>
    </p> 
    <p class="fas fa-phone">
      <span>[Your Prefix Phone number]</span>
    </p> 
    <p class="fas fa-envelope">
      <span>[Your Email]</span>
    </p> 
    <p class="fab fa-linkedin">
      <a href="[Link LinkedIn account]">LinkedIn</a>
    </p> 
    <p class="fab fa-github">
      <a href="[Link GitHub account]">GitHub</a>
    </p> 
  </div>
</header>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_bio = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to create a professional and polished bio for the resume, ensuring it aligns with the provided job description. For the bio, ensure you include:

1. **Professional Summary**: Provide a concise summary of your professional journey, highlighting key achievements and skills.
2. **Career Focus**: Clearly state your career goals and the specific role you are seeking.

Ensure the information is clearly presented and emphasizes points that align with the job description.

- **My information:**  
  {bio}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="bio" class="section-block">
  <p>[Your Bio]</p>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```"
"""

prompt_technologies = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list the technologies you are proficient in, ensuring it aligns with the provided job description. For each technology, ensure you include:

1. **Technology Category**: Clearly state the category or type of technology without the word "Technologies".
2. **Specific Technologies**: List the specific technologies or tools within each category.

Ensure that the technologies listed are relevant and accurately reflect your expertise in the field.

- **My information:**  
  {technologies}

- **Template to Use**
```
<section id="technologies" class="section-block">
  <h2>Technologies</h2>
  <ul class="section-list ">
    <li class="section-list-item">
      <h3 class="section-list-item-heading">[Technology Category]</h3>
      <p class="section-list-item-content">[Specific Technologies]</p>
    </li>
  </ul>
</section>  
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume, ensuring it aligns with the provided job description. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.
3. **GPA**: Include your GPA if it is strong and relevant.

Ensure the information is clearly presented and emphasizes academic achievements that align with the job description.

- **My information:**  
  {education_details}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="education" class="section-block">
  <h2>Education</h2>
  <ul class="section-list">
    <li class="section-list-item section-list-item--start">
      <h3 class="section-list-item-heading">[Start Year] - [End Year]</h3>
      <div class="section-list-body">
        <header class="section-list-body-header">
          <span class="section-list-body-header-role">[Degree] in [Field of Study] | GPA:
            [Your GPA]</span>
          <span class="section-list-body-header-employer">[University Name] — [Location]</span>
        </header>
      </div>
    </li>
  </ul>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_working_experience = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to detail the work experience for a resume, ensuring it aligns with the provided job description. For each job entry, ensure you include:

1. **Company Name and Location**: Provide the name of the company and its location.
2. **Job Title**: Clearly state your job title.
3. **Dates of Employment**: Include the start and end dates of your employment.
4. **Responsibilities and Achievements**: Describe your key responsibilities and notable achievements, emphasizing measurable results and specific contributions.

Ensure that the descriptions highlight relevant experience and align with the job description.

- **My information:**  
  {experience_details}

- **Job Description:**  
  {job_description}

- **Template to Use**
```
<section id="work-experience" class="section-block">
  <h2>Work Experience</h2>
  <ul class="section-list">

    <li class="section-list-item section-list-item--start">
      <h3 class="section-list-item-heading">[Start Date] - [End Date]</h3>
      <div class="section-list-body">
        <header class="section-list-body-header">
          <span class="section-list-body-header-role">[Your Job Title]</span>
          <span class="section-list-body-header-employer">[Company Name] — [Location]</span>
        </header>
        <ul class="section-list-body-content">
          <li>[Describe your responsibilities and achievements in this role]</li>
        </ul>
      </div>
    </li>
  </ul>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_skills = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list additional skills relevant or not to the job based on the provided job description. For each skill, ensure you include:

1. **Skill Category**: Clearly state the category or type of skill.
2. **Specific Skills**: List the specific skills or technologies within each category.
3. **Language Proficiency and Experience**: Include language proficiency levels.

Ensure that the skills listed are relevant and accurately reflect your expertise in the field.

- **My information:**  
  {skills}

- **Job Description:**  
  {job_description}

- **Template to Use**
'''
<section id="skills" class="section-block">
  <h2>Other Skills</h2>
  <ul class="section-list ">
    <li class="section-list-item">
      <h3 class="section-list-item-heading">[Category]</h3>
      <p class="section-list-item-content">[Specific skill or Language]</p>
    </li>
  </ul>
</section>
'''
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

summarize_prompt_template = """
As a seasoned HR expert, your task is to identify and outline the key skills and requirements necessary for the position of this job. Use the provided job description as input to extract all relevant information. This will involve conducting a thorough analysis of the job's responsibilities and the industry standards. You should consider both the technical and soft skills needed to excel in this role. Additionally, specify any educational qualifications, certifications, or experiences that are essential. Your analysis should also reflect on the evolving nature of this role, considering future trends and how they might affect the required competencies.

Rules:
Remove boilerplate text
Include only relevant information to match the job description against the resume

# Analysis Requirements
Your analysis should include the following sections:
Technical Skills: List all the specific technical skills required for the role based on the responsibilities described in the job description.
Soft Skills: Identify the necessary soft skills, such as communication abilities, problem-solving, time management, etc.
Educational Qualifications and Certifications: Specify the essential educational qualifications and certifications for the role.
Professional Experience: Describe the relevant work experiences that are required or preferred.
Role Evolution: Analyze how the role might evolve in the future, considering industry trends and how these might influence the required skills.

# Final Result:
Your analysis should be structured in a clear and organized document with distinct sections for each of the points listed above. Each section should contain:
This comprehensive overview will serve as a guideline for the recruitment process, ensuring the identification of the most qualified candidates.

# Job Description:
```
{text}
```

---

# Job Description Summary"""



