
adad_mosbat = int(input())
if adad_mosbat > 1:
    for i in range (2, int(adad_mosbat/2)+1):
        if (adad_mosbat % i) == 0:
            print("not prime")
            break

    else:
        print("prime")

