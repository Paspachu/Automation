# Read answers from answers.txt
with open("answers.txt") as file:
    lines = [line.rstrip() for line in file]

# Insert '\(' in front of "begin{align*}" and '\)' behind "end{align*}"
for i in range(len(lines)):
    if "begin{align*}" in lines[i]:
        lines[i] = "\(" + lines[i]
    if "end{align*}" in lines[i]:
        lines[i] = lines[i] + "\)"

answers = []
start = 0
for i in range(len(lines)):
    if "Solution:" in lines[i]:
        start = i + 1
        continue
    if "section*" in lines[i]:
        answers.append(lines[start:i])

with open('updated.txt', 'w') as f:
    num = 1
    for ans in answers:
        f.write(f"Problem{num}\n")
        num += 1
        for line in ans:
            f.write(f"{line}\n")