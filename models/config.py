import os


def config():
    return {
        'ProjectName': "Project Master Blaster has begun",
        'ProjectPurpose': "This script was created to scan a network for information",
        'Schedule': False,
        'Menu': False,
        'Logs': True,
        'Model': r'{}{}'.format(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')), "/model/")
    }
