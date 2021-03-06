# settings
[![GitHub license](https://img.shields.io/badge/license-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-settings/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v01.03-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-All-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/settings)

## Description
Manage (read/ write) settings file in different formats (eg. JAML, JSON, ...)

## Suppeorted standards
 - json
 - yaml/ yml

## Required
 - python3
 - pip
 
## Directories structure
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
   - workflows
     - pypi-on-push.yml
     - pypi-on-release.yml
     - python-test.yml
 - settings
	 - \_\_init\_\_.py
     - test-settings.py
 - docs
   - LICENSE
   - README.md
 - log
	 - trace.log
 - requirements
   - requirements.txt
 - .gitignore
 - setup.py
   
### Execution examples  
 ```
# Import
from settings import settings

# Inizialize
mysettings = settings(file, format) # file = file path; format = one of "json", "yml", "yaml" (default "yaml")

# Read
mysettings.read()

# Write
mysettings.write(a_dictionary_with_your_settings)
 ```

# Changelog
 - [Version_01.03_2021-03-07](#Version_0103_2021-03-07)
 - [Version_01.02_2021-02-22](#Version_0102_2021-02-22)
 - [Version_01.01_2021-02-22](#Version_0101_2021-02-22)

## Version_01.03_2021-03-07
 - Added a needed requirements

## Version_01.02_2021-02-22
 - Fixed a minor bug

## Version_01.01_2021-02-22
 - Initial version

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/settings/issues)
