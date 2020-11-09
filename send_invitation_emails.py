import pandas as pd
import os

names_emails = pd.read_csv("invite_list.csv", skipinitialspace=True,
                           dtype={'Name01':str,'Name02':str,'Email':str})

for n, invite in names_emails.iterrows():
    if isinstance(invite["Name02"], str):
        dear = f'Dear {invite["Name01"]} and {invite["Name02"]},'
    else:
        dear = f'Dear {invite["Name01"]},'

    email = f"{dear}\n\nYou are cordially invited to attend the wedding ceremony and reception of Lynn Palmeri and Conor Beardsley.\n\nPlease visit the following website for information and RSVP instructions: http://lynn-and-conor-wedding.palmeri.io\n\nWe hope to see you in February!\nLynn and Conor\n\n"

    email_file = f"email_body.txt"

    with open(email_file, "w") as email_body:
        email_body.write(email)

    cmd = f'mail -r "lynn-and-conor-wedding@palmeri.io (Lynn & Conor)" -s "Lynn Palmeri and Conor Beardsley Wedding" {invite["Email"]} < {email_file}'

    os.system(f"cat {email_file}")
    print(cmd)

    os.remove(email_file)
