#DC11
#Adresy stránek

emailSRadami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org 
nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky,
 rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů 
 víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz.
"""

import re

mujRegex = re.compile(r"((http|https):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)")
#((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*
#Tohle fungovalo na regexp101 a je to obecnejsi, bohužel se mi to nepodařilo aplikovat
vystup = mujRegex.findall(emailSRadami) 
print([v[0] for v in vystup])

