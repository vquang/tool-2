import os
import yara
from global_var import *


rules_paths = [
    {
        "name": "antidebug_antivm",
        "path": "yara_rules/antidebug_antivm_index.yar"
    },{
        "name": "capabilities",
        "path": "yara_rules/capabilities_index.yar"
    },{
        "name": "crypto",
        "path": "yara_rules/crypto_index.yar"
    },{
        "name": "cve_rules",
        "path": "yara_rules/cve_rules_index.yar"
    },{
        "name": "email",
        "path": "yara_rules/email_index.yar"
    },{
        "name": "exploit_kits",
        "path": "yara_rules/exploit_kits_index.yar"
    },{
        "name": "packers",
        "path": "yara_rules/packers_index.yar"
    },{
        "name": "webshell",
        "path": "yara_rules/webshells_index.yar"
    },{
        "name": "apt_malware",
        "path": "yara_rules/apt.yar"
    },{
        "name": "pos_malware",
        "path": "yara_rules/pos.yar"
    },{
        "name": "ransom_malware",
        "path": "yara_rules/ransom.yar"
    },{
        "name": "rat_malware",
        "path": "yara_rules/rat.yar"
    },{
        "name": "toolkit_malware",
        "path": "yara_rules/toolkit.yar"
    }
]




def compileRules():
    compiled_rules = []
    rules = []
    for rule_file in rules_paths:
   
        try:
    
            rules_compiled = yara.compile(rule_file["path"])
            
            rules.append(rules_compiled) 
        except yara.Error as e:
            print(f"Error compiling rule '{rule_file['path']}': {e}")

        compiled_rules.append({
            "rules" : rules,
            "class" : rule_file["name"]
        })
        rules = []

    setCompiledRules(compiled_rules)
    return compiled_rules



