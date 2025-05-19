from setuptools import find_packages, setup

# additional requirements
import os
from glob import glob

package_name = 'viz_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # put folders we created
        # launch folder
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # if more folders or files needed, add below
        (os.path.join('share', package_name, 'xacro'), glob('xacro/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kisangpark',
    maintainer_email='kisangpark@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

            # put user defined executables below
            # be aware of format!
            # 'executable_name = package_name.file_name:main',
        ],
    },
)
