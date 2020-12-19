import sys
import random

while True:
	name = input("이름: (종료하려면 엔터키) ")
	if name == "":
		sys.exit()

question = input("무엇에 대하여 알고 싶은가요?")
print(name + "님", "\"", question, "\"에 대하여 질문 주셨군요.")
print("운명의 주사위를 굴려볼게요...")

answers = random. randint(1, 8)
if answer == 1:
	print("네 확실합니다. ")
elif answer == 2:
	print("전망이 좋은 거 같은데요.")
elif answer == 3:
        print("믿으셔도 됩니다.")
elif answer == 4:
        print("글쎄요 아닌거 같군요.")
elif answer == 5:
        print("한 점의 의심도 없이 맞습니다.")
elif answer == 6:
        print("그럼요, 명백히 올바른 선택을 하셨습니다.")
elif answer == 7:
        print("제 답변은 No입니다.")
else:
        print("나중에 다시 물어보세요")

