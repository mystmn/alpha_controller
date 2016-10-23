import controllers.engine as ce
import config.main as config


print(config.cl_setup['ProjectName'])
print(config.cl_setup['ProjectPurpose'])

ce.Main().start()

# -->  Model can only be run within the Controller
