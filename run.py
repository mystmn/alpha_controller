import config.main as config
from controllers.engine import Main as CE

print(config.cl_setup['ProjectName'])
print(config.cl_setup['ProjectPurpose'])
print(config.cl_setup['Model'])

CE.start()

# -->  Model can only be run within the Controller

if __name__ == '__main__':
    pass
