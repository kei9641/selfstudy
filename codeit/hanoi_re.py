def move_disk(disk_num, start_peg, end_peg):
    print('%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동' % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 중간 기둥 찾기
    for peg in range(1, 4):
        if peg != start_peg and peg != end_peg:
            middle_peg = peg
            break    
    # 탈출 조건
    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)
        return

    if num_disks % 2:
        hanoi(num_disks-1, start_peg, middle_peg)
        move_disk(num_disks, start_peg, end_peg)
    else:
        hanoi(num_disks-1, start_peg, end_peg)
        move_disk(num_disks, start_peg, middle_peg)


    

hanoi(3, 1, 3)