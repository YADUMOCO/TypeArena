from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# ================= Beginner (short sentences, 50)
beginner_sentences = [
    "Practice makes perfect.",
    "Coding is fun and rewarding.",
    "Always keep learning new things.",
    "Typing faster needs regular practice.",
    "Success comes from hard work.",
    "Stay calm and code on.",
    "Focus improves typing speed.",
    "Read more to type better.",
    "Mistakes are lessons in disguise.",
    "Patience leads to progress.",
    "Keep trying every day.",
    "Learning never stops.",
    "Small steps lead to success.",
    "Consistency beats intensity.",
    "Typing is a useful skill.",
    "Never give up on learning.",
    "Start small and grow.",
    "Hard work pays off.",
    "Practice daily for improvement.",
    "Challenge yourself every day.",
    "Typing speed improves with effort.",
    "Believe in yourself always.",
    "Slow and steady wins.",
    "Learning builds confidence.",
    "Errors are opportunities to learn.",
    "Write code every day.",
    "Stay motivated and focused.",
    "Begin with simple exercises.",
    "Repetition strengthens memory.",
    "Time management is important.",
    "Stay positive always.",
    "Set realistic goals.",
    "Daily practice is key.",
    "Learn from your mistakes.",
    "Be patient with yourself.",
    "Start early and practice.",
    "Keep a steady pace.",
    "Typing helps productivity.",
    "Accuracy matters more than speed.",
    "Stay consistent with practice.",
    "Focus on one task at a time.",
    "Never stop improving.",
    "Celebrate small achievements.",
    "Keep learning new words.",
    "Practice typing sentences.",
    "Typing helps brain focus.",
    "Beginner exercises are simple.",
    "Start typing short sentences.",
    "Daily effort leads to growth.",
    "Short sentences are easy to type."
]

# ================= Intermediate (medium sentences, 50)
intermediate_sentences = [
    "Programming teaches problem solving and logical thinking skills.",
    "Consistency and focus are key to achieving long term success.",
    "Artificial intelligence is transforming industries around the globe.",
    "Learning new technologies helps in adapting to future challenges.",
    "Teamwork and communication are vital for software development.",
    "Typing faster improves productivity in daily digital tasks.",
    "The Internet connects people across diverse cultures and countries.",
    "Persistence is the secret ingredient of all great achievements.",
    "Organizing your thoughts clearly leads to better coding results.",
    "Never stop exploring new tools and programming frameworks.",
    "Software testing ensures bugs are caught early in development.",
    "Cloud computing provides flexibility and scalable solutions for businesses.",
    "Effective learning requires focus, discipline, and regular practice.",
    "Open-source contributions improve skills and community engagement.",
    "Time management is essential for meeting project deadlines.",
    "Problem solving improves with consistent practice and learning.",
    "Logical thinking is strengthened through coding challenges.",
    "Daily coding exercises build muscle memory for syntax.",
    "Reading technical blogs helps expand programming knowledge.",
    "Documenting code improves maintainability for future developers.",
    "Debugging effectively saves time and frustration in programming.",
    "Consistent practice enhances typing speed and accuracy.",
    "Understanding algorithms improves coding efficiency.",
    "Software development involves creativity, logic, and patience.",
    "Learning version control is important for collaborative coding.",
    "Programming exercises improve problem-solving capabilities.",
    "Continuous learning keeps developers updated with trends.",
    "Effective communication ensures team productivity in projects.",
    "Intermediate coding challenges help strengthen logical thinking.",
    "Testing code thoroughly avoids unexpected errors.",
    "Collaboration tools like GitHub streamline team development.",
    "Typing skills improve with regular, focused practice.",
    "Understanding data structures is essential for coding efficiency.",
    "Clear code enhances readability and maintainability.",
    "Analytical thinking helps solve complex coding problems.",
    "Intermediate exercises prepare you for advanced challenges.",
    "Proper planning reduces errors in software projects.",
    "Debugging skills improve with repeated practice.",
    "Learning frameworks accelerates application development.",
    "Practicing algorithms improves logical reasoning.",
    "Project management skills aid in successful coding projects.",
    "Writing clean code is a professional habit.",
    "Time tracking improves efficiency during practice sessions.",
    "Understanding coding concepts deeply reduces errors.",
    "Collaborative coding builds teamwork and problem-solving skills.",
    "Regular practice improves both typing speed and accuracy.",
    "Learning by doing is more effective than just reading.",
    "Organizing code well leads to better project maintenance.",
    "Intermediate exercises bridge beginner and advanced levels."
]

