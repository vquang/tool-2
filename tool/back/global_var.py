
COMPILED_RULES = []
MALWARE_FILE = []

SQLI_FILE = '/home/user/log/sqli.log'
XSS_FILE = '/home/user/log/xss.log'
CMDI_FILE = '/home/user/log/cmdi.log'
PATH_TRAVERSAL = '/home/user/log/path-traversal.log'

def setCompiledRules(value):
    global COMPILED_RULES
    COMPILED_RULES = value


def getCompiledRules():
    return COMPILED_RULES

def setMalwareFile(value):
    global MALWARE_FILE
    MALWARE_FILE = value

def getMalwareFile():
    return MALWARE_FILE
