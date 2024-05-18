from bg3Questions import bg3Questions

bgquestion_prompts = ["Which character consumes magical items?\n(a) Lae'zel\n(b) Wyll\n(c) Gale\n(d) Shadowheart\n",
                      "Which NPC is Bhaals chosen?\n(a) Orin\n(b) Kethric Thorm\n(c) Gortash\n(d) Zevlor\n",
                      "You can save this NPC from a windmill:\n(a) Wulbren\n(b) Withers\n(c) Alfira\n(d) Barcus\n",
                      "The nightsong is:\n(a) an artifact\n(b) Dame Aylin\n(c) a tiefling\n(d) Kethric's daughter\n",
                      "You can gain this companion on the Nautiloid:\n(a) Us\n(b) Scratch\n(c) Tara\n(d) Grub\n",
                      "You can find this clown in pieces:\n(a) Bozo\n(b) Drippy\n(c) Dribbles\n(d) Raphael\n",
                      "You can free this pixie:\n(a) Dolly\n(b) Polly\n(c) Flora\n(d) Lolly\n",
                      "You're timed to take his head:\n(a) Glut\n(b) Orpheus\n(c) Balthazar\n(d) Nere\n",
                      ]
questions = [
    bg3Questions(bgquestion_prompts[0], "c"),
    bg3Questions(bgquestion_prompts[1], "a"),
    bg3Questions(bgquestion_prompts[2], "d"),
    bg3Questions(bgquestion_prompts[3], "b"),
    bg3Questions(bgquestion_prompts[4], "a"),
    bg3Questions(bgquestion_prompts[5], "c"),
    bg3Questions(bgquestion_prompts[6], "a"),
    bg3Questions(bgquestion_prompts[7], "d"),
]
def run_test(questions):
    score = 0
    for questions in questions:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score +=1
    print("You have scored " +str(score) + "/" + str(len(bgquestion_prompts)))

run_test(questions)






