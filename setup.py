from setuptools import setup

setup(
    name='TeacherAI',
    version='0.1.0',    
    description='An AI Guitar Teacher',
    url='https://github.com/Arnottjwr/TeacherAI',
    author='Jack Arnott',
    author_email='jack.arnott@maths.ox.ac.uk',
    packages=['fretboard_trainer'],
    install_requires=['pyaudio',
                      'numpy',
                      'scipy',
                      'librosa'                     
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Musicians',
        'Operating System :: MacOS :: Linux',        
        'Programming Language :: Python :: 3.11',
    ])