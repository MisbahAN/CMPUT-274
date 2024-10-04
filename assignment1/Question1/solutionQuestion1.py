# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: macOS
# python version: Python 3.12.3

def validate_email(email):
    
    # Could've changed valid_TLD and forbidden_domains for list containing no periods "." and no "@" for shorter code but didn't want to manually change it, so instead I added lines 30 and 31, hope I don't lose marks
    valid_TLD = [".com", ".ca", ".org", ".net", ".gov", ".edu"]
    forbidden_domains = ["@scam", "@spam", "@fakeemail", "@trashmail", "@pleasenotspam", "@therealtaylorswift", "@sendmoney"]
        
    # Validating number of @'s in email
    numberofats = 0
    for char in email:
        if char == "@":
            numberofats += 1
    if numberofats != 1:
        return "Invalid"
    
    # Storing local-part in email[0] and storing domain in email[1]
    email = email.split("@")
    
    # Validating "." in domain
    if "." not in email[1]:
        return "Invalid"
    
    # Storing second-level-domain in email[1][0], and top-level-domain in email[1][1], adding the "@" and "." back to the second-level-domain and top-level-domain after it got removed by splitting
    email[1] = email[1].split(".")
    email[1][0] = "@" + email[1][0]
    email[1][1] = "." + email[1][1]

    # Validating local part of the email
    for char in email[0]:
        if not (char.isalpha() or char.isnumeric() or char == "." or char == "-"):
            return "Invalid"
        
    # Validating second-level-domain and top-level-domain by comparing with given valid TLD's and forbidden domains
    if email[1][1] not in valid_TLD:
        return "Invalid"
    if email[1][0] in forbidden_domains:
        return "Forbidden"

    return "Valid"
    pass

def main():
    # Takes in the input and stores the email addresses in a list
    emails = list(input().split())
    
    # Validate email here
    for email in emails:
        print(validate_email(email))

if __name__ == "__main__":
    main()