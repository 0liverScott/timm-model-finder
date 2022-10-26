import timm

while True:
    keyword = input("""
Input keyword. '*' means anything. ex)"*effi*ns*"
""")
    pt = input("""
0: Pretrained = False
1: Pretrained = True
""")
    model_names = timm.list_models(str(keyword), pretrained=False if pt == 0 else 1)
    print('=' * 50)
    for name in model_names:
        print(name)
    print('=' * 50)
