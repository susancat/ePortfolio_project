
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ePortfolio_project.settings')

import django 
django.setup()
from ESE.models import Student, Assessor, Assignment, Feedback, Competency, Module, Student_comp, User, Profile

def populate():

        student_one_assignment =[
                {"owner": "student1", "assignment_ID": "00268235",
                "SID": "2423289","module_ID": "COMPSCI4023","title": "HCI Reflection",
                "description": "A personal reflection on HCI",
                "text": "The report will explore the main issues of team project in three parts: process, outcome and"
                "reflection. In the first aspect, it will describe the team process used within our group, the challenges"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "will discuss the successes obtained as well as the weaknesses, limitations and avenues for future"
                "work. Lastly, the reflections include what we gained in peer-review to improve paper quality and"
                "what I learned useful."}, 
                {"owner": "student1", "assignment_ID": "00268268",
                "SID": "2423289","module_ID": "COMPSCI4023","title": "HCI Thesis",
                "description": "A team-based thesis of HCI",
                "text": "We met twice weekly, each meeting lasted for about two hours. In the meetings, we followed the"
                "schedule from course instruction to choose some themes at each stage. Then each of us expressed"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "our opinions about the themes freely, discussed and decided for what we were going to do and how. "
                "One of us took notes for the key points and formed a weekly report. "},
                {"owner": "student1", "assignment_ID": "00268234",
                "SID": "2423289","module_ID": "COMPSCI5059","title": "Software Engineering: software design",
                "description": "A software design required by on-site mentor.",
                "text": "The report will explore the main issues of team project in three parts: process, outcome and"
                "reflection. In the first aspect, it will describe the team process used within our group, the challenges"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "will discuss the successes obtained as well as the weaknesses, limitations and avenues for future"
                "work. Lastly, the reflections include what we gained in peer-review to improve paper quality and"
                "what I learned useful."},
                {"owner": "student1", "assignment_ID": "00268295",
                "SID": "2423289","module_ID": "COMPSCI5059","title": "Software Engineering: pattern design",
                "description": "A pattern design of a software required by the on-site mentor. ",
                "text": "At the beginning, we spent much time on achieving consensus about choosing the design project."
                "One member suggested to design a visual feedback application. But the idea was vague and I"
                "misunderstood it as something with face recognizing technology which can get people’s real"
                "thought/emotion. Then based on some related literatures, we agreed the design should be an"
                "application that motivate museum/gallery visitors to equally engage in creative expression and get"
                "enhanced visiting experience from creation involvement."},
                {"owner": "student1", "assignment_ID": "00268197",
                "SID": "2423289","module_ID": "COMPSCI5029","title": "Tools about Software Project Management",
                "description": "A personal reflection on HCI",
                "text": "The second significant decision was about prototype and its interface. From week 3 to 4, each of us"
                "designed an interface for the low-fidelity device. We merged our idea as well as considered about"
                "its usability then made a preliminary interface design. Next step was that we completed a"
                "hand-made over-sized prototype together in week 5. It was really interesting because we experienced"
                "a creative process within a team."},
                {"owner": "student1", "assignment_ID": "00268299",
                "SID": "2423289","module_ID": "COMPSCI5029","title": "Software Project Management Practical Principle",
                "description": "A practical application of software project management principles",
                "text": "The third important decision was about evaluation procedure and methods. We had to decide on"
                "how we exactly conduct the experiment. I wrote a draft on briefing, experiment introduction,"
                "debriefing and possible questions for questionnaire. I suggested to adopt close-ended questions with"
                "5-point Likert Scale as well as open-ended questions to measure participants’ motivation to use"
                "visual feedback application in a real scenario and their attitudes about our design. Then other"
                "members developed full version of instructions and questionnaire."},
                {"owner": "student1", "assignment_ID": "00268135",
                "SID": "2423289","module_ID": "COMPSCI4039","title": "Coding in Practice",
                "description": "A coding test designed by on-site mentor",
                "text": "Peer-review used to improve the quality of the project in the following points: in final paper we"
                "added more theoretical supports in HCI concepts for our design; we did an extra third iteration only"
                "for questions about colors and positions of buttons. Before this we did minor changes after each"
                "iteration; in final iteration we designed some tasks ask participants to complete rather than let them"
                "interact with device intuitively. This improved respondents’ understanding towards the device."
                "what I learned useful."},
                {"owner": "student1", "assignment_ID": "00268196",
                "SID": "2423289","module_ID": "COMPSCI4039","title": "team project",
                "description": "Cooperate with other colleagues in the company",
                "text": "During the process of project, I think the biggest challenge is achieving consensus for every crucial"
                "decision. For a four-member team without related academic training (e.g. in questionnaire design"
                "and analysis), different opinions resulted in debating, we did not have a round conflicts solving"
                "mechanism and final decisions were not always the best."} ]

        student_two_assignment =[
                {"owner": "student2", "assignment_ID": "00268335",
                "SID": "2214170","module_ID": "COMPSCI4023","title": "HCI Reflection",
                "description": "A personal reflection on HCI",
                "text": "The report will explore the main issues of team project in three parts: process, outcome and"
                "reflection. In the first aspect, it will describe the team process used within our group, the challenges"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "will discuss the successes obtained as well as the weaknesses, limitations and avenues for future"
                "work. Lastly, the reflections include what we gained in peer-review to improve paper quality and"
                "what I learned useful."}, 
                {"owner": "student2", "assignment_ID": "00268468",
                "SID": "2214170","module_ID": "COMPSCI4023","title": "HCI Thesis",
                "description": "A team-based thesis of HCI",
                "text": "We met twice weekly, each meeting lasted for about two hours. In the meetings, we followed the"
                "schedule from course instruction to choose some themes at each stage. Then each of us expressed"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "our opinions about the themes freely, discussed and decided for what we were going to do and how. "
                "One of us took notes for the key points and formed a weekly report. "},
                {"owner": "student2", "assignment_ID": "00268434",
                "SID": "2214170","module_ID": "COMPSCI5059","title": "Software Engineering: software design",
                "description": "A software design required by on-site mentor.",
                "text": "The report will explore the main issues of team project in three parts: process, outcome and"
                "reflection. In the first aspect, it will describe the team process used within our group, the challenges"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "will discuss the successes obtained as well as the weaknesses, limitations and avenues for future"
                "work. Lastly, the reflections include what we gained in peer-review to improve paper quality and"
                "what I learned useful."},
                {"owner": "student2", "assignment_ID": "00268495",
                "SID": "2214170","module_ID": "COMPSCI5059","title": "Software Engineering: pattern design",
                "description": "A pattern design of a software required by the on-site mentor. ",
                "text": "At the beginning, we spent much time on achieving consensus about choosing the design project."
                "One member suggested to design a visual feedback application. But the idea was vague and I"
                "misunderstood it as something with face recognizing technology which can get people’s real"
                "thought/emotion. Then based on some related literatures, we agreed the design should be an"
                "application that motivate museum/gallery visitors to equally engage in creative expression and get"
                "enhanced visiting experience from creation involvement."},
                {"owner": "student2", "assignment_ID": "00268397",
                "SID": "2214170","module_ID": "COMPSCI5029","title": "Tools about Software Project Management",
                "description": "A personal reflection on HCI",
                "text": "The second significant decision was about prototype and its interface. From week 3 to 4, each of us"
                "designed an interface for the low-fidelity device. We merged our idea as well as considered about"
                "its usability then made a preliminary interface design. Next step was that we completed a"
                "hand-made over-sized prototype together in week 5. It was really interesting because we experienced"
                "a creative process within a team."},
                {"owner": "student2", "assignment_ID": "00268499",
                "SID": "2214170","module_ID": "COMPSCI5029","title": "Software Project Management Practical Principle",
                "description": "A practical application of software project management principles",
                "text": "The third important decision was about evaluation procedure and methods. We had to decide on"
                "how we exactly conduct the experiment. I wrote a draft on briefing, experiment introduction,"
                "debriefing and possible questions for questionnaire. I suggested to adopt close-ended questions with"
                "5-point Likert Scale as well as open-ended questions to measure participants’ motivation to use"
                "visual feedback application in a real scenario and their attitudes about our design. Then other"
                "members developed full version of instructions and questionnaire."},
                {"owner": "student2", "assignment_ID": "00268335",
                "SID": "2214170","module_ID": "COMPSCI4039","title": "Coding in Practice",
                "description": "A coding test designed by on-site mentor",
                "text": "Peer-review used to improve the quality of the project in the following points: in final paper we"
                "added more theoretical supports in HCI concepts for our design; we did an extra third iteration only"
                "for questions about colors and positions of buttons. Before this we did minor changes after each"
                "iteration; in final iteration we designed some tasks ask participants to complete rather than let them"
                "interact with device intuitively. This improved respondents’ understanding towards the device."
                "what I learned useful."},
                {"owner": "student2", "assignment_ID": "00268396",
                "SID": "2214170","module_ID": "COMPSCI4039","title": "team project",
                "description": "Cooperate with other colleagues in the company",
                "text": "During the process of project, I think the biggest challenge is achieving consensus for every crucial"
                "decision. For a four-member team without related academic training (e.g. in questionnaire design"
                "and analysis), different opinions resulted in debating, we did not have a round conflicts solving"
                "mechanism and final decisions were not always the best."} ]
        
        student_three_assignment =[
                {"owner": "student3", "assignment_ID": "00268635",
                "SID": "2324220","module_ID": "COMPSCI4023","title": "HCI Reflection",
                "description": "A personal reflection on HCI",
                "text": "The report will explore the main issues of team project in three parts: process, outcome and"
                "reflection. In the first aspect, it will describe the team process used within our group, the challenges"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "will discuss the successes obtained as well as the weaknesses, limitations and avenues for future"
                "work. Lastly, the reflections include what we gained in peer-review to improve paper quality and"
                "what I learned useful."}, 
                {"owner": "student3", "assignment_ID": "00268668",
                "SID": "2324220","module_ID": "COMPSCI4023","title": "HCI Thesis",
                "description": "A team-based thesis of HCI",
                "text": "We met twice weekly, each meeting lasted for about two hours. In the meetings, we followed the"
                "schedule from course instruction to choose some themes at each stage. Then each of us expressed"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "our opinions about the themes freely, discussed and decided for what we were going to do and how. "
                "One of us took notes for the key points and formed a weekly report. "},
                {"owner": "student3", "assignment_ID": "00268634",
                "SID": "2324220","module_ID": "COMPSCI5059","title": "Software Engineering: software design",
                "description": "A software design required by on-site mentor.",
                "text": "The report will explore the main issues of team project in three parts: process, outcome and"
                "reflection. In the first aspect, it will describe the team process used within our group, the challenges"
                "we met, significant decisions we made and how. Second, outcome the project achieved. The report"
                "will discuss the successes obtained as well as the weaknesses, limitations and avenues for future"
                "work. Lastly, the reflections include what we gained in peer-review to improve paper quality and"
                "what I learned useful."},
                {"owner": "student3", "assignment_ID": "00268695",
                "SID": "2324220","module_ID": "COMPSCI5059","title": "Software Engineering: pattern design",
                "description": "A pattern design of a software required by the on-site mentor. ",
                "text": "At the beginning, we spent much time on achieving consensus about choosing the design project."
                "One member suggested to design a visual feedback application. But the idea was vague and I"
                "misunderstood it as something with face recognizing technology which can get people’s real"
                "thought/emotion. Then based on some related literatures, we agreed the design should be an"
                "application that motivate museum/gallery visitors to equally engage in creative expression and get"
                "enhanced visiting experience from creation involvement."},
                {"owner": "student3", "assignment_ID": "00268597",
                "SID": "2324220","module_ID": "COMPSCI5029","title": "Tools about Software Project Management",
                "description": "A personal reflection on HCI",
                "text": "The second significant decision was about prototype and its interface. From week 3 to 4, each of us"
                "designed an interface for the low-fidelity device. We merged our idea as well as considered about"
                "its usability then made a preliminary interface design. Next step was that we completed a"
                "hand-made over-sized prototype together in week 5. It was really interesting because we experienced"
                "a creative process within a team."},
                {"owner": "student3", "assignment_ID": "00268699",
                "SID": "2324220","module_ID": "COMPSCI5029","title": "Software Project Management Practical Principle",
                "description": "A practical application of software project management principles",
                "text": "The third important decision was about evaluation procedure and methods. We had to decide on"
                "how we exactly conduct the experiment. I wrote a draft on briefing, experiment introduction,"
                "debriefing and possible questions for questionnaire. I suggested to adopt close-ended questions with"
                "5-point Likert Scale as well as open-ended questions to measure participants’ motivation to use"
                "visual feedback application in a real scenario and their attitudes about our design. Then other"
                "members developed full version of instructions and questionnaire."},
                {"owner": "student3", "assignment_ID": "00268535",
                "SID": "2324220","module_ID": "COMPSCI4039","title": "Coding in Practice",
                "description": "A coding test designed by on-site mentor",
                "text": "Peer-review used to improve the quality of the project in the following points: in final paper we"
                "added more theoretical supports in HCI concepts for our design; we did an extra third iteration only"
                "for questions about colors and positions of buttons. Before this we did minor changes after each"
                "iteration; in final iteration we designed some tasks ask participants to complete rather than let them"
                "interact with device intuitively. This improved respondents’ understanding towards the device."
                "what I learned useful."},
                {"owner": "student3", "assignment_ID": "00268596",
                "SID": "2324220","module_ID": "COMPSCI4039","title": "team project",
                "description": "Cooperate with other colleagues in the company",
                "text": "During the process of project, I think the biggest challenge is achieving consensus for every crucial"
                "decision. For a four-member team without related academic training (e.g. in questionnaire design"
                "and analysis), different opinions resulted in debating, we did not have a round conflicts solving"
                "mechanism and final decisions were not always the best."} ]

        Students = {"student1": {"assignments": student_one_assignment},
                        "student2": {"assignments": student_two_assignment},
                        "student3": {"assignments": student_three_assignment}} 

        for stu, stu_data in Students.items():
                s = add_student(stu)
                for a in stu_data["assignments"]:
                        add_assignment(a["owner"], s, a["assignment_ID"], a["SID"], a["module_ID"], a["title"], a["description"], a["text"])

        for stu in Student.objects.all():
                for a in Assignment.objects.filter(SID=stu):
                      print("- {0} - {1}".format(str(stu), str(a)))    

def add_student(SID):
        s = Student.objects.get_or_create(SID=SID)
        s.user = user
        s.stu_name = stu_name 
        s.SID = SID
        s.major = major
        s.enroll_year = enroll_year
        s.graduate_year = graduate_year
        s.save()
        return s

def add_assignment(owner, assignment_ID,SID, module_ID, title, description, text):
        a = Assignment.objects.get_or_create(title=title, SID=SID)
        a.owner = owner
        a.assignment_ID = assignment_ID
        a.SID = SID
        a.module_ID = module_ID
        a.title = title
        a.description = description
        a.text = text
        a.save()
        return a

if __name__=='__main__':
        print("Starting ESE population script...")
populate()

        
