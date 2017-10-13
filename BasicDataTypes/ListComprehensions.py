x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
ar = []
p = 0
for i in range (x + 1) :
    for j in range ( y + 1) :
          for k in range (z + 1) :
              if i + j + k != n :
                  # list 추가
                  ar.append([])
                  ar[p] = [ i, j, k ]
                  p += 1
print ar
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print [ [i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1
) if ( ( i + j + k ) != n )]
'''
