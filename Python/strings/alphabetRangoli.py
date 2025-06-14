# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------


def print_rangoli(n):
    width = n * 4 - 3  
    
    for i in range(n):
        
        left = [chr(97 + n - 1 - j) for j in range(i + 1)]
        right = left[:-1][::-1]  
        row = '-'.join(left + right)
        print(row.center(width, '-'))

    
    for i in range(n - 2, -1, -1):
        left = [chr(97 + n - 1 - j) for j in range(i + 1)]
        right = left[:-1][::-1]
        row = '-'.join(left + right)
        print(row.center(width, '-'))


n = int(input())  
print_rangoli(n)