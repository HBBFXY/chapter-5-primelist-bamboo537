def is_prime(num):
    """判断一个数是否为质数"""
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def PrimeList(N):
    """返回小于N的所有质数，以空格分隔"""
    primes = []
    for num in range(2, N):
        if is_prime(num):
            primes.append(str(num))
    return ' '.join(primes)

# 测试示例
if __name__ == "__main__":
    print(PrimeList(10))  # 输出：2 3 5 7
