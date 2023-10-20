###       Jacob Guzman       ###
###         CYB 333          ###
###      Course Project      ###

import webbrowser

print('||     Welcome to the CYB 333 Course Project     ||\n'
'||     This project was done by Jacob Guzman.    ||\n'
'||     The goal of the project is to create a    ||\n'
'||     security automation script using Python.  ||\n'
'||     My project was made to direct users to    ||\n'
'||     some of our favorite security scripts     ||\n'
'||     discussed this semester. =)               ||')

def open_url(url): ## assign webrowser.open to function ##
    webbrowser.open_new_tab(url)

def main_menu(): ## main menu function ##
    print("\nSelect a cybersecurity topic and a list of tools will be shown:")
    print("1. Security Automation")
    print("2. Open Source Intelligence (OSINT)")
    print("3. Network Traffic Analysis")
    print("4. Cloud Security Automation")

    choice = input("\nPick a number between 1 and 4 to make a selection. ")

    if choice == '1':
        security_automation_menu()
    elif choice == '2':
        osint_menu()
    elif choice == '3':
        network_analysis_menu()
    elif choice == '4':
        cloud_security_menu()
    else:
        print("That selection is invalid.  Please choose a number between 1 and 4")
        main_menu()

def security_automation_menu(): ## sub-menu function ##
    print("\nSecurity Automation Sub-Menu:")
    print("1. TraxOsint")
    print("2. Infection Monkey")
    print("3. CVE Bin Tool")
    print("4. OWASP-security-scanner")
    print("5. SpiderFoot")

    choice = input("Choose a tool and a web browser will direct you to the page:  ")
    open_url(security_automation_urls.get(choice, "Invalid choice."))

def osint_menu(): ## sub-menu function ##
    print("\nOpen Source Intelligence (OSINT) Sub-Menu:")
    print("1. Mr.Holmes")
    print("2. Intel Owl")
    print("3. Osintgram")
    print("4. NetworkX")
    print("5. SpiderFoot")

    choice = input("Choose a tool and a web browser will direct you to the page:  ")
    open_url(osint_urls.get(choice, "Invalid choice."))

def network_analysis_menu(): ## sub-menu function ##
    print("\nNetwork Traffic Analysis Sub-Menu:")
    print("1. TheHive Project")
    print("2. Malcolm")
    print("3. ThePhish")
    print("4. Monkey")
    print("5. PyShark")

    choice = input("Choose a tool and a web browser will direct you to the page: ")
    open_url(network_analysis_urls.get(choice, "Invalid choice."))

def cloud_security_menu(): ## sub-menu function ##
    print("\nCloud Security Automation Sub-Menu:")
    print("1. AWS Audit Automation")
    print("2. Cloudmarker")
    print("3. Boto3")
    print("4. Turbinia")
    print("5. GCP Scanner")

    choice = input("Choose a tool and a web browser will direct you to the page: ")
    open_url(cloud_security_urls.get(choice, "Invalid choice."))


security_automation_urls = { ## URL dictionary for security automation ##
    '1': 'https://github.com/N0rz3/TraxOsint.git',
    '2': 'https://github.com/guardicore/monkey',
    '3': 'https://github.com/intel/cve-bin-tool',
    '4': 'https://github.com/abhi00o7/OWASP-security-scanner',
    '5': 'https://github.com/smicallef/spiderfoot'
}

osint_urls = { ## URL dictionary for OSINT ##
    '1': 'https://github.com/Lucksi/Mr.Holmes',
    '2': 'https://github.com/intelowlproject/IntelOwl#intel-owl',
    '3': 'https://github.com/Datalux/Osintgram',
    '4': 'https://pypi.org/project/networkx/',
    '5': 'https://www.geeksforgeeks.org/spiderfoot-a-automate-osint-framework-in-kali-linux/#'
}

network_analysis_urls = { ## URL dictionary for Network Analysis ##
    '1': 'https://thehive-project.org/',
    '2': 'https://github.com/cisagov/Malcolm',
    '3': 'https://github.com/emalderson/ThePhish',
    '4': 'https://github.com/guardicore/monkey',
    '5': 'https://github.com/KimiNewt/pyshark'
}

cloud_security_urls = { ## URL dictionary for Cloud Security Automation ##
    '1': 'https://github.com/andresriancho/aws-audit-automation',
    '2': 'https://github.com/cloudmarker/cloudmarker',
    '3': 'https://github.com/boto/boto3',
    '4': 'https://github.com/google/turbinia',
    '5': 'https://github.com/google/gcp_scanner'
}

if __name__ == "__main__":
    main_menu()