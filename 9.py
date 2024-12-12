with open(0) as file:
    disk_map = [int(c) for c in file.read().strip()]

def CreateBlocks(disk_map):
    disk = []
    file_id = 0
    free_space = False
    for num in disk_map:
        if free_space:
            disk.extend([-1] * num)
        else:
            disk.extend([file_id] * num)
            file_id += 1
        free_space = not free_space
    return disk

# Compute checksum when there might be free space in between disk.
def Checksum2(disk):
    return sum(i*val for i, val in enumerate(disk) if val != -1)

def LeftmostFree(disk, start):
    l = start
    while l < len(disk) and disk[l] != -1:
        l += 1
    return l

def RightmostUsed(disk, end):
    r = end
    while r >= 0 and disk[r] == -1:
        r -= 1
    return r

def Part1(disk):
    l = LeftmostFree(disk, 0)
    r = RightmostUsed(disk, len(disk) - 1)
    while l < r:
        disk[l], disk[r] = disk[r], disk[l]
        l = LeftmostFree(disk, l)
        r = RightmostUsed(disk, r)
    checksum = sum(i*val for i, val in enumerate(disk[:l]))
    return checksum

def LeftmostFreeSector(disk, start):
    l = LeftmostFree(disk, start)
    l_end = l + 1
    while l_end < len(disk) and disk[l_end] == -1:
        l_end += 1
    return l, l_end

def FreeSectors(disk):
    start, end = 0, 0
    result = []
    while True:
        while start < len(disk) and disk[start] != -1:
            start += 1
        if start == len(disk):
            return result
        end = start
        while end < len(disk) and disk[end] == -1:
            end += 1
        result.append((start, end))
        if end == len(disk):
            return result
        start = end
    return result

# Returns file_id, start_idx, end_idx (end_idx is non-inclusive of file)
def RightmostFile(disk, end):
    if end < 0:
        return None, None, None
    r = RightmostUsed(disk, end)
    i = r - 1
    while r >= 0 and disk[i] == disk[r]:
        i -= 1
    return disk[r], i + 1, r + 1

def PrintDisk(disk):
    print(''.join(str(num) if num != -1 else '.' for num in disk), end='\n\n')

def EmptyFreeSectorsRemoved(free_sectors):
    return [s for s in free_sectors if s[0] != s[1]]

def Part2(disk):
    free_sectors = FreeSectors(disk)
    file_id, src_start, src_end = RightmostFile(disk, len(disk) - 1)
    while file_id is not None:
        free_sectors = EmptyFreeSectorsRemoved(free_sectors)
        src_length = src_end - src_start
        for sector_idx in range(len(free_sectors)):
            sector_start, sector_end = free_sectors[sector_idx]
            sector_length = sector_end - sector_start
            if sector_start > src_start:
                continue
            if sector_length >= src_length:
                dst_start = sector_start
                dst_end = sector_start + src_length
                disk[dst_start:dst_end], disk[src_start:src_end] = disk[src_start:src_end], disk[dst_start:dst_end]
                free_sectors[sector_idx] = (dst_end, sector_end)
                break
        file_id, src_start, src_end = RightmostFile(disk, src_start - 1)
    return Checksum2(disk)

if __name__ == '__main__':
    disk = CreateBlocks(disk_map)
    print(Part1(disk)) # 6334655979668
    disk = CreateBlocks(disk_map)
    print(Part2(disk)) # 6349492251099
