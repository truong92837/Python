#!/usr/bin/python3
from sympy import symbols, Eq, solve
from math import gcd

e = 1
c = 9327565722767258308650643213344542404592011161659991421
n =245841236512478852752909734912575581815967630033049838269083
p = 416064700201658306196320137931
q = 590872612825179551336102196593
tongpq = 243955297001875649110591178596664519421365583875937419955860634262572008253538872345495699896786789026251764371334547170212476149618376013444778474827527338147052428677920298268071440203885194814050988084198235457158014533528171242352737052474822770985257963673645191582394975053918021291330275164997228304682

## Tìm p và q từ p+q và n
def find_pq_sum(sum_val, n_val):
    p, q = symbols('p q')
    eq1 = Eq(p + q, sum_val)
    eq2 = Eq(p * q, n_val)
    solution = solve((eq1, eq2), (p, q))
    return solution

def calculate_flag(p, q):
    phi_n = (p - 1) * (q - 1)

    # Tìm ước số chung lớn nhất của e và (p-1)*(q-1) bằng thuật toán Euclid mở rộng
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return gcd, y, x - (a // b) * y

    # Tính modular inverse của e modulo (p-1)*(q-1)
    def mod_inverse(a, m):
        g, x, y = extended_gcd(a, m)
        if g != 1:
            raise ValueError("Modular inverse does not exist.")
        return x % m

    # Tính d = e^(-1) mod (p-1)*(q-1)
    d = mod_inverse(e, phi_n)

    # Tính m = c^d mod n
    m = pow(int(c), int(d), n)

    # Chuyển đổi m từ số nguyên sang dạng bytes
    flag = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')

    print()
    #print("Kết quả:")
    #print("p =", p)
    #print("q =", q)
    print("Flag:\t", flag)
    print()

# Lựa chọn chạy p, q có sẵn hoặc tính p, q từ p+q và n
option = input("(1) Có sẵn p, q \n(2) Tính p, q từ p+q và n\nNhập lựa chọn: ")

if option == "1":
    calculate_flag(p, q)
elif option == "2":
    result = find_pq_sum(tongpq, n)
    p = result[0][0]
    q = result[0][1]
    calculate_flag(p, q)
else:
    print("Lựa chọn không hợp lệ.")
    exit()
