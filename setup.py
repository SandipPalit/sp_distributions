from setuptools import setup

with open("sp_distributions/README.md", "r") as fh:
    long_description = fh.read()

setup(name='sp_distributions',
      version='0.1.2',
      license='MIT',
      author='Sandip Palit',
      author_email='sandippalit009@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      description='A statistical package to compute Mean and Standard deviation on of various Probability distributions',
      packages=['sp_distributions'],
      python_requires='>=3.6',
      zip_safe=False)