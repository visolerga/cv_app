# No es necesario poner nada
###############################################################################

# # Pero queda bien poner los imports mas generales y tenerlos agrupados aqui
# from .config import *
# from .dev_config import *
# from .prod_config import *
###############################################################################

# # En otro orden de cosas, si vamos a hacer que la configuracion dependa del entorno
# # entonces, tambien debemos indicarlo aqui
# import os

# ENV = os.getenv('ENV', 'development')  # Default to 'development' if ENV is not set

# if ENV == 'production':
#     from .prod_config import *
# elif ENV == 'testing':
#     from .test_config import *
# else:
#     from .dev_config import *

# # Uso en el terminal
# export ENV=production     # Set environment to production
# export ENV=testing        # Set environment to testing
###############################################################################

# OTRA opcion, es hacer una configuracion centralizada que es lo que practicaremos
import os

# Attempt to read the environment variable 'ENV'
env_variable = os.getenv('ENV')  # Read the ENV variable
print(f"\nenv_variable is set to: {env_variable}\n")  # Display the current environment

if env_variable is not None:
    ENV = env_variable.lower()  # Use the value if it exists
else:
    ENV = 'development'  # Default to 'development' if ENV is not set

print(f"\nENV is set to: {ENV}\n")  # Display the current environment

# Load the appropriate configuration based on the environment
if ENV == 'production':
    from .prod_config import *  # Production configuration
elif ENV == 'testing':
    from .test_config import *  # Testing configuration
else:
    from .dev_config import *  # Development configuration (default)

def get_config():
    """Return the current environment's configuration as a dictionary."""
    return {
        "APP_NAME": APP_NAME,
        "DATABASE_FILE": DATABASE_FILE,
        "DEBUG": DEBUG,
        "LOG_LEVEL": LOG_LEVEL,
        "LOG_DIR": LOG_DIR,
        "BASE_DIR": BASE_DIR,
    }


# # # Uso en el terminal
# # export ENV=production     # Set environment to production
# # export ENV=testing        # Set environment to testing
#
# # python src/main.py
# # Si esto no funciona hay que ir al .vscode/launch.json y crear la key 'env' a mano

# # Ejemplo de uso
# from config import get_config

# config = get_config()

# print(f"Running {config['APP_NAME']} in {'DEBUG' if config['DEBUG'] else 'PRODUCTION'} mode.")
# print(f"Database file: {config['DATABASE_FILE']}")
###############################################################################