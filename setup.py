from setuptools import setup

console_scripts = """
cadre-test-app-serve = cadre_test_app:serve
cadre-test-app-dump-routes = cadre_test_app:dump_routes
"""

setup(name='cadre',
      version='0.1.1',
      description="Cadre framework",
      author="Jean Schurger",
      author_email='jean@schurger.org',
      packages=['cadre', 'cadre_flask'],
      install_requires=['Flask', 'fastjsonschema', 'flask-cors',
                        'decorator', 'nose', 'coverage', 'flask_jwt_extended'],
      entry_points={
          'console_scripts': console_scripts,
          'cadre.frameworks':
          ['flask = cadre_flask:FlaskFramework'],
          'cadre_test_app.controllers':
          ['test_controllers = cadre_test_controllers']
      },
      license='GPLv3')
