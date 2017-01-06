from setuptools import setup

setup(name='sklearn_perm_feat_import',
      version='0.1',
      description='Random Forest Feature Importance on OOB Score Delta',
      url='https://github.com/pjh2011/sklearn_oob_feat_import',
      author='Peter Hughes',
      author_email='pethug210@gmail.com',
      license='MIT',
      packages=['sklearn_perm_feat_import'],
      install_requires=[
          'numpy',
          'sklearn'
      ],
      zip_safe=False)
