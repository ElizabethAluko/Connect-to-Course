#!/usr/bin/python3
""""Module that contain all functionalies of the all"""

import random
import api_fetch

def generate_courses(courses_list):
    """generate random course"""
    random_courses = []
    count = 0
    while len(random_courses) < 10:
        course = random.choice(courses_list)
        if  course not in random_courses:
            random_courses.append(course)
        count += 1
    return random_courses


def search_courses(courses_list, search_str):
    """search for course related to search string
       return list of searches
    """
    searches = []
    for course in courses_list:
        if all(item in [x.upper() for x in course.split(" ")]
               for item in [x.upper() for x in search_str.split(" ")]):
            searches.append(course)
        elif any(item in [x.upper() for x in course.split(" ")]
               for item in [x.upper() for x in search_str.split(" ")]):
            searches.append(course)
        else:
            searches = searches

    return searches


def save_course(course):
    """add a course to list of save courses"""
    save_courses = []
    save_courses.append(course)
    return save_courses


def filter_search(courses_list, course_category=None, src=None, plan=None):
    """filter the course search
       return list of courses under args
    """
    courses = []
    if course_category is not None:
        for course in course_category:
            if course['source'] == src and course['plan'] == plan:
                courses.append(course)
    else:
        for course in courses_list:
            if course['source'] == src and course['plan'] == plan:
                courses.append(course)
    return course