"""
languages
Estimate: 20 minutes
Actual: 18 minutes
"""

from programming_language import ProgrammingLangugage

python = ProgrammingLangugage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLangugage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLangugage("Visual Basic", "Static", False, 1991)
print(python)

lists_langugage = [python, ruby, visual_basic]

dynamic_languages = [language for language in lists_langugage if language.is_dynamic()]
print('The dynamically typed languages are:')
for language in dynamic_languages:
    print(language.name)
