morphems = float(input())
if morphems < 2:
    print("Analytic")
elif 2 <= morphems <= 3:
    print("Synthetic")
elif morphems > 3:
    print("Polysynthetic")
