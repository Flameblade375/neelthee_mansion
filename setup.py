from setuptools import setup, find_packages

setup(
    name='neelthee_mansion',
    version='1.0.0',
    packages=find_packages(),  # Automatically finds all packages and modules
    install_requires=[
        'psutil', 'playsound', 'requests', 'keyboard', 'pandas',
        # List other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'neelthee=neelthee_mansion.main:main',  # Adjust if `main` function is elsewhere
        ],
    },
    python_requires='>=3.6',  # Specify Python version compatibility
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    description='A text-based adventure game set in a mansion.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/neelthee_mansion',  # Update with your repository URL
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
)
