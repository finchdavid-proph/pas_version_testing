from setuptools import setup, find_packages
setup(
    name = 'iterator_test',
    version = '1.0',
    packages = find_packages(include = ('iterator_test*', )) + ['prophecy_config_instances.iterator_test'],
    package_dir = {'prophecy_config_instances.iterator_test' : 'configs/resources/iterator_test'},
    package_data = {'prophecy_config_instances.iterator_test' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.7'],
    entry_points = {
'console_scripts' : [
'main = iterator_test.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
