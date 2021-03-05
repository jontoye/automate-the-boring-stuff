import random

def main():

    SAMPLE_SIZE = 10000
    num_of_streaks = 0

    for exp_num in range(SAMPLE_SIZE):
        streak = 1
        coin_flip = [random.choice(['H', 'T']) for i in range(100)]
        
        for i in range(1, len(coin_flip)):
            if coin_flip[i] == coin_flip[i - 1]:
                streak += 1
            else:
                streak = 1
            if streak == 6:
                num_of_streaks += 1
                break;
                

    print(f"Chance of streak: {num_of_streaks / SAMPLE_SIZE * 100}%")
    print(f"Sample size: {SAMPLE_SIZE}")


if __name__ == '__main__':
    main()