# ================= Advanced (long sentences, 50)
advanced_sentences = [
    "The rapid advancement of technology has completely redefined the way humans interact, communicate, and share knowledge across the globe.",
    "Machine learning algorithms analyze large volumes of data to discover patterns, enabling predictions and decisions with remarkable accuracy.",
    "The effectiveness of artificial intelligence depends on the quality of training data and the ethical frameworks that guide its usage.",
    "Innovation requires a balance between creativity, technical expertise, and a deep understanding of user needs and market trends.",
    "As technology evolves, professionals must continue learning to remain relevant and adapt to the dynamic global workforce.",
    "The combination of automation and human intelligence is shaping the next generation of smart and efficient workplaces.",
    "Cybersecurity has become an essential priority as more data moves online and digital privacy becomes increasingly vulnerable.",
    "The integration of artificial intelligence in healthcare has the potential to revolutionize diagnosis, treatment, and patient care.",
    "Sustainable technology solutions play a critical role in addressing environmental challenges and ensuring long term progress.",
    "The digital transformation of industries is accelerating innovation while redefining how businesses compete and collaborate.",
    "Deep learning models have significantly improved computer vision tasks, including image recognition and object detection.",
    "Effective project management ensures teams meet deadlines while maintaining high standards of quality.",
    "Cloud technologies allow organizations to scale applications seamlessly while reducing infrastructure costs.",
    "Ethical considerations are vital when designing algorithms that impact millions of users globally.",
    "Continuous professional development is necessary for adapting to rapid technological and industrial changes.",
    "Advanced programming requires understanding both theory and practical application of complex concepts.",
    "Artificial intelligence systems must be trained responsibly to avoid bias and ensure fairness in decision-making.",
    "The future of work will increasingly rely on human-AI collaboration for optimal performance.",
    "Data privacy regulations have reshaped how companies collect, store, and process personal information.",
    "Learning advanced algorithms equips developers to handle real-world problems more efficiently.",
    "Automated testing frameworks improve software reliability and reduce manual testing efforts significantly.",
    "The field of bioinformatics leverages computing to understand complex biological systems and datasets.",
    "Quantum computing promises to solve problems that classical computers cannot handle efficiently.",
    "Global connectivity through the Internet has transformed education, business, and social interactions.",
    "Augmented reality applications enhance learning experiences by providing immersive, interactive content.",
    "Leadership in technology requires both vision and the ability to execute strategic initiatives effectively.",
    "Blockchain technology ensures transparency and security in digital transactions across industries.",
    "Resilient software systems can adapt to changes while maintaining stability and performance.",
    "Innovative solutions often emerge from interdisciplinary collaboration between experts from various fields.",
    "The scalability of cloud-based applications enables businesses to grow without significant hardware investments.",
    "Developers must balance performance optimization with code readability and maintainability.",
    "Understanding human-computer interaction principles improves user interface and user experience design.",
    "Automated data analysis accelerates insights that inform business and research decisions.",
    "Digital ethics emphasizes responsible technology use to benefit society and minimize harm.",
    "The convergence of AI, IoT, and big data is shaping smart cities and intelligent infrastructure.",
    "Professional development involves not only technical skills but also communication, leadership, and problem-solving abilities.",
    "Emerging technologies require continuous learning to remain competitive and innovative in the workforce.",
    "Natural language processing enables machines to comprehend, interpret, and generate human language effectively.",
    "Robust software architecture ensures long-term maintainability, scalability, and system reliability.",
    "Technological innovation often requires experimentation, failure, and iterative improvement to achieve success.",
    "Data visualization helps stakeholders understand complex datasets and make informed decisions.",
    "The ethical use of AI involves transparency, accountability, and fairness in algorithmic decision-making.",
    "Global collaboration platforms allow distributed teams to work efficiently across time zones.",
    "Cyber threats are becoming increasingly sophisticated, necessitating advanced cybersecurity measures.",
    "Advanced algorithms are crucial for optimizing performance in large-scale software applications.",
    "The responsible deployment of AI has the potential to solve critical societal challenges.",
    "Understanding statistical principles is fundamental for effective data analysis and interpretation.",
    "The combination of creativity, technical expertise, and problem-solving skills drives innovation.",
    "Automation of repetitive tasks allows humans to focus on creative and strategic work.",
    "Effective communication ensures technology solutions align with user needs and organizational goals."
]

# ================= Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sentence/<level>')
def get_sentence(level):
    if level == "beginner":
        return jsonify({'sentence': random.choice(beginner_sentences)})
    elif level == "intermediate":
        return jsonify({'sentence': random.choice(intermediate_sentences)})
    elif level == "advanced":
        return jsonify({'sentence': random.choice(advanced_sentences)})
    else:
        return jsonify({'sentence': "Invalid level selected."})

if __name__ == '__main__':
    app.run(debug=True)
