from operator import itemgetter
pillar_list = []
for _ in range(int(input())):
    pillar_list.append(list(map(int, input().split())))
pillar_list = sorted(pillar_list, key=itemgetter(0)) #기둥의 x 좌표 기준으로 오름차순 정렬
# print(f"정렬 된 기둥 리스트: {pillar_list}")
max_pillar_cursor, max_height = 0, 0

#max_height 기둥 위차와 높이 찾기
for i, pillar in enumerate(pillar_list):
    if pillar[1] > max_height:
        max_pillar_cursor = i
        max_height = pillar[1]
x_cursor, height_temp, area_total = 0, 0, 0

"""
max height 등장 전 까지 면적 연산
0번 기둥 ~ max height 기둥까지는 height값이 높아질 수 있다
"""

for i, pillar in enumerate(pillar_list[:max_pillar_cursor]): #max height를 가진 기둥이 나오기 전 까지
    x_cursor = pillar[0]
    if height_temp <= pillar[1]: #만약 새로 불러오는 기둥이 이전 기둥보다 높이가 크거나 같으면
        height_temp = pillar[1] #기둥 높이를 업데이트
    area = ((pillar_list[i+1][0] - 1) - (x_cursor - 1)) * height_temp  #다음 기둥 위치 직전까지 면적을 합산
    area_total += area
    # print(f"{i}기둥(x좌표:{x_cursor}) ~ {i+1}기둥(x좌표:{pillar_list[i+1][0]}) 까지 면적: {area}")

"""
0번 기둥 ~ max height등장 전 면적 합산 완료
"""

area_total += max_height #총 면적에 max_height 기둥 면적 합산

"""
max_height 기둥 이후 ~ 마지막 기둥 면적 합산
max height 기둥 이후부터 마지막기둥까지는 height값이 낮아질 수 있다
"""

x_cursor, height_temp = 0, 0 #변수 초기화
pillar_list = list(reversed(pillar_list[max_pillar_cursor:])) #max height기둥 등작 이후 리스트 뒤집기
for i, pillar in enumerate(pillar_list):
    x_cursor = pillar[0]
    if height_temp <= pillar[1]: #만약 새로 불러오는 기둥이 이전 기둥보다 높이가 크거나 같으면
        height_temp = pillar[1] #기둥 높이를 업데이트
    try:
        area = (x_cursor - pillar_list[i+1][0]) * height_temp  #다음 기둥 위치 직전까지 면적을 합산
        area_total += area
        # print(f"{i}기둥(x좌표:{x_cursor}) ~ {i+1}기둥(x좌표:{pillar_list[i+1][0]}) 까지 면적: {area}")
    except:
        pass

print(area_total)
