import sys
input = sys.stdin.readline

address_must_length = 8
short_address = input().strip()

# zfill(4) 사용해서 0001 형태 만들기 (string에 사용가능)

address_list = short_address.split(":")

if "::" in short_address:
    left, right = short_address.split("::")
    left = left.split(":") if left else [] # 비어있지 않는 것 체크
    right = right.split(":") if right else [] # 비어있지 않는 것 체크

    # print(left, len(left))
    # print(right, len(right))

    missing = address_must_length - ( len(left) + len(right) )

    result = left + ["0000"] * missing + right # list 형태로 합쳐진다.

    # print(result)
    print(":".join(x.zfill(4) for x in result))

else:
    print(":".join(address.zfill(4) for address in address_list))