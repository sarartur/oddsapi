from distutils.core import setup

setup(
  name = 'oddsapi',        
  packages = ['oddsapi'],  
  version = '0.1', 
  license='MIT',       
  description = 'Python wrapper around The Odds-Api.',  
  author = 'Artur Saradzhyan',                  
  author_email = 'saradzhyanartur@gmail.com',    
  url = 'https://github.com/saradzhyanartur/oddsapi', 
  download_url = 'https://github.com/saradzhyanartur/oddsapi/archive/v_01.tar.gz',   
  keywords = ['The Odds-Api', 'The Odds-API', 'Sports', 'Betting', 'Odds'], 
  install_requires=[        
          'urllib3==1.25.9',
          'certifi==2020.4.5.1',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',   
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)