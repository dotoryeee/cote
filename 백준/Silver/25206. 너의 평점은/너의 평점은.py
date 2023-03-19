import sys
data = []
for _ in range(20):
    data.append(list(sys.stdin.readline().split()))
score_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F" : 0.0
}
total_credit = 0 #수강 학점
total_score = 0.0 #전공 성적 합산 (학점 * 과목평점)
for line in data:
    if line[2] != "P":
        total_score += float(line[1]) * score_dict[line[2]]
        total_credit += float(line[1])
print(f"{total_score/total_credit:.6f}")