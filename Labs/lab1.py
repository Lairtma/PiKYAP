import sys
import math


def get_coef(index, prompt, error_prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt, end="")
        coef_str = input()
    while True:
        try:
            coef = float(coef_str)
            break
        except:
            print(error_prompt, end="")
            coef_str = input()

    return coef


def get_roots(a, b, c):
    d = b ** 2 - (4 * a * c)
    ans = []
    pre_ans = []
    if a != 0:
        if d > 0:
            d = math.sqrt(d)
            pre_ans.append((d - b) / (2 * a))
            pre_ans.append((-d - b) / (2 * a))
            for i in pre_ans:
                if i > 0:
                    tmp = math.sqrt(i)
                    ans.append(tmp)
                    ans.append(-tmp)
                elif i == 0:
                    ans.append(0)
        elif d == 0:
            ans.append(0)
    else:
        if c < 0 and b > 0 or c > 0 and b < 0:
            tmp = math.sqrt(abs(c) / abs(b))
            ans.append(tmp)
            ans.append(-tmp)
        elif c == 0:
            ans.append(0)
    return ans


def main():
    a = get_coef(1, "Введите коэффициент А: ", "Ошибка ввода коэффициента А, повторите попытку: ")
    b = get_coef(2, "Введите коэффициент B: ", "Ошибка ввода коэффициента B, повторите попытку: ")
    c = get_coef(3, "Введите коэффициент C: ", "Ошибка ввода коэффициента C, повторите попытку: ")
    ans = sorted(get_roots(a, b, c))
    ans = list(map(str, ans))
    if len(ans) == 0:
        print("Нет корней")
    else:
        print(f"Получено {len(ans)} корней, вот они: {', '.join(ans)}")


if __name__ == "__main__":
    main()

