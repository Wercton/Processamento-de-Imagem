from matplotlib import pyplot as plt
from .Utils import exibir_imagem

def histograma(img, contraste):

    y, z, rgb = img.shape
    full_size = y*z
    size_x = 256

    pixels = [0 for x in range(size_x)]
    for i in range(y):
        for u in range(z):
            p = img.item(i, u, contraste)
            pixels[p] = pixels[p] + 1

    probabilidade = [0 for x in range(size_x)]
    for i in range(size_x):
        probabilidade[i] = pixels[i]/full_size

    freq = [0 for x in range(size_x)]
    for i in range(size_x):
        freq[i] = freq[i-1] + probabilidade[i]

    eq = [0 for x in range(size_x)]
    for i in range(size_x):
        eq[i] = int(255 * freq[i])

    dev_x = [0 for x in range(size_x)]
    for i in range(size_x):
        dev_x[i] = i

    plt.style.use("seaborn-poster")
    plt.bar(dev_x, pixels, color="#444444", label="Quantidade")
    plt.legend()
    plt.show()

    plt.bar(dev_x, probabilidade, color="#444444", label="Probabilidade")
    plt.legend()
    plt.show()

    plt.bar(dev_x, freq, color="#444444", label="Frequencia")
    plt.legend()
    plt.show()

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                x = img.itemset((i, u, j), eq[img.item(i, u, j)])

    exibir_imagem(img, f"histograma: contraste {str(contraste)}")

    print("Rk", " "*(5-len("Rk")), "| Nk", " "*(9-len("Nk")), "| Pr(rk)", " "*(9-len("Pr(rk)")),  "| Freq", " "*(9-len("Freq")), "| Eq\n")

    for i in range(size_x):
        print(dev_x[i], " "*(5-len(str(dev_x[i]))), "|", pixels[i], " "*(9-len(str(pixels[i]))), "| %.5f" % probabilidade[i], " "*(9-len("0.00000")), "| %.5f" % freq[i], " "*(9-len(str("0.00000"))), "|", eq[i])
        
    return img