def calculate_bmi(weight, height):
    return weight / (height * height)

def classify_bmi(bmi):
    if bmi < 18.5:
        return '저체중(underweight)'
    elif 18.5 <= bmi < 23:
        return '정상(normal)'
    elif 23 <= bmi < 25:
        return '과체중(overweight)'
    elif 25 <= bmi < 30:
        return '비만(obese)'
    elif 30 <= bmi < 35:
        return '고도비만(severely obese)'
    else:
        return '초고도비만(very severely obese)'

def color_bmi_category(bmi_category):
    colors = {
        '저체중(underweight)': '\033[94m',             # 파란색
        '정상(normal)': '\033[92m',                    # 초록색
        '과체중(overweight)': '\033[96m',              # 청록색
        '비만(obese)': '\033[93m',                     # 주황색
        '고도비만(severely obese)': '\033[95m',        # 자홍색
        '초고도비만(very severely obese)': '\033[91m',  # 빨간색
        'reset': '\033[0m'                             # 리셋 (색상 초기화)
    }
    return colors[bmi_category] + bmi_category + colors['reset']

def main():
    try:
        weight = float(input("체중(kg)을 입력하세요: "))
        height = float(input("키(m)을 입력하세요: "))

        bmi = calculate_bmi(weight, height)
        bmi_category = classify_bmi(bmi)
        bmi_category = color_bmi_category(bmi_category)

        print(f"당신의 BMI 지수는 {bmi:.2f}이며, {bmi_category}입니다.")
    except ValueError:
        print("\033[91m숫자만 입력해주세요(Please enter number).\033[0m")

if __name__ == "__main__":
    main()