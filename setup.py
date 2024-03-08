from setuptools import setup, find_packages

setup(
    name='cha',
    version='0.2.5',
    packages=find_packages(),
    license='MIT',
    description="A simple CLI chat tool to easily interface with OpenAI's LLM models",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'openai==1.13.3',
        'beautifulsoup4==4.12.3',
        'selenium==4.18.1',
        'webdriver-manager==4.0.1',
        'yt-dlp==2023.12.30'
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'cha = cha.main:cli',
        ],
    },
)

