INITIAL_RESPONSE = "Welcome to Ecoute 👋"
contextual_data = """
Sajid Javed, a Full-stack Software Engineer from Dubai, UAE, boasts 4 years of experience across various aspects of software development. Proficient in a wide range of languages including JavaScript, TypeScript, Java, Kotlin, Python, Swift, CSS, C++, HTML, YAML, XML, and SQL, Sajid specializes in Web Development with Node.js, React, Express, Mobile Development using Android SDK, iOS SDK, React Native, and Cloud Services involving AWS and Firebase.

At Darkblock, he led the design and development of a full-stack web application focused on processing, analyzing, minting, and showcasing Darkblocks. His role was pivotal in enhancing the company's software processes and building scalable AWS infrastructures. As a solo engineer, he managed the entire development lifecycle, emphasizing scalability and performance.

During his tenure as a Mobile Developer & Technical Writer, Sajid worked remotely, handling diverse software projects and collaborating with clients worldwide. He was known for his quality deliverables and timely execution, earning consistent positive feedback.

At Dads Agree, he significantly reduced content deployment time by 20% through XML web form process optimization. Sajid also played a key role in developing custom e-commerce themes and managing the company's largest custom migration project, contributing to the platform's technical accuracy and coherence.

As a Junior Android Developer at Shopsy.pk, he enhanced the user interface and experience of the Android app, which led to a 17% increase in positive user reviews. His expertise in serial communications and database design was instrumental in developing intuitive GUIs, and he also mentored interns, fostering a learning environment.
"""

def create_prompt(transcript):
    return f"""You are a casual pal, genuinely interested in the conversation at hand. A poor transcription of conversation is given below. Let me introduce myself first and keep this as context in our conversations ahead, so {contextual_data}
    
Transcription: {transcript}

Provide a response in two parts. First, give a brief and direct answer in square brackets. This should be a concise summary. Next, offer an expanded explanation in a separate paragraph, diving deeper into the subject without repeating the summary. This expanded section should provide additional insights, examples, or details that were not included in the brief answer. Avoid asking for repetition or clarification."""