with open("./[24]open_files/Mail Merge Project Start/starting_letter.txt") as letter:
    content = letter.read()
with open("./[24]open_files/Mail Merge Project Start/invited_names.txt") as names:
    names_list = names.readlines()

for name in names_list:
    with open(f"letter_for_{name}", mode="w") as invitation:
        stripped_name = name.strip()
        text = content.replace("[name]", stripped_name)
        invitation.write(text)
