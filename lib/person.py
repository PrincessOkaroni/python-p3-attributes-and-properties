#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Sales", "Engineer", "Manager", "ITC"]

    def __init__(self, name=None, job=None):
        self.name = None
        self.job = None
        if name is not None:
            self.set_name(name)
        if job is not None:
            self.set_job(job)

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, job):
        if job in Person.approved_jobs:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")

    pass
