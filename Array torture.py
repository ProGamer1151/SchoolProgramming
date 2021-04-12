import time
def pause():
    print("Break")
score = [[3,5,6,1,4,6,5,8] , [2,7,3,4,2,0,5,9] , [9,9,6,7,9,7,8,9]]
for a in range(0,8):
    print(score[0][a])
pause()
for b in range(0,8):
    print(score[2][b])
pause()
for c in range(0,3):
    print(score[c][0])
pause()
for d in range(0,3):
    print(score[d][2])
pause()
for e in range(0,3):
    print(score[e][7])
pause()
stud1 = 0
for f in range(0,8):
    stud1 += score[0][f]
print(stud1)
pause()
test1 = 0
for g in range(0,3):
    test1 += score[g][0]
    avg1 = test1 / 3
print(avg1)
pause()
