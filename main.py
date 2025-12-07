from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "student_government": {
                "name": "Student Government",
                "overview": "The Student Government serves as the voice representing the entire student body, fostering leadership, equality, and unity within our halls.  ",
                "schedule": "Every Monday and Thursday 3:00-5:30 PM",
                "venue": " Student Affairs Conference Room; Orion Hall",
                "faculty": "Dean Emmeline Draven",
                "members": 32,
                "domain": "Leadership Training"
            },
            "specialty_interest_groups": {
                "name": "Specialty Interest Groups",
                "overview": "The Specialty Interest Groups of Polaris College of Medicine aim to explore and deepen their focus on specific medical fields. ",
                "schedule": "Every Wednesday to Friday 4:00-7:00 PM",
                "venue": "Specialty Training Suite; Auriga Tower, Floor 2",
                "faculty": "Professor Raphael Cromwell",
                "members": 38,
                "domain": "Academic"
            },
            "research_and_innovation": {
                "name": "Research and Innovation",
                "overview": "The Research and Innovation Club of Polaris College of Medicine is dedicated to advancing scientific knowledge through experimentation, analysis, and collaboration. ",
                "schedule": "Every Tuesday 4:30-8:00 PM",
                "venue": "Adromeda Research Lab",
                "faculty": "Professor Ekaterina Zaitsev",
                "members": 46,
                "domain": "Academic"
            },
            "sports_and_recreation": {
                "name": "Sports and Recreation",
                "overview": "The Sports and Recreation Division promotes discipline, teamwork, and physical wellness among students.  ",
                "schedule": "Every Monday, Wednesday, Friday 3:30-5:00 PM",
                "venue": "Apollo Gymnasium; Campus Recreation Center",
                "faculty": "Mister Cameron Zhang",
                "members": 29,
                "domain": "Life and Wellness"
            },
            "cultural_and_arts": {
                "name": "cultural arts",
                "overview": "The Cultural Arts Division celebrates diversity, creativity, and self-expression through performance and literary arts.  ",
                "schedule": "Every Wednesday 3:15-6:30 PM",
                "venue": "Cassiopeia Studio; Rigel Studio",
                "faculty": "Miss Daphne Tsukino",
                "members": 43,
                "domain": "Creative Development"
            },
            "": {
                "name": "",
                "overview": "",
                "schedule": "",
                "venue": "",
                "faculty": "",
                "members": "",
                "domain": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Overview:{info['overview']}
            Schedule {info['schedule']}
            Venue : {info['venue']}
            Faculty: {info['faculty']}
            Members: {info['members']}
            Domain: {info['domain']}
            """
    display(output, target="club-info")
