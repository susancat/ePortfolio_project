
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ePortfolio_project.settings')

import django 
django.setup()
from ESE.models import Module, Competency, User, Student, Rating

def populate(): 
        programming = add_module( "Programming", "python and java, for year-1 students",
                "2018-09-17", "2018-12-20",  year=1, semester=2, level=1)
        
        add_competencies()
        software_engineering =[
                {"name": "Software Engineering", 
                "summary": "for year-2 students",
                "start_date": "2018-09-17",
                "end_date": "2018-12-20",
                "year": 2,
                "semester":3,
                "level": 1}]
        software_project_management =[
                {"name": "Software Project Management", 
                "summary": "for year-3 students",
                "start_date": "2018-01-17",
                "end_date": "2018-04-20",
                "year": 3,
                "semester":6,
                "level": 1}]
        human_computer_interaction =[
                {"name": "Human Computer Interaction", 
                "summary": "for year-4 students",
                "start_date": "2018-09-17",
                "end_date": "2018-12-20",
                "year": 4,
                "semester":7,
                "level": 1}]

        programming_comp =[
                {"name": "Programming", "description": "python and java",
                "module": "Programming",
                "group_name": "Technicals",
                "dimension_name": "Technical knowledge"}, 
                {"name": "Evaluation of tools", "description": "know how to evaluate a suitable programming tool",
                "module": "Programming",
                "group_name": "Technicals",
                "dimension_name": "Use of technology"}, 
                {"name": "Communication", "description": "communicate with other team members",
                "module": "Programming",
                "group_name": "Socials",
                "dimension_name": "Interpersonal relations"}, 
                {"name": "Desire to contribute", "description": "be productive",
                "module": "Programming",
                "group_name": "Socials",
                "dimension_name": "Cooperation and work in team"}, 
                {"name": "Judgment and common sense", "description": "can do right selection",
                "module": "Programming",
                "group_name": "Socials",
                "dimension_name": "Handling and solving conflicts"}, 
                {"name": "Capacity to search information", "description": "can collect information with good quality",
                "module": "Programming",
                "group_name": "Personals",
                "dimension_name": "Development in the job environment"}, 
                {"name": "Personal commitment", "description": "can achieve what he/she promised",
                "module": "Programming",
                "group_name": "Personals",
                "dimension_name": "Personal development"}, 
                {"name": "To suggest arrangement or alternative solutions", "description": "provide different ideas and solutions",
                "module": "Programming",
                "group_name": "Personals",
                "dimension_name": "Rights and limits"}]

        software_engineering_comp = [
                {"name": "Software design", "description": "design pattern and diagrams",
                "module": "Software Engineering",
                "group_name": "Technicals",
                "dimension_name": "Technical knowledge"}, 
                {"name": "Selection of tools", "description": "know how to select a suitable programming tool",
                "module": "Software Engineering",
                "group_name": "Technicals",
                "dimension_name": "Use of technology"}, 
                {"name": "Aptitude to relate", "description": "find out relations",
                "module": "Software Engineering",
                "group_name": "Socials",
                "dimension_name": "Interpersonal relations"}, 
                {"name": "Motivation", "description": "eager to do coding",
                "module": "Software Engineering",
                "group_name": "Socials",
                "dimension_name": "Cooperation and work in team"}, 
                {"name": "Resolution of conflicts", "description": "confilcts always happen in software design",
                "module": "Software Engineering",
                "group_name": "Socials",
                "dimension_name": "Handling and solving conflicts"}, 
                {"name": "Capacity to learn along", "description": "learn and think alone ",
                "module": "Software Engineering",
                "group_name": "Personals",
                "dimension_name": "Development in the job environment"}, 
                {"name": "To learn of past actions to project future result", "description": "reflection and rethinking",
                "module": "Software Engineering",
                "group_name": "Personals",
                "dimension_name": "Personal development"}, 
                {"name": "Ability of arguing for rights and needs", "description": "not give up for right things",
                "module": "Software Engineering",
                "group_name": "Personals",
                "dimension_name": "Rights and limits"}]
        
        software_project_management_comp = [
                {"name": "Project management", "description": "design pattern and diagrams",
                "module": "Software Project Management",
                "group_name": "Technicals",
                "dimension_name": "Technical knowledge"}, 
                {"name": "Adaptation", "description": "know how to select a suitable programming tool",
                "module": "Software Project Management",
                "group_name": "Technicals",
                "dimension_name": "Use of technology"}, 
                {"name": "Sociability", "description": "find out relations",
                "module": "Software Project Management",
                "group_name": "Socials",
                "dimension_name": "Interpersonal relations"}, 
                {"name": "Leadership", "description": "eager to do coding",
                "module": "Software Project Management",
                "group_name": "Socials",
                "dimension_name": "Cooperation and work in team"}, 
                {"name": "Aptitude to listen to others", "description": "confilcts always happen in software design",
                "module": "Software Project Management",
                "group_name": "Socials",
                "dimension_name": "Handling and solving conflicts"}, 
                {"name": "Stress resistance", "description": "learn and think alone ",
                "module": "Software Project Management",
                "group_name": "Personals",
                "dimension_name": "Development in the job environment"}, 
                {"name": "To evaluate required resources", "description": "reflection and rethinking",
                "module": "Software Project Management",
                "group_name": "Personals",
                "dimension_name": "Personal development"}, 
                {"name": "To know the rules and identify limits", "description": "not give up for right things",
                "module": "Software Project Management",
                "group_name": "Personals",
                "dimension_name": "Rights and limits"}]

        human_computer_interaction_comp = [
                {"name": "Requirement analysis", "description": "design pattern and diagrams",
                "module": "Human Computer Interaction",
                "group_name": "Technicals",
                "dimension_name": "Technical knowledge"}, 
                {"name": "Use tools to support areas", "description": "know how to select a suitable programming tool",
                "module": "Human Computer Interaction",
                "group_name": "Technicals",
                "dimension_name": "Use of technology"}, 
                {"name": "interpersonal sensibility", "description": "find out relations",
                "module": "Human Computer Interaction",
                "group_name": "Socials",
                "dimension_name": "Interpersonal relations"}, 
                {"name": "DEcision Making", "description": "eager to do coding",
                "module": "Human Computer Interaction",
                "group_name": "Socials",
                "dimension_name": "Cooperation and work in team"}, 
                {"name": "The skills of negotiating", "description": "confilcts always happen in software design",
                "module": "Human Computer Interaction",
                "group_name": "Socials",
                "dimension_name": "Handling and solving conflicts"}, 
                {"name": "Flexibility", "description": "learn and think alone ",
                "module": "Human Computer Interaction",
                "group_name": "Personals",
                "dimension_name": "Development in the job environment"}, 
                {"name": "Balance resources and goals", "description": "reflection and rethinking",
                "module": "Human Computer Interaction",
                "group_name": "Personals",
                "dimension_name": "Personal development"}, 
                {"name": "Ability to understand one's own interests and needs", "description": "not give up for right things",
                "module": "Human Computer Interaction",
                "group_name": "Personals",
                "dimension_name": "Rights and limits"}]

'''
        Modules = {"Human Computer Interaction": {"competencies": human_computer_interaction_comp},
                        "Software Project Management": {"competencies": software_project_management_comp},
                        "Software Engineering": {"competencies": software_engineering_comp},
                        "Programming": {"competencies": programming_comp}} 
'''
        
        for m in Module.objects.all():
                for c in Competency.objects.filter(module=m):
                      print("- {0} - {1}".format(str(m), str(c))  

def add_module(name,summary,start_date,end_date,year,semester,level):
        m = Module.objects.get_or_create(name=name,summary = summary,start_date = start_date,end_date = end_date,year = year,semester = semester,level = level)
        #m.save()
        return m

def add_competencies(name, description, module, group_name, dimension_name):
        c = Competency.objects.get_or_create(name=name, module=module,description = description,group_name = group_name,dimension_name = dimension_name)
        #c.save()
        return c

if __name__=='__main__':
        print("Starting breakfast population script...")
populate()
