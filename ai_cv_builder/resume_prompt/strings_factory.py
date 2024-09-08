prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, LinkedIn profile, and GitHub profile. Exclude any information that is not provided.
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
The results should be provided in html format, include only the provide information and Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_bio = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to create a professional and polished bio for the resume. The bio should:

1. **Professional Summary**: Provide a concise summary of your professional journey, highlighting key achievements and skills.
2. **Career Focus**: Clearly state your career goals and the specific role you are seeking.

- **My information:**  
  {bio}

- **Template to Use**
```
<section id="bio" class="section-block">
  <p>[Your Bio]</p>
</section>
```
The results should be provided in html format, include only the provide information and Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_technologies = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list the technologies you are proficient in. For each technology, ensure you include:

1. **Technology Category**: Clearly state the category or type of technology without the word "Technologies".
2. **Specific Technologies**: List the specific technologies or tools within each category.

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
The results should be provided in html format, include only the provide information and Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.

- **My information:**  
  {education_details}

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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to detail the work experience for a resume. For each job entry, ensure you include:

1. **Company Name and Location**: Provide the name of the company and its location.
2. **Job Title**: Clearly state your job title.
3. **Dates of Employment**: Include the start and end dates of your employment.
4. **Responsibilities and Achievements**: Describe your key responsibilities and notable achievements, emphasizing measurable results and specific contributions.

- **My information:**  
  {experience_details}

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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list additional skills relevant or not to the job. For each skill, ensure you include:

1. **Skill Category**: Clearly state the category or type of skill.
2. **Specific Skills**: List the specific skills or technologies within each category.
3. **Language Proficiency and Experience**: Include language proficiency levels.

- **My information:**  
  {skills}

- **Template to Use**
```
<section id="skills" class="section-block">
  <h2>Other Skills</h2>
  <ul class="section-list ">
    <li class="section-list-item">
      <h3 class="section-list-item-heading">[Category]</h3>
      <p class="section-list-item-content">[Specific skill or Language]</p>
    </li>
  </ul>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""
