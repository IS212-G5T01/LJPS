from backend.app import JobRole, Skill, getAllJobRole, getskills, createSkills
from flask import Flask
import json
import pytest 

#----------- test_create_job_role ------------------
def test_create_job_role_success():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = JobRole('Human Resource', 'HR', 0)
    assert test_job_role.job_role_name == 'Human Resource'
    assert test_job_role.job_role_desc == 'HR'
    assert test_job_role.job_role_status == 0

def test_create_job_role_invalid_name():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_name
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole(123, 'HR', 0)

def test_create_job_role_invalid_desc():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_desc
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 123, 0)

def test_create_job_role_invalid_status():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_status
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 'HR', '0')\

def test_create_job_role_invalid_parameters():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with invalid amount of parameters
    THEN check the TypeError is raised
    """
    with pytest.raises(Exception):
        JobRole(0, 'Human Resource', 'HR', 0)

def test_view_job_role_success():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = JobRole('Human Resource', 'HR', 0)
    assert test_job_role.json()['job_role_name'] == 'Human Resource'
    assert test_job_role.json()['job_role_desc'] == 'HR'
    assert test_job_role.json()['job_role_status'] == 0


#----------- test_view_job_role ------------------
def test_view_job_role_success():
    app = Flask(__name__)

    test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getAllJobRole([ 
            JobRole(test_data[0][0], test_data[0][1], test_data[0][2]),
            JobRole(test_data[1][0], test_data[1][1], test_data[1][2]),
            JobRole(test_data[2][0], test_data[2][1], test_data[2][2])
        ])

        assert result_data.json['code'] == 200
        assert len(result_data.json['data']) == 3
        for i in range(len(test_data)):
            assert result_data.json['data'][i]['job_role_name'] == test_data[i][0]
            assert result_data.json['data'][i]['job_role_desc'] == test_data[i][1]
            assert result_data.json['data'][i]['job_role_status'] == test_data[i][2]


def test_skill_success():
#-------------------------test class Skill-----------------------------------
def test_class_skill_success():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    skill = Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status=1)
    assert skill.skill_name == "Python"
    assert skill.skill_desc == "Python is a programming language"
    assert skill.skill_status == 1

def test_class_skill_invalid_skill_name():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_name
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name=0, skill_desc="Python is a programming language", skill_status=1)

def test_class_skill_invalid_skill_desc():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_desc
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name="Python", skill_desc=0, skill_status=1)

def test_class_skill_invalid_skill_status():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_status
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status="1")

def test_class_skill_invalid_parameters():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with invalid amount of parameters parameters
    THEN check the Exception is raised
    """
    with pytest.raises(Exception):
        Skill(skill_id=0, skill_name=0, skill_desc=0, skill_status="1")

#----------- test class JobRole ------------------
def test_create_job_role_invalid_name():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_name
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole(123, 'HR', 0)

def test_create_job_role_invalid_desc():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_desc
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 123, 0)

def test_create_job_role_invalid_status():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_status
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 'HR', '0')\

def test_create_job_role_invalid_parameters():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with invalid amount of parameters
    THEN check the TypeError is raised
    """
    with pytest.raises(Exception):
        JobRole(0, 'Human Resource', 'HR', 0)

def test_view_job_role_success():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = JobRole('Human Resource', 'HR', 0)
    assert test_job_role.json()['job_role_name'] == 'Human Resource'
    assert test_job_role.json()['job_role_desc'] == 'HR'
    assert test_job_role.json()['job_role_status'] == 0

#-------------------------test function getskills-----------------------------------
def test_get_skills_success():
    """
    GIVEN a getskills function
    WHEN getskills is called
    THEN check the response code is 200 and the data is returned as per expected
    """
    app = Flask(__name__)
    test_data = test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getskills([
            Skill(test_data[0][0], test_data[0][1], test_data[0][2]),
            Skill(test_data[1][0], test_data[1][1], test_data[1][2]),
            Skill(test_data[2][0], test_data[2][1], test_data[2][2])
        ])
        assert result_data.json['code'] == 200
        assert len(result_data.json['data']) == 3
        for i in range(len(test_data)):
                assert result_data.json['data'][i]['skill_name'] == test_data[i][0]
                assert result_data.json['data'][i]['skill_desc'] == test_data[i][1]
                assert result_data.json['data'][i]['skill_status'] == test_data[i][2]

#-------------------------test function createSkills-----------------------------------
def test_new_skill():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skill_status, skill_name, skill_desc are defined correctly
    """
    app = Flask(__name__)

    test_data = {
        "skill_name": "Python",
        "skill_desc": "Python is a programming language",
        "skill_status": 1
    }

    with app.app_context():
        result_data = createSkills(test_data)
        assert result_data.json['code'] == 200
        assert result_data.json['data']['skill_status'] == 1
        assert result_data.json['data']['skill_name'] == "Python"
        assert result_data.json['data']['skill_desc'] == "Python is a programming language"


#----------- test_view_job_role ------------------
def test_view_job_role_success():
    app = Flask(__name__)

    test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getAllJobRole([ 
            JobRole(test_data[0][0], test_data[0][1], test_data[0][2]),
            JobRole(test_data[1][0], test_data[1][1], test_data[1][2]),
            JobRole(test_data[2][0], test_data[2][1], test_data[2][2])
        ])

        assert result_data.json['code'] == 200
        assert len(result_data.json['data']) == 3
        for i in range(len(test_data)):
            assert result_data.json['data'][i]['job_role_name'] == test_data[i][0]
            assert result_data.json['data'][i]['job_role_desc'] == test_data[i][1]
            assert result_data.json['data'][i]['job_role_status'] == test_data[i][2]





    
