from setuptools import find_packages,setup

setup(
    name="mcq_generator",
    author = "thilan hasitha",
    version="0.0.1",
    author_email="yasanjithbgth@gmail.com",
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